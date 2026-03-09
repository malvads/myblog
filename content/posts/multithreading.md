+++
title = 'Understanding Multithreading and Multiprocessing Once and for All'
description = 'Threads or Processes? Understand how to scale your software.'
tags = ['Concurrency', 'Programming', 'Operating Systems']
date = '2026-03-09T00:00:00.000Z'
draft = false
categories = ['Software Development']
series = []
author = 'Miguel Alvarez'
keywords = ['Multithreading', 'Multiprocessing', 'GIL', 'Race Condition', 'Context Switch']

[cover]
image = ""
relative = true
+++

Programming is often compared to following a recipe. But when we want our software to be professional, it's not enough for the recipe to work, we need the restaurant to be able to serve a hundred people at once without burning the kitchen down. Today we are going to explore the world of **concurrency** and **parallelism**. If you've ever wondered why your program is slow despite having a top-of-the-line processor, the answer lies in how you manage your **threads and processes**.

### Hardware Threads vs. Software Threads

Imagine that **Hardware Threads** are the **physical cooks** you have in the kitchen, that is, the logical cores of your CPU. It is important to distinguish between a physical core, the actual computing unit, and a logical thread. Technologies like SMT or Hyperthreading allow one core to look like two to the system, so if your processor has 8 threads, you have 8 pairs of hands working.

On the other hand, **Software Threads** are the **tasks written on tickets or comandas**. In most modern systems these are Kernel threads or mapped to them. A single cook or hardware thread can be in charge of several tickets or software threads. The **Scheduler** performed by the operating system makes a **Context Switch**, which means that the cook stops chopping onions for a second to stir the soup and then goes back to the onions. To the customer it looks like they are doing both things at once, but in reality they are rapidly alternating between them.

{{< figure src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter4/4_01_ThreadDiagram.jpg" title="Figure 1: Diagram of threads and processes in the operating system." >}}

### The GIL and the GVL

In languages like **Python (CPython)** or **Ruby (MRI)** there is a very strict character called the **GIL or Global Interpreter Lock**, also known as **GVL or Global VM Lock** in Ruby. Imagine that even if you have 10 cooks, there is only one official ladle. For a cook to execute any instruction from the bytecode they must have the ladle. This ensures that no one corrupts the interpreter's memory management, but it prevents true parallelism for heavy CPU tasks within the same process. It is worth noting that implementations like **JRuby** or **Jython** do not have this limitation, and C extensions can release the GIL to execute work in parallel.

In **CPU-Bound** tasks or heavy calculations, such as chopping 50kg of meat, the GIL prevents multiple threads from executing Python code at once, making multithreading less useful here and leaving **Multiprocessing** as the solution. In contrast, in **I/O-Bound** tasks or network and disk waiting, such as waiting for the oven to beep, the cook releases the ladle while waiting to allow someone else to proceed. Here, **Multithreading** or **Async I/O** are extremely efficient.

{{< figure src="https://static-assets.codecademy.com/understanding-gil-in-python/GIL-behaviour.png" title="Figure 2: Operation of the Global Interpreter Lock (GIL)." >}}

### Race Condition

Imagine a shared variable called `salt_in_the_soup = 0`. If two cooks want to add a pinch of salt, the first one reads that there is 0 salt, the second one also reads that there is 0, the first one adds 1 and writes that there is 1, and the second one does the same. The result is that there is 1 salt when there should be 2. This is a **Race Condition** and the final result depends on who arrived last to write to memory.

{{< figure src="https://media.geeksforgeeks.org/wp-content/uploads/20201228232441/gfgdiagram.png" title="Figure 3: Race condition when accessing shared memory." >}}

### Mutex and Synchronization

To prevent two cooks from putting their hands in the same pot we use a **Mutex or Mutual Exclusion**, which is a lock on the door of the critical section of the code. If a thread enters it locks the door, and others must wait in line or be blocked until the key is free. However, if we are not careful we can fall into a **Deadlock**. This occurs when cook A has the key to the oven and is waiting for the knife, while cook B has the key to the knife and is waiting for the oven. Neither moves and the program freezes. To avoid this, best practices include always ordering lock acquisition, using timeouts to avoid waiting forever or simply avoiding nested locks whenever possible.

{{< figure src="https://miro.medium.com/v2/resize:fit:1200/1*nT6M9U44up3hYJoQjohC3A.png" title="Figure 4: The problem of mutual blocking (Deadlock)." >}}

### Semaphores: The Capacity Controller

If a Mutex is a key for a single office, a **Semaphore** is a security gate that allows a limited number of threads to pass, for example 3 threads at a time. It is the perfect tool when you have a shared resource that can handle multiple connections but not infinite ones, as is the case with a database connection pool.

{{< figure src="https://cdn.codegym.cc/images/article/edf6d093-dd70-41a0-8e8d-b987e687c089/800.webp" title="Figure 5: The semaphore allowing controlled access to multiple threads." >}}

### Atomic Operations: The Art of Not Blinking

Sometimes locking an entire section of code with a Mutex is like using a sledgehammer to crack a nut. An **Atomic Operation** is a low-level instruction that the CPU guarantees will execute indivisibly. To the rest of the system the operation happens instantaneously or not at all, with no intermediate states. It is the purest and fastest way to avoid Race Conditions in counters or flags as there are no context switches or heavy waiting. In **C (C11)** this becomes extremely powerful.

```c
#include <stdatomic.h>

atomic_int dishes_served = 0;

void serve_dish() {
    // Indivisible at the hardware level. 
    // Maximum speed without the need for locks.
    // (Note: C11 allows specifying 'memory_order' for even finer control).
    atomic_fetch_add(&dishes_served, 1);
}
```

### Shared Kitchen or Independent Restaurants?

This is where you decide your technical architecture. **Multithreading** is like having all the cooks in the same room sharing the same pantry or shared memory, which is lightweight and fast to communicate but requires many locks to avoid ruining the data. **Multiprocessing** is like opening separate restaurants where each has its own pantry or memory isolation. If one restaurant burns down the other keeps running, there is no GIL to stop them but communicating between them is more expensive by requiring inter-process communication mechanisms such as pipes or sockets.

{{< figure src="https://miro.medium.com/1*F8ckVaR__PlBssnf-mn76A.png" title="Figure 6: Visual difference between threads (shared memory) and processes (isolated memory)." >}}

### Threading vs Multiprocessing in Python

To move beyond theory, threading tasks with a lock to protect the pantry would look like this in Python.

```python
import threading

salt_in_the_soup = 0
lock = threading.Lock()

def add_salt():
    global salt_in_the_soup
    for _ in range(100000):
        with lock: # The Mutex in action
            salt_in_the_soup += 1

threads = [threading.Thread(target=add_salt) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(f"Total salt {salt_in_the_soup}") # Should be 200000
```

On the other hand, separate restaurant processes would be implemented in the following way.

```python
import multiprocessing
import os

def cook():
    print(f"Cooking in process {os.getpid()}")

if __name__ == "__main__":
    processes = [multiprocessing.Process(target=cook) for _ in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()
```

### Technical Conclusion

For mathematical calculations, artificial intelligence or video processing, **Multiprocessing** is recommended because it leverages the true parallelism of several cores. For API queries or database reading it is better to use **Multithreading or Async** to manage concurrency during wait times. Finally, for data protection, **Mutex or Semaphores** should be used to avoid race conditions in shared memory.

Mastering these techniques is what separates a programmer who makes it work from an engineer who makes it scale. The next time you write an `import threading` or `import multiprocessing`, remember that you are designing the workflow for your own digital kitchen.
