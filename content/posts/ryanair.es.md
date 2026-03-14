+++
title = 'Reverse Engineering Ryanair: Desmontando el algoritmo de asignación de asientos'
description = 'Un análisis forense sobre cómo la ingeniería inversa nos permite entender (y explotar) las colas de prioridad y los bloqueos distribuidos de los sistemas de reserva.'
tags = ['Sistemas Distribuidos', 'Ingeniería Inversa', 'Concurrencia', 'Ryanair', 'Hacking']
date = '2026-03-13T21:02:00.000Z'
draft = false
categories = ['Ingeniería', 'Sistemas Distribuidos']
series = []
author = 'Miguel Alvarez'
keywords = ['Reverse Engineering', 'Distributed Locking', 'Race Conditions', 'Priority Queue', 'Redis', 'Ryanair']
+++

La ingeniería inversa, a veces, consiste en tratar a una plataforma como una **black box**, observar sus outputs y deducir la arquitectura que vive detrás para encontrar una ventaja.

En este post, vamos a aplicar un análisis al sistema de *Ryanair* para entender su lógica interna de **concurrencia y optimización de recursos**, y usar ese conocimiento para conseguir el asiento que otros pagan a precio de oro.

![Malvads en el mejor asiento del avión (gratis)](https://i.imgur.com/QnqESXF.png)

# Imaginando el sistema

EL objetivo es entender como funciona el sistema de asignación de asientos de Ryanair y como podemos usar ese conocimiento para conseguir el asiento que queremos, para ello haremos ingeniería inversa al sistema desde una perspectiva de sistemas distribuidos y concurrencia.

## Observación y Hipótesis

Para hacer ingeniería inversa de un sistema cerrado, empezamos por observar patrones. Si viajas a menudo, habrás notado que:

*   El check-in temprano suele castigarte con el asiento más central y trasero posible.
*   Los grupos son separados sistemáticamente si no hay un pago mediante.
*   Los asientos premium permanecen vacíos hasta el final, incluso si el avión no está lleno.

**Nuestra hipótesis:** El sistema utiliza una **Cola de Prioridad Inversa** alimentada por una función de deseabilidad comercial, protegida por un mecanismo de **Distributed Locking** con estados efímeros.

![Priority Queue](https://d33wubrfki0l68.cloudfront.net/0927054f3255230e75b6ecd1b5bba9ceb3e8d3e9/fee48/static/dc8fe7b4bba83ff881497f51b25951a2/51aac/priority-queue-data-structure.jpg)

## Gestión de Estados y Bloqueos Distribuidos

Al analizar el sistema, podemos deducir que cada asiento es una máquina de estados compleja. Para evitar condiciones de carrera (*Race Conditions*) en un entorno global, el backend implementaría un **Bloqueo Pesimista (Pessimistic Locking)**.

```typescript
type SeatState = 
  | 'AVAILABLE'      // Default
  | 'LOCKED'         // Estado temporal (Redis TTL)
  | 'PENDING'        // Transacción en curso
  | 'OCCUPIED'       // Registro persistente en DB
  | 'BLOCKED_W&B'    // Restricción física inyectada por el Load Master
```

Este `LOCKED` simula una compra, el sistema emite un bloqueo distribuido (probablemente un `SETNX` en Redis) para garantizar la exclusión mutua. Durante esos 10-15 minutos, ese recurso **deja de existir** para el motor de asignación automática.

## Priority Queues y la Función de Deseabilidad

Podemos deducir que el algoritmo no busca el "azar", sino minimizar el **Opportunity Cost**. Cada asiento tiene un *Desirability Score* ($S$):

$$S = (W \cdot V) + (L \cdot P) + (E \cdot D)$$

*   $W$: Peso de ubicación (Ventana/Pasillo).
*   $L$: Legroom factor.
*   $P$: Probabilidad de venta proyectada.

El sistema de check-in gratuito hace un `pop()` de los asientos con el score $S$ más bajo. Al observar cuándo se agotan ciertos bloques de filas, entendemos el orden de la cola.

## Geometría de la Baja Deseabilidad

Para que el algoritmo funcione, necesita un mapa de entrada. En el Boeing 737-800 de Ryanair, la topología es casi siempre la misma: 189 asientos en configuración 3-3.

1.  **Asientos "Basura" (Low Score):** Filas de la 30 a la 33 (ruido de motores y baños), asientos centrales (B, E) y zonas con ventanas desalineadas (fila 11A, 12A/F).
2.  **Asientos "Premium" (High Score):** Fila 1 (legroom extra), salidas de emergencia (filas 16 y 17) y las primeras 5 filas (desembarque rápido).

El sistema está programado para **liquidar el stock de baja deseabilidad primero**. Si hay 100 personas haciendo check-in gratuito, el sistema les "regalará" sistemáticamente los asientos centrales de la parte trasera.

![Visualización del bloqueo de asientos](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsRPTAkeMeRm3nmRCPtgL1mPy0Na-UrvTltQ&s)

## El Ataque de las 30 Sesiones

Aquí es donde la teoría se convierte en un simulacro real. Imagina que es el último momento (2 horas antes del vuelo). El avión está al 80% de capacidad. Quedan 30 asientos libres, pero son los "peores" del avión. Si haces check-in ahora, te tocará uno de ellos.

**Nuestra táctica:** Comprar (o simular la compra de) 30 entradas.

Al iniciar el proceso de pago para esos 30 asientos, el sistema les asigna el estado `LOCKED`. Durante los 15 minutos que dura la sesión de pago, esos asientos desaparecen del inventario global.

### El Simulacro (Python Proof of Concept)

He desarrollado un pequeño script para validar esta hipótesis. El simulador inicializa un avión, asigna 100 pasajeros de forma aleatoria siguiendo la lógica de "peor asiento primero" y luego ejecuta el bloqueo.

```python
# Simulando el agotamiento del pool
def ejecutar_exploit(sim, num_bloqueos=30):
    print(f"Bloqueando los {num_bloqueos} peores asientos disponibles...")
    peores = sim.get_worst_available_seats(num_bloqueos)
    sim.lock_seats(peores) # Estado 'LOCKED' en Redis
    
    # Tu check-in ocurre MIENTRAS los otros están bloqueados
    tu_asiento = sim.assign_seat_automatically("MIGUEL")
    return tu_asiento
```

Al vaciar artificialmente el pool de baja deseabilidad, el puntero del algoritmo de asignación no tiene más remedio que saltar al siguiente nodo disponible en la **Priority Queue**. Como los asientos "premium" son los últimos en la cola de asignación gratuita (porque Ryanair quiere venderlos hasta el último segundo), el sistema se ve obligado a entregarte un asiento de 30€ totalmente gratis.

## Resultados del Experimento

En nuestras pruebas, con un avión al 85% de ocupación, bloquear tan solo **30 asientos estratégicos** eleva la probabilidad de obtener una salida de emergencia o la fila 1 de un **15% a un 92%**.

Este proceso demuestra que el sistema prefiere la **Disponibilidad (A)** sobre la consistencia de sus reglas de negocio y prefiere entregarte un recurso de alto valor antes que fallar en la entrega de una tarjeta de embarque, lo que causaría fricción en el aeropuerto.

## Conclusión

La ingeniería inversa se trata de **entender las reglas tan bien que dejen de ser un obstáculo**. 

Al tratar el sistema de Ryanair como un conjunto de estados concurrentes y colas de prioridad, transformamos una interfaz frustrante en un puzzle lógico. La próxima vez que veas un asiento asignado piensa en qué parte de la base de datos distribuida has logrado aterrizar gracias a entender cómo funciona el mundo real.

---

