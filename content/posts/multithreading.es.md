+++
title = 'Entiende de una vez por todas el multithreading y multiprocessing'
description = '¿Hilos o Procesos? Entiende cómo escalar tu software.'
tags = ['Concurrencia', 'Programación', 'Sistemas Operativos']
date = '2026-03-09T00:00:00.000Z'
draft = false
categories = ['Desarrollo de Software']
series = []
author = 'Miguel Alvarez'
keywords = ['Multithreading', 'Multiprocessing', 'GIL', 'Race Condition', 'Context Switch']

[cover]
image = ""
relative = true
+++

Programar suele compararse con seguir una receta. Pero cuando queremos que nuestro software sea profesional, no basta con que la receta funcione, necesitamos que el restaurante sea capaz de servir a cien personas a la vez sin quemar la cocina.

Hoy vamos a explorar el mundo de la **concurrencia** y el **paralelismo**. Si alguna vez te has preguntado por qué tu programa va lento a pesar de tener un procesador de última generación, la respuesta está en cómo gestionas tus **hilos y procesos**.

### Hardware Threads vs. Software Threads

Imagina que los **Hardware Threads** son los **cocineros físicos** que tienes en la cocina (los núcleos lógicos de tu CPU). Si tu procesador tiene 8 hilos, tienes 8 pares de manos trabajando.

Por otro lado, los **Software Threads** son las **tareas anotadas en comandas**. Un solo cocinero (hardware thread) puede estar a cargo de varias comandas (software threads). El sistema operativo hace un **Context Switch** (cambio de contexto), el cocinero deja de picar cebolla un segundo para remover la sopa y luego vuelve a la cebolla. A ojos del cliente, parece que está haciendo ambas cosas a la vez, pero en realidad está alternando rápidamente entre ellas (¿mágico verdad?).

{{< figure src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter4/4_01_ThreadDiagram.jpg" title="Figura 1: Diagrama de hilos y procesos en el sistema operativo." >}}

### El GIL y el GVL

En lenguajes como **Python (CPython)** o **Ruby (MRI)**, existe un personaje muy estricto, el **GIL (Global Interpreter Lock)**. 

Imagina que, aunque tengas 10 cocineros, solo hay un **cucharón oficial**. Para que un cocinero ejecute cualquier instrucción del código, debe tener el cucharón. Esto garantiza que nadie corrompa la "receta" (la gestión de memoria del intérprete), pero impide el **paralelismo real** en tareas pesadas.

* **CPU-Bound (Cálculos pesados):** Como picar 50kg de carne. El GIL hace que los cocineros se peleen por el cucharón, haciendo que el multithreading sea inútil. Aquí es donde brilla el **Multiprocessing**.
* **I/O-Bound (Espera de red/disco):** Como esperar a que el horno suene. El cocinero suelta el cucharón mientras espera, permitiendo que otro avance. Aquí el **Multithreading** o el **Async I/O** son extremadamente eficientes.

{{< figure src="https://static-assets.codecademy.com/understanding-gil-in-python/GIL-behaviour.png" title="Figura 2: Funcionamiento del Global Interpreter Lock (GIL)." >}}

### Condición de Carrera (Race Condition)

Imagina una variable compartida llamada `sal_en_la_sopa = 0`. 
Dos hilos (cocineros) quieren añadir una pizca de sal:
1.  **Hilo A** lee que hay 0 de sal.
2.  **Hilo B** lee que hay 0 de sal.
3.  **Hilo A** suma 1 y escribe: "Hay 1 de sal".
4.  **Hilo B** suma 1 y escribe: "Hay 1 de sal".

¡Error! Debería haber 2 de sal, pero el resultado es 1. Esto es una **Race Condition**. El resultado final depende de quién llegó último a escribir en la memoria.

{{< figure src="https://media.geeksforgeeks.org/wp-content/uploads/20201228232441/gfgdiagram.png" title="Figura 3: Condición de carrera al acceder a memoria compartida." >}}

### Mutex y Sincronización

Para evitar que dos cocineros metan la mano en la misma olla, usamos un **Mutex (Mutual Exclusion)**. Es un cerrojo en la puerta de la sección crítica del código. Si un hilo entra, echa la llave; los demás deben esperar en la cola (**Block**) hasta que la llave quede libre.

Sin embargo, si no tenemos cuidado, podemos caer en un **Deadlock** (Bloqueo mutuo):
* El Cocinero A tiene la llave del *Horno* y espera la del *Cuchillo*.
* El Cocinero B tiene la llave del *Cuchillo* y espera la del *Horno*.
Ninguno se mueve. El programa se congela.

{{< figure src="https://miro.medium.com/v2/resize:fit:1200/1*nT6M9U44up3hYJoQjohC3A.png" title="Figura 4: El problema del bloqueo mutuo (Deadlock)." >}}

### ¿Cocina compartida o Restaurantes independientes?

Aquí es donde decides tu arquitectura técnica:

* **Multithreading (Hilos):** Es como tener a todos los cocineros en la **misma habitación compartiendo la misma despensa (Shared Memory)**. Es ligero y rápido para comunicarse, pero requiere muchos cerrojos (Mutex) para no arruinar los datos.
* **Multiprocessing (Procesos):** Es como abrir **restaurantes separados**. Cada uno tiene su propia despensa (Memory Isolation). Si un restaurante se quema, el otro sigue funcionando. No hay GIL que los detenga, pero comunicarse entre ellos es más costoso (requiere **IPC - Inter-Process Communication** como Pipes o Sockets).

{{< figure src="https://miro.medium.com/1*F8ckVaR__PlBssnf-mn76A.png" title="Figura 5: Diferencia visual entre hilos (memoria compartida) y procesos (memoria aislada)." >}}

### Threading vs Multiprocessing

Para que no quede solo en teoría, así es como se ve en Python:

**Threading con Lock (Protegiendo la despensa):**
```python
import threading

sal_en_la_sopa = 0
lock = threading.Lock()

def añadir_sal():
    global sal_en_la_sopa
    for _ in range(100000):
        with lock: # El Mutex en acción
            sal_en_la_sopa += 1

hilos = [threading.Thread(target=añadir_sal) for _ in range(2)]
for h in hilos: h.start()
for h in hilos: h.join()

print(f"Sal total: {sal_en_la_sopa}") # Debería ser 200000
```

**Multiprocessing (Restaurantes independientes):**
```python
import multiprocessing
import os

def cocinar():
    print(f"Cocinando en el proceso {os.getpid()}")

if __name__ == "__main__":
    procesos = [multiprocessing.Process(target=cocinar) for _ in range(4)]
    for p in procesos: p.start()
    for p in procesos: p.join()
```


### Resumen Técnico

| Tarea | Técnica Recomendada | Referencia Técnica |
| :--- | :--- | :--- |
| **Cálculos matemáticos, IA, Video** | Multiprocessing | Aprovecha el paralelismo real (Multi-core). |
| **Consultas a API, Lectura de DB** | Multithreading / Async | Gestiona la concurrencia en tiempos de espera. |
| **Protección de datos** | Mutex / Semáforos | Evita Race Conditions en memoria compartida. |

Dominar estas técnicas es lo que separa a un programador que "hace que funcione" de un ingeniero que "hace que escale". La próxima vez que escribas un `import threading` o `import multiprocessing`, recuerda: estás diseñando el flujo de trabajo de tu propia cocina digital.