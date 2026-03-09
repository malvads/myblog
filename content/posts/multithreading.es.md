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

Programar suele compararse con seguir una receta. Pero cuando queremos que nuestro software sea profesional, no basta con que la receta funcione, necesitamos que el restaurante sea capaz de servir a cien personas a la vez sin quemar la cocina. Hoy vamos a explorar el mundo de la **concurrencia** y el **paralelismo**. Si alguna vez te has preguntado por qué tu programa va lento a pesar de tener un procesador de última generación, la respuesta está en cómo gestionas tus **hilos y procesos**.

### Hardware Threads vs. Software Threads

Imagina que los **Hardware Threads** son los **cocineros físicos** que tienes en la cocina, es decir, los núcleos lógicos de tu CPU. Es importante distinguir entre un núcleo físico, la unidad real de cómputo, y un hilo lógico. Tecnologías como SMT o Hyperthreading permiten que un núcleo parezca dos para el sistema, así que si tu procesador tiene 8 hilos, tienes 8 pares de manos trabajando.

Por otro lado, los **Software Threads** son las **tareas anotadas en comandas**. En la mayoría de los sistemas modernos, estos son hilos del Kernel o mapeados a ellos. Un solo cocinero o hardware thread puede estar a cargo de varias comandas o software threads. El **Planificador o Scheduler** del sistema operativo hace un **Context Switch** o cambio de contexto, lo que significa que el cocinero deja de picar cebolla un segundo para remover la sopa y luego vuelve a la cebolla. A ojos del cliente parece que está haciendo ambas cosas a la vez, pero en realidad está alternando rápidamente.

{{< figure src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter4/4_01_ThreadDiagram.jpg" title="Figura 1: Diagrama de hilos y procesos en el sistema operativo." >}}

### El GIL y el GVL

En lenguajes como **Python (CPython)** o **Ruby (MRI)** existe un personaje muy estricto llamado el **GIL o Global Interpreter Lock**, también conocido como **GVL o Global VM Lock** en Ruby. Imagina que, aunque tengas 10 cocineros, solo hay un cucharón oficial. Para que un cocinero ejecute cualquier instrucción del bytecode debe tener el cucharón. Esto garantiza que nadie corrompa la gestión de memoria del intérprete, pero impide el paralelismo real en tareas pesadas de CPU dentro del mismo proceso. Es importante notar que implementaciones como **JRuby** o **Jython** no tienen esta limitación, y que las extensiones en C pueden liberar el GIL para ejecutar trabajo en paralelo.

En las tareas de tipo **CPU-Bound** o de cálculos pesados, como picar 50kg de carne, el GIL impide que varios hilos ejecuten código Python a la vez, haciendo que el multithreading sea poco útil aquí y dejando como solución el **Multiprocessing**. En cambio, en las tareas de **I/O-Bound** o de espera de red y disco, como esperar a que el horno suene, el cocinero suelta el cucharón mientras espera para permitir que otro avance. Aquí el **Multithreading** o el **Async I/O** son extremadamente eficientes.

{{< figure src="https://static-assets.codecademy.com/understanding-gil-in-python/GIL-behaviour.png" title="Figura 2: Funcionamiento del Global Interpreter Lock (GIL)." >}}

### Condición de Carrera (Race Condition)

Imagina una variable compartida llamada `sal_en_la_sopa = 0`. Si dos cocineros quieren añadir una pizca de sal, el primero lee que hay 0 de sal, el segundo también lee que hay 0, el primero suma 1 y escribe que hay 1, y el segundo hace lo mismo. El resultado es que hay 1 de sal cuando debería haber 2. Esto es una **Race Condition** y el resultado final depende de quién llegó último a escribir en la memoria.

{{< figure src="https://media.geeksforgeeks.org/wp-content/uploads/20201228232441/gfgdiagram.png" title="Figura 3: Condición de carrera al acceder a memoria compartida." >}}

### Mutex y Sincronización

Para evitar que dos cocineros metan la mano en la misma olla usamos un **Mutex o Mutual Exclusion**, que es un cerrojo en la puerta de la sección crítica del código. Si un hilo entra echa la llave, y los demás deben esperar en la cola o quedar bloqueados hasta que la llave quede libre. Sin embargo, si no tenemos cuidado podemos caer en un **Deadlock** o bloqueo mutuo. Esto ocurre cuando el cocinero A tiene la llave del horno y espera la del cuchillo, mientras que el cocinero B tiene la llave del cuchillo y espera la del horno. Ninguno se mueve y el programa se congela. Para evitar esto, las buenas prácticas dictan ordenar siempre la adquisición de locks, usar timeouts para no esperar eternamente o simplemente evitar los cerrojos anidados siempre que sea posible.

{{< figure src="https://miro.medium.com/v2/resize:fit:1200/1*nT6M9U44up3hYJoQjohC3A.png" title="Figura 4: El problema del bloqueo mutuo (Deadlock)." >}}

### Semáforos: El controlador de aforo

Si un Mutex es una llave para una sola oficina, un **Semáforo** es una garita de seguridad que permite el paso a un número limitado de hilos, por ejemplo 3 hilos a la vez. Es la herramienta perfecta cuando tienes un recurso compartido que puede manejar varias conexiones pero no infinitas, como ocurre con un pool de conexiones a una base de datos.

{{< figure src="https://cdn.codegym.cc/images/article/edf6d093-dd70-41a0-8e8d-b987e687c089/800.webp" title="Figura 5: El semáforo permitiendo el acceso controlado a múltiples hilos." >}}

### Operaciones Atómicas: El arte de no parpadear

A veces bloquear todo un tramo de código con un Mutex es como matar moscas a cañonazos. Una **Operación Atómica** es una instrucción de tan bajo nivel que la CPU garantiza que se ejecute de forma indivisible. Para el resto del sistema la operación sucede instantáneamente o no sucede en absoluto, sin estados intermedios. Es la forma más pura y rápida de evitar Race Conditions en contadores o banderas ya que no hay cambios de contexto ni esperas pesadas. En **C (C11)** esto se vuelve extremadamente potente.

```c
#include <stdatomic.h>

atomic_int platos_servidos = 0;

void servir_plato() {
    // Indivisible a nivel de hardware. 
    // Máxima velocidad sin necesidad de cerrojos (locks).
    // (Nota: C11 permite especificar 'memory_order' para un control aún más fino).
    atomic_fetch_add(&platos_servidos, 1);
}
```

### ¿Cocina compartida o Restaurantes independientes?

Aquí es donde decides tu arquitectura técnica. El **Multithreading o Hilos** es como tener a todos los cocineros en la misma habitación compartiendo la misma despensa o memoria compartida, lo cual es ligero y rápido para comunicarse pero requiere muchos cerrojos para no arruinar los datos. El **Multiprocessing o Procesos** es como abrir restaurantes separados donde cada uno tiene su propia despensa o aislamiento de memoria. Si un restaurante se quema el otro sigue funcionando, no hay GIL que los detenga pero comunicarse entre ellos es más costoso al requerir mecanismos de comunicación entre procesos como tuberías o sockets.

{{< figure src="https://miro.medium.com/1*F8ckVaR__PlBssnf-mn76A.png" title="Figura 6: Diferencia visual entre hilos (memoria compartida) y procesos (memoria aislada)." >}}

### Threading vs Multiprocessing en Python

Para que no quede solo en teoría, las tareas de hilos con bloqueo para proteger la despensa se verían así en Python.

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

print(f"Sal total {sal_en_la_sopa}") # Debería ser 200000
```

Por otro lado, los procesos para restaurantes independientes se implementarían de la siguiente forma.

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

### Conclusión técnica

Para los cálculos matemáticos, inteligencia artificial o procesamiento de vídeo se recomienda el **Multiprocessing** porque aprovecha el paralelismo real de varios núcleos. Para las consultas a API o lectura de bases de datos es mejor usar **Multithreading o Async** para gestionar la concurrencia en los tiempos de espera. Finalmente, para la protección de datos se deben usar **Mutex o Semáforos** con el fin de evitar condiciones de carrera en la memoria compartida.

Dominar estas técnicas es lo que separa a un programador que hace que funcione de un ingeniero que hace que escale. La próxima vez que escribas un `import threading` o `import multiprocessing`, recuerda que estás diseñando el flujo de trabajo de tu propia cocina digital.