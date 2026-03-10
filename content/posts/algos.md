+++
title = 'Asymptotic Notation and Algorithmic Complexity'
description = 'A practical guide to Big O, Big Omega, and Big Theta notation, time and space complexity analysis, and essential data structures every engineer should know.'
tags = ['Algorithms', 'Big O', 'Data Structures', 'CS Fundamentals']
date = '2026-03-10T10:20:00.000Z'
draft = false
categories = ['Engineering']
series = []
author = 'Miguel Alvarez'
keywords = ['Big O', 'Asymptotic Notation', 'Algorithmic Complexity', 'Data Structures', 'Time Complexity', 'Space Complexity']

[cover]
image = ""
relative = true
+++

In the world of software, it's not enough to just write code — we need to write efficient and scalable code. To do that, we must understand algorithmic complexity and asymptotic notation.

These are tools that allow us to analyze the performance of our algorithms and compare them against each other. They let us know whether our algorithm will be able to handle large amounts of data and whether it will scale as the data volume increases.

## Asymptotic Notation

Asymptotic notation is a mathematical language used in computer science to describe the efficiency and behavior of an algorithm as the input size ($n$) tends toward infinity. It focuses on the growth rate of time or space, stripping away constants and lower-order terms.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg" title="Figure 1: Comparison of common computational complexities. Source: Wikimedia Commons." >}}

## Algorithmic Complexity: Big O, Big Omega, and Big Theta

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/8/89/BigOnotationfunctionapprox.svg" title="Figure 2: Graphical representation of Big O. The function f(x) is upper-bounded by g(x). Source: Wikimedia Commons." >}}

### Big O

It is used to describe the worst-case scenario. It is a guarantee that the algorithm will not take longer than a certain amount.

It is the most widely used in the industry. If you say an algorithm is $O(n^2)$, you are guaranteeing that, in the worst case, its growth will be quadratic.

We say that $f(n) = O(g(n))$ if the growth of the time function does not exceed $g(n)$ multiplied by a constant, beyond a certain threshold. It is a safety guarantee that the algorithm will never be slower than this limit, allowing engineers to set performance ceilings and ensure the system won't collapse under a massive increase in data.

### Big Omega

In contrast, the analysis requires defining the Lower Bound or Big Omega ($\Omega$), which establishes the minimum guaranteed performance. Mathematically, $f(n) = \Omega(g(n))$ indicates that the algorithm will always execute at least a number of steps proportional to $g(n)$ in the best case. This metric is crucial for proving the intrinsic complexity of a problem, confirming that no more efficient solution exists than the lower bound established by the nature of the computation itself.

### Big Theta

It is the most precise of the three. It is used when the upper and lower bounds coincide, defining the exact behavior.

This occurs only when the upper and lower bounds match asymptotically. When declaring that an algorithm is $\Theta(g(n))$, one is asserting that its behavior is strictly trapped between two constants of the same reference function. This notation represents the "exact order" of growth, providing a complete and bidirectional technical description that eliminates any ambiguity about how the function scales as $n$ grows without bound.

## Space Complexity
Space Complexity refers to the total amount of working memory (RAM) that an algorithm needs to run to completion, also expressed as a function of the input size $n$. This analysis is technically divided into two essential components: the input space (the size of the initial data) and the auxiliary space, which is the additional memory (temporary variables, recursion stacks, intermediate data structures) that the algorithm creates to operate.

In modern software engineering, we often face the trade-off between space and time — we can speed up an algorithm by using more memory (for example, through lookup tables or memoization), or reduce memory consumption at the cost of longer processing time. An efficient design seeks the optimal balance, ensuring that the algorithm does not exhaust the system's available memory (Stack Overflow or Out of Memory), especially in resource-constrained environments like mobile devices or embedded systems.

## Time Complexity

{{< figure src="https://static.afteracademy.com/images/comparison-of-sorting-algorithms-compare1-18082c14f960abf3.png" title="Figure 4: Comparison of the number of operations across different sorting algorithms." >}}

Time Complexity defines the amount of time an algorithm requires to complete as a function of the input length $n$. It is essential to understand that in asymptotic analysis we do not measure seconds or microseconds, as those depend on the processor and architecture; instead, we quantify the number of elementary operations (such as assignments, comparisons, and jumps) that the algorithm performs.

When analyzing time, we focus on how this operation count scales as $n$ grows exponentially. A constant-time algorithm, $O(1)$, is the theoretical ideal, while an exponential-time algorithm, $O(2^n)$, becomes computationally intractable even for moderate values of $n$. Time analysis is critical for ensuring that an application is responsive and can process large volumes of data within acceptable timeframes for the user or the system.

## Algorithm Analysis with Examples

{{< figure src="https://carolinacheuquiante.files.wordpress.com/2012/06/imagen1.png?w=300&h=201" title="Example of a comparative analysis of sorting algorithms." >}}

Algorithm Analysis is the practical application of asymptotic notation to evaluate and predict the performance of a block of code. This methodical process consists of abstracting the source code into elementary operations (assignments, comparisons, arithmetic operations) and identifying how these scale as a function of the data input ($n$).

By performing this analysis, software engineers can make informed architectural decisions, balancing CPU time consumption against RAM memory usage. Below are classic examples that illustrate how temporal and spatial complexities are determined across different scenarios.

The following examples are simple — you should know that there are many more algorithms and data structures for solving problems with code.

### Linear Search

{{< figure src="https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif" title="Comparison between Linear Search and Binary Search." >}}

#### Time Complexity
In the worst case (the target is at the end or doesn't exist), the loop will iterate exactly $n$ times, where $n$ is the size of the list. Therefore, the execution time is strictly proportional to the input, resulting in $O(n)$.

#### Space Complexity
Regardless of whether the list has ten or a million elements, the algorithm only allocates the iterator variable in memory. Since it requires no additional data structures that grow with the input, its space complexity remains constant at $O(1)$.

### Bubble Sort

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" title="Visualization of the Bubble Sort algorithm. Source: Wikimedia Commons." >}}

#### Time Complexity
This algorithm compares adjacent elements and swaps them if they are in the wrong order. Having two nested loops that depend on the length of the list ($n$), in the worst case (when the list is in reverse order), it will perform a number of operations proportional to $n \times n$. Therefore, its time complexity is quadratic: $O(n^2)$.

#### Space Complexity
The sorting is done *in-place* (on the original list itself), requiring only extra space for the temporary variable swap. Therefore, its space complexity is $O(1)$.

### Binary Search

{{< figure src="data:image/png;base64,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" title="Step-by-step depiction of Binary Search." >}}

#### Time Complexity
Unlike linear search, binary search divides the search space in half with each iteration (requiring the list to be previously sorted). This successive division causes the operations to grow logarithmically relative to the input. Its complexity is very efficient: $O(\log n)$.

#### Space Complexity
If implemented iteratively, only pointers for the start, end, and midpoint are needed, so its complexity is $O(1)$.

### Merge Sort

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg" title="Diagram of the Merge Sort algorithm. Source: Wikimedia Commons." >}}

#### Time Complexity
Merge Sort uses the "Divide and Conquer" paradigm. It repeatedly divides the list into halves (which takes logarithmic time $\log n$) and then merges those halves by sorting them (which takes linear time $n$). The combination of both steps gives us a time complexity of $O(n \log n)$, being much more efficient than Bubble Sort for large volumes of data.

#### Space Complexity
Unlike Bubble Sort, Merge Sort does not sort *in-place*. It needs to create temporary auxiliary arrays to store the halves before merging them. In the worst case, it will require as much extra memory as the length of the original list, resulting in a space complexity of $O(n)$.

## Advanced Data Structures and Algorithms

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Hash_table_average_insertion_time.png" title="Average insertion time in a Hash Table." >}}

Not all problems are solved by iterating over lists. In real-world software engineering, we face scenarios where we need to access data almost instantly, maintain ordered collections efficiently, or model complex relationships between entities. For each of these cases, there are specialized data structures that we must know.

**Hash Tables** (known as dictionaries in Python or HashMaps in Java) allow us to associate keys with values and access them in practically constant time, $O(1)$. They are the reason why a search in an indexed database is almost instantaneous, regardless of whether it has a hundred records or a hundred million.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg" title="Example of a Binary Search Tree (BST)." >}}

**Trees** are hierarchical structures that keep data organized so that search, insertion, and deletion operations are performed in $O(\log n)$. Variants like AVL or Red-Black trees self-balance to guarantee that performance even in the worst-case scenarios. They are the foundation of database indexes and your operating system's file system.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Directed.svg" title="Example of a Directed Graph." >}}

**Graphs** allow modeling relationships between entities — something that lists and trees cannot easily represent. Every time you use GPS to find the shortest route, browse recommendations on a social network, or your package travels through the network to reach you, there is a graph algorithm (like Dijkstra, BFS, or DFS) working behind the scenes.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/QUEUE_VS_STACK.svg/3840px-QUEUE_VS_STACK.svg.png" title="Comparison between a Queue (FIFO) and a Stack (LIFO)." >}}

**Queues** and **Stacks** are simpler structures, but fundamental ones. A queue (FIFO) guarantees that elements are processed in the order they arrive, like tasks in a print queue or messages in an event system. A stack (LIFO) works the other way around: the last one in is the first one out, like the "undo" history in any editor or the call stack that manages the execution of your own code.

Each of these structures has its own temporal and spatial complexities that directly affect the performance of our applications. In an upcoming post, we will dive deeper into each of them with implementations and detailed analyses.

### Examples

#### Linear Search
```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
```

Time Complexity: Best case: $O(1)$ (The target is in the first position).

Worst case / Average case: $O(n)$ (The target is at the end of the list or doesn't exist, requiring traversal of all elements).

Space Complexity: $O(1)$. Only one extra variable is used for the index i, regardless of the list size.

#### Bubble Sort
```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
```

Time Complexity: Best case: $O(n)$ (The list is already sorted, only one pass is made).

Worst case / Average case: $O(n^2)$ (The list is in reverse order, requiring comparisons and swaps in every iteration of both nested loops).

Space Complexity: $O(1)$. The sorting is done *in-place*, only temporary variables are used for the swap.

#### Binary Search
```python
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
```

Time Complexity: Best case: $O(1)$ (The target is exactly at the midpoint).

Worst case / Average case: $O(\log n)$ (The search space is halved with each iteration).

Space Complexity: $O(1)$. Only three auxiliary variables (start, end, mid) are used, regardless of the list size.

#### Merge Sort
```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

Time Complexity: Best case / Worst case / Average case: $O(n \log n)$ (It always divides the list into halves and merges them, regardless of the initial order of the data).

Space Complexity: $O(n)$. Auxiliary arrays are created to store the halves during merging, requiring memory proportional to the input size.
