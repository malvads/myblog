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

{{< figure src="https://static.afteracademy.com/images/comparison-of-sorting-algorithms-compare1-18082c14f960abf3.png" title="Figure 3: Comparison of the number of operations across different sorting algorithms." >}}

Time Complexity defines the amount of time an algorithm requires to complete as a function of the input length $n$. It is essential to understand that in asymptotic analysis we do not measure seconds or microseconds, as those depend on the processor and architecture; instead, we quantify the number of elementary operations (such as assignments, comparisons, and jumps) that the algorithm performs.

When analyzing time, we focus on how this operation count scales as $n$ grows exponentially. A constant-time algorithm, $O(1)$, is the theoretical ideal, while an exponential-time algorithm, $O(2^n)$, becomes computationally intractable even for moderate values of $n$. Time analysis is critical for ensuring that an application is responsive and can process large volumes of data within acceptable timeframes for the user or the system.

## Algorithm Analysis with Examples

{{< figure src="https://carolinacheuquiante.files.wordpress.com/2012/06/imagen1.png?w=300&h=201" title="Figure 4: Example of a comparative analysis of sorting algorithms." >}}

Algorithm Analysis is the practical application of asymptotic notation to evaluate and predict the performance of a block of code. This methodical process consists of abstracting the source code into elementary operations (assignments, comparisons, arithmetic operations) and identifying how these scale as a function of the data input ($n$).

By performing this analysis, software engineers can make informed architectural decisions, balancing CPU time consumption against RAM memory usage. Below are classic examples that illustrate how temporal and spatial complexities are determined across different scenarios.

The following examples are simple — you should know that there are many more algorithms and data structures for solving problems with code.

### Linear Search

{{< figure src="https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif" title="Figure 5: Comparison between Linear Search and Binary Search." >}}

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

{{< figure src="https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif" title="Figure 7: Step-by-step depiction of Binary Search. Source: Wikimedia Commons." >}}

#### Time Complexity
Unlike linear search, binary search divides the search space in half with each iteration (requiring the list to be previously sorted). This successive division causes the operations to grow logarithmically relative to the input. Its complexity is very efficient: $O(\log n)$.

#### Space Complexity
If implemented iteratively, only pointers for the start, end, and midpoint are needed, so its complexity is $O(1)$.

### Merge Sort

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg" title="Figure 8: Diagram of the Merge Sort algorithm. Source: Wikimedia Commons." >}}

#### Time Complexity
Merge Sort uses the "Divide and Conquer" paradigm. It repeatedly divides the list into halves (which takes logarithmic time $\log n$) and then merges those halves by sorting them (which takes linear time $n$). The combination of both steps gives us a time complexity of $O(n \log n)$, being much more efficient than Bubble Sort for large volumes of data.

#### Space Complexity
Unlike Bubble Sort, Merge Sort does not sort *in-place*. It needs to create temporary auxiliary arrays to store the halves before merging them. In the worst case, it will require as much extra memory as the length of the original list, resulting in a space complexity of $O(n)$.

## Advanced Data Structures and Algorithms

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Hash_table_average_insertion_time.png" title="Figure 9: Average insertion time in a Hash Table. Source: Wikimedia Commons." >}}

Not all problems are solved by iterating over lists. In real-world software engineering, we face scenarios where we need to access data almost instantly, maintain ordered collections efficiently, or model complex relationships between entities. For each of these cases, there are specialized data structures that we must know.

**Hash Tables** (known as dictionaries in Python or HashMaps in Java) allow us to associate keys with values and access them in practically constant time, $O(1)$. They are the reason why a search in an indexed database is almost instantaneous, regardless of whether it has a hundred records or a hundred million.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg" title="Figure 10: Example of a Binary Search Tree (BST). Source: Wikimedia Commons." >}}

**Trees** are hierarchical structures that keep data organized so that search, insertion, and deletion operations are performed in $O(\log n)$. Variants like AVL or Red-Black trees self-balance to guarantee that performance even in the worst-case scenarios. They are the foundation of database indexes and your operating system's file system.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Directed.svg" title="Figure 11: Example of a Directed Graph. Source: Wikimedia Commons." >}}

**Graphs** allow modeling relationships between entities — something that lists and trees cannot easily represent. Every time you use GPS to find the shortest route, browse recommendations on a social network, or your package travels through the network to reach you, there is a graph algorithm (like Dijkstra, BFS, or DFS) working behind the scenes.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/QUEUE_VS_STACK.svg/3840px-QUEUE_VS_STACK.svg.png" title="Figure 12: Comparison between a Queue (FIFO) and a Stack (LIFO). Source: Wikimedia Commons." >}}

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
