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

Programming is often compared to following a recipe. But when we want our software to be professional, it's not enough for the recipe to work; we need the restaurant to be able to serve a hundred people at once without burning the kitchen down.

Today we are going to explore the world of **concurrency** and **parallelism**. If you've ever wondered why your program is slow despite having a top-of-the-line processor, the answer lies in how you manage your **threads and processes**.

### Hardware Threads vs. Software Threads

Imagine that **Hardware Threads** are the **physical cooks** you have in the kitchen (the logical cores of your CPU). If your processor has 8 threads, you have 8 pairs of hands working.

On the other hand, **Software Threads** are the **tasks written on tickets (comandas)**. A single cook (hardware thread) can be in charge of several tickets (software threads). The operating system performs a **Context Switch**: the cook stops chopping onions for a second to stir the soup, and then goes back to the onions. To the customer, it looks like they are doing both things at once, but in reality, they are rapidly alternating between them (magical, right?).

{{< figure src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter4/4_01_ThreadDiagram.jpg" title="Figure 1: Diagram of threads and processes in the operating system." >}}

### The GIL and the GVL

In languages like **Python (CPython)** or **Ruby (MRI)**, there is a very strict character: the **GIL (Global Interpreter Lock)**.

Imagine that, even if you have 10 cooks, there is only one **official ladle**. For a cook to execute any instruction from the code, they must have the ladle. This ensures that no one corrupts the "recipe" (the interpreter's memory management), but it prevents **true parallelism** in heavy tasks.

* **CPU-Bound (Heavy calculations):** Like chopping 50kg of meat. The GIL causes the cooks to fight over the ladle, making multithreading useless. This is where **Multiprocessing** shines.
* **I/O-Bound (Waiting for network/disk):** Like waiting for the oven to beep. The cook releases the ladle while waiting, allowing someone else to proceed. Here, **Multithreading** or **Async I/O** are extremely efficient.

{{< figure src="https://static-assets.codecademy.com/understanding-gil-in-python/GIL-behaviour.png" title="Figure 2: Operation of the Global Interpreter Lock (GIL)." >}}

### Race Condition

Imagine a shared variable called `salt_in_the_soup = 0`.
Two threads (cooks) want to add a pinch of salt:
1. **Thread A** reads that there is 0 salt.
2. **Thread B** reads that there is 0 salt.
3. **Thread A** adds 1 and writes: "There is 1 salt".
4. **Thread B** adds 1 and writes: "There is 1 salt".

Error! There should be 2 salt, but the result is 1. This is a **Race Condition**. The final result depends on who arrived last to write to memory.

{{< figure src="https://media.geeksforgeeks.org/wp-content/uploads/20201228232441/gfgdiagram.png" title="Figure 3: Race condition when accessing shared memory." >}}

### Mutex and Synchronization

To prevent two cooks from putting their hands in the same pot, we use a **Mutex (Mutual Exclusion)**. It's a lock on the door of the critical section of the code. If a thread enters, it locks the door; others must wait in line (**Block**) until the key is free.

However, if we are not careful, we can fall into a **Deadlock**:
* Cook A has the key to the *Oven* and is waiting for the *Knife*.
* Cook B has the key to the *Knife* and is waiting for the *Oven*.
No one moves. The program freezes.

{{< figure src="https://miro.medium.com/v2/resize:fit:1200/1*nT6M9U44up3hYJoQjohC3A.png" title="Figure 4: The problem of mutual blocking (Deadlock)." >}}

### Shared Kitchen or Independent Restaurants?

This is where you decide your technical architecture:

* **Multithreading (Threads):** It's like having all the cooks in the **same room sharing the same pantry (Shared Memory)**. It's lightweight and fast to communicate, but requires many locks (Mutex) to avoid ruining the data.
* **Multiprocessing (Processes):** It's like opening **separate restaurants**. Each has its own pantry (Memory Isolation). If one restaurant burns down, the other keeps running. There is no GIL to stop them, but communicating between them is more expensive (requires **IPC - Inter-Process Communication** like Pipes or Sockets).

{{< figure src="https://miro.medium.com/1*F8ckVaR__PlBssnf-mn76A.png" title="Figure 5: Visual difference between threads (shared memory) and processes (isolated memory)." >}}

### Threading vs Multiprocessing

To move beyond theory, here is how it looks in Python:

**Threading with Lock (Protecting the pantry):**
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

print(f"Total salt: {salt_in_the_soup}") # Should be 200000
```

**Multiprocessing (Independent restaurants):**
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

### Technical Summary

| Task | Recommended Technique | Technical Reference |
| :--- | :--- | :--- |
| **Math calculations, AI, Video** | Multiprocessing | Leverages true parallelism (Multi-core). |
| **API calls, DB reads** | Multithreading / Async | Manages concurrency during wait times. |
| **Data protection** | Mutex / Semaphores | Prevents Race Conditions in shared memory. |

Mastering these techniques is what separates a programmer who "makes it work" from an engineer who "makes it scale". The next time you write an `import threading` or `import multiprocessing`, remember: you are designing the workflow for your own digital kitchen.
