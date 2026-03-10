+++
title = 'Notación Asintotica y Big O, Complejidad Algoritmica'
description = ''
tags = []
date = '2026-03-10T10:20:00.000Z'
draft = false
categories = []
series = []
author = 'Miguel Alvarez'
keywords = []

[cover]
image = ""
relative = true
+++

En el mundo del software no basta con solo escribir codigo, tenemos que escribir codigo eficiente y escalable. Para ello, debemos entender la complejidad algoritmica y la notación asintótica.

Estas son herramientas que nos permiten analizar el rendimiento de nuestros algoritmos y compararlos entre sí. Nos permiten saber si nuestro algoritmo será capaz de manejar grandes cantidades de datos y si será capaz de escalar a medida que aumenta la cantidad de datos.

## Notación Asintótica

La notación asintótica es un lenguaje matemático usado en computación para describir la eficiencia y el comportamiento de un algoritmo a medida que el tamaño de entrada ($n$) tiende al infinito. Se centra en la tasa de crecimiento del tiempo o espacio, eliminando constantes y términos de menor orden.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg" title="Figura 1: Comparación de complejidades computacionales comunes. Fuente: Wikimedia Commons." >}}

## Big O, Big Omega y Big Theta

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/8/89/BigOnotationfunctionapprox.svg" title="Figura 2: Representación gráfica de Big O. La función f(x) está acotada superiormente por g(x). Fuente: Wikimedia Commons." >}}

### Big O

Se utiliza para describir el peor escenario posible. Es una garantía de que el algoritmo no tardará más que una cantidad determinada.

Es la más usada en la industria. Si dices que un algoritmo es $O(n^2)$, aseguras que, en el peor de los casos, su crecimiento será cuadrático.

Decimos que $f(n) = O(g(n))$ si el crecimiento de la función de tiempo no supera a $g(n)$ multiplicada por una constante, a partir de un umbral determinado. Es una garantía de seguridad de que el algoritmo nunca será más lento que este límite, lo que permite a los ingenieros establecer techos de rendimiento y asegurar que el sistema no colapsará ante el incremento masivo de datos.

### Big Omega

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Big-Ω-notation.png" title="Cota inferior: f(x) = Ω(g(x)). Fuente: Wikimedia Commons." >}}

En contraposición, el análisis requiere definir la Cota Inferior o Big Omega ($\Omega$), que establece el rendimiento mínimo garantizado. Matemáticamente, $f(n) = \Omega(g(n))$ indica que el algoritmo siempre ejecutará, al menos, una cantidad de pasos proporcional a $g(n)$ en el mejor de los casos. Esta métrica es crucial para demostrar la complejidad intrínseca de un problema, confirmando que no existe una solución más eficiente que el límite inferior establecido por la naturaleza del propio cálculo.

### Big Theta

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Big-θ-notation.png" title="Cota ajustada: f(x) = Θ(g(x)). Fuente: Wikimedia Commons." >}}

Es la más precisa de las tres. Se usa cuando el límite superior y el inferior coinciden, definiendo el comportamiento exacto.

La cual ocurre únicamente cuando los límites superior e inferior coinciden asintóticamente. Al declarar que un algoritmo es $\Theta(g(n))$, se está afirmando que su comportamiento está estrictamente atrapado entre dos constantes de la misma función de referencia. Esta notación representa el "orden exacto" de crecimiento, proporcionando una descripción técnica completa y bidireccional que elimina cualquier ambigüedad sobre cómo escala la función a medida que $n$ crece sin límite.

## Complejidad Espacial 

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/0/0c/ComputerMemoryHierarchy.svg" title="Figura 3: Jerarquía de memoria en un sistema computacional. Fuente: Wikimedia Commons." >}}

La Complejidad Espacial se refiere a la cantidad total de memoria de trabajo (RAM) que un algoritmo necesita para ejecutarse hasta su finalización, expresada también como una función del tamaño de la entrada $n$. Este análisis se divide técnicamente en dos componentes esenciales, el espacio de la entrada (el tamaño de los datos iniciales) y el espacio auxiliar, que es la memoria adicional (variables temporales, pilas de recursión, estructuras de datos intermedias) que el algoritmo crea para operar.

En la ingeniería de software moderna, a menudo nos enfrentamos al trade-off (intercambio) entre espacio y tiempo, podemos acelerar un algoritmo utilizando más memoria (por ejemplo, mediante tablas de búsqueda o memoization), o reducir el consumo de memoria a costa de un mayor tiempo de procesamiento. Un diseño eficiente busca el equilibrio óptimo, asegurando que el algoritmo no agote la memoria disponible del sistema (Stack Overflow o Out of Memory), especialmente en entornos con recursos limitados como dispositivos móviles o sistemas embebidos.

## Complejidad Temporal

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Comparison_of_sorting_algorithms.png" title="Figura 4: Comparación del número de operaciones en distintos algoritmos de ordenamiento. Fuente: Wikimedia Commons." >}}

La Complejidad Temporal define la cantidad de tiempo que requiere un algoritmo para completarse en función de la longitud de la entrada $n$. Es fundamental comprender que en el análisis asintótico no medimos segundos o microsegundos, ya que estos dependen del procesador y la arquitectura; en su lugar, cuantificamos el número de operaciones elementales (como asignaciones, comparaciones y saltos) que el algoritmo realiza.

Al analizar el tiempo, nos centramos en cómo escala este conteo de operaciones a medida que $n$ crece exponencialmente. Un algoritmo de tiempo constante, $O(1)$, es el ideal teórico, mientras que un algoritmo de tiempo exponencial, $O(2^n)$, se vuelve computacionalmente intratable incluso para valores moderados de $n$. El análisis temporal es crítico para garantizar que una aplicación sea responsiva y pueda procesar grandes volúmenes de datos en tiempos aceptables para el usuario o el sistema.

## Análisis de Algoritmos con ejemplos

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Análisis_de_algoritmos_-_ordenass.svg" title="Ejemplo de análisis comparativo de algoritmos de ordenamiento. Fuente: Wikimedia Commons." >}}

El Análisis de Algoritmos es la aplicación práctica de la notación asintótica para evaluar y predecir el rendimiento de un bloque de código. Este proceso metodológico consiste en abstraer el código fuente en operaciones elementales (asignaciones, comparaciones, operaciones aritméticas) e identificar cómo estas escalan en función de la entrada de datos ($n$).

Al realizar este análisis, los ingenieros de software podemos tomar decisiones arquitectónicas fundamentadas, equilibrando el consumo de tiempo de CPU frente al uso de la memoria RAM. A continuación, se presentan ejemplos clásicos que ilustran cómo se determinan las complejidades temporal y espacial en diferentes escenarios.

Los ejemplos a continuación son simples, debes saber que existen múltiples algoritmos y estructuras de datos para resolver problemas usando código.

### Búsqueda Lineal

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Binary_search_vs_Linear_search_example_svg.svg" title="Figura 2: Comparación entre Búsqueda Lineal y Búsqueda Binaria. Fuente: Wikimedia Commons." >}}

#### Complejidad Temporal
En el peor de los casos (el objetivo está al final o no existe), el bucle iterará exactamente $n$ veces, donde $n$ es el tamaño de la lista. Por lo tanto, el tiempo de ejecución es estrictamente proporcional a la entrada, resultando en $O(n)$.

#### Complejidad Espacial
Independientemente de si la lista tiene diez o un millón de elementos, el algoritmo solo aloja en memoria la variable iteradora. Al no requerir estructuras de datos adicionales que crezcan con la entrada, su complejidad espacial se mantiene constante en $O(1)$.

### Bubble Sort (Ordenamiento de Burbuja)

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" title="Figura 3: Visualización del algoritmo Bubble Sort. Fuente: Wikimedia Commons." >}}

#### Complejidad Temporal
Este algoritmo compara elementos adyacentes y los intercambia si están en el orden incorrecto. Al tener dos bucles anidados que dependen de la longitud de la lista ($n$), en el peor de los casos (cuando la lista está en orden inverso), realizará una cantidad de operaciones proporcional a $n \times n$. Por ello, su complejidad temporal es cuadrática: $O(n^2)$.

#### Complejidad Espacial
El ordenamiento se realiza *in-place* (sobre la misma lista original), requiriendo únicamente espacio extra para realizar el intercambio temporal de variables. Por lo tanto, su complejidad espacial es $O(1)$.

### Búsqueda Binaria

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/6/64/Binary_Search_Depiction.svg" title="Figura 7: Representación paso a paso de la Búsqueda Binaria. Fuente: Wikimedia Commons." >}}

#### Complejidad Temporal
A diferencia de la búsqueda lineal, la búsqueda binaria divide el espacio de búsqueda a la mitad en cada iteración (requiriendo que la lista esté previamente ordenada). Esta división sucesiva hace que las operaciones crezcan de manera logarítmica respecto a la entrada. Su complejidad es muy eficiente: $O(\log n)$.

#### Complejidad Espacial
Si se implementa de manera iterativa, solo se necesitan punteros para el inicio, el fin y el punto medio, por lo que su complejidad es $O(1)$.

### Merge Sort

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg" title="Figura 4: Diagrama del algoritmo Merge Sort. Fuente: Wikimedia Commons." >}}

#### Complejidad Temporal
Merge Sort utiliza el paradigma de "Divide y Vencerás". Divide la lista repetidamente en mitades (lo que toma tiempo logarítmico $\log n$) y luego mezcla esas mitades ordenándolas (lo que toma tiempo lineal $n$). La combinación de ambos pasos nos da una complejidad temporal de $O(n \log n)$, siendo mucho más eficiente que Bubble Sort para grandes volúmenes de datos.

#### Complejidad Espacial
A diferencia de Bubble Sort, Merge Sort no ordena *in-place*. Necesita crear arreglos temporales auxiliares para almacenar las mitades antes de mezclarlas. En el peor de los casos, requerirá tanta memoria extra como la longitud de la lista original, resultando en una complejidad espacial de $O(n)$.

## Estructuras de Datos y Algoritmos Avanzados

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/8/84/Hash_table_average_insertion_time.png" title="Figura 9: Tiempo promedio de inserción en una Tabla Hash. Fuente: Wikimedia Commons." >}}

No todos los problemas se resuelven iterando listas. En la ingeniería de software real nos enfrentamos a escenarios donde necesitamos acceder a datos de forma casi instantánea, mantener colecciones ordenadas de manera eficiente o modelar relaciones complejas entre entidades. Para cada uno de estos casos existen estructuras de datos especializadas que debemos conocer.

Las **Tablas Hash** (conocidas como diccionarios en Python o HashMaps en Java) nos permiten asociar claves a valores y acceder a ellos en tiempo prácticamente constante, $O(1)$. Son la razón por la que una búsqueda en una base de datos indexada es casi instantánea, sin importar si tiene cien registros o cien millones.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg" title="Ejemplo de un Árbol Binario de Búsqueda (BST). Fuente: Wikimedia Commons." >}}

Los **Árboles** son estructuras jerárquicas que mantienen los datos organizados de forma que las operaciones de búsqueda, inserción y eliminación se realizan en $O(\log n)$. Variantes como los árboles AVL o Red-Black se autoequilibran para garantizar ese rendimiento incluso en los peores escenarios. Son la base de los índices en bases de datos y de los sistemas de archivos de tu sistema operativo.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Directed.svg" title="Ejemplo de un Grafo Dirigido. Fuente: Wikimedia Commons." >}}

Los **Grafos** permiten modelar relaciones entre entidades, algo que las listas y los árboles no pueden representar fácilmente. Cada vez que usas un GPS para encontrar la ruta más corta, navegas por recomendaciones en una red social o tu paquete viaja por la red hasta llegar a ti, hay un algoritmo de grafos (como Dijkstra, BFS o DFS) trabajando por detrás.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/d/d5/QUEUE_VS_STACK.svg" title="Comparación entre una Cola (Queue/FIFO) y una Pila (Stack/LIFO). Fuente: Wikimedia Commons." >}}

Las **Colas** y las **Pilas** son estructuras más sencillas, pero fundamentales. Una cola (FIFO) garantiza que los elementos se procesan en el orden en que llegan, como las tareas en una cola de impresión o los mensajes en un sistema de eventos. Una pila (LIFO) funciona al revés: el último en entrar es el primero en salir, como el historial de "deshacer" en cualquier editor o la pila de llamadas que gestiona la ejecución de tu propio código.

Cada una de estas estructuras tiene sus propias complejidades temporales y espaciales que afectan directamente al rendimiento de nuestras aplicaciones. En un próximo post profundizaremos en cada una de ellas con implementaciones y análisis detallados.

### Ejemplos

#### Búsqueda Lineal
```python
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
```

Complejidad Temporal: Mejor caso: $O(1)$ (El objetivo está en la primera posición).

Peor caso / Caso promedio: $O(n)$ (El objetivo está al final de la lista o no existe, requiriendo recorrer todos los elementos).

Complejidad Espacial: $O(1)$. Solo se utiliza una variable extra para el índice i, independientemente del tamaño de la lista.

#### Bubble Sort (Ordenamiento de Burbuja)
```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

Complejidad Temporal: Mejor caso: $O(n)$ (La lista ya está ordenada, solo se realiza una pasada).

Peor caso / Caso promedio: $O(n^2)$ (La lista está en orden inverso, requiriendo comparaciones e intercambios en cada iteración de los dos bucles anidados).

Complejidad Espacial: $O(1)$. El ordenamiento se realiza *in-place*, solo se utilizan variables temporales para el intercambio.

#### Búsqueda Binaria
```python
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
```

Complejidad Temporal: Mejor caso: $O(1)$ (El objetivo está exactamente en el punto medio).

Peor caso / Caso promedio: $O(\log n)$ (El espacio de búsqueda se divide a la mitad en cada iteración).

Complejidad Espacial: $O(1)$. Solo se utilizan tres variables auxiliares (inicio, fin, medio), independientemente del tamaño de la lista.

#### Merge Sort (Ordenamiento por Mezcla)
```python
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
```

Complejidad Temporal: Mejor caso / Peor caso / Caso promedio: $O(n \log n)$ (Siempre divide la lista en mitades y las mezcla, sin importar el orden inicial de los datos).

Complejidad Espacial: $O(n)$. Se crean arreglos auxiliares para almacenar las mitades durante la mezcla, requiriendo memoria proporcional al tamaño de la entrada.
