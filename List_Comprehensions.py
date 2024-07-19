# '''
# Definición y propósito:

# Las list comprehensions son una forma concisa de crear listas en Python.
#     - Permiten generar listas a partir de secuencias u otras estructuras de datos de manera más compacta que utilizando bucles tradicionales.
#     - Ventajas sobre bucles tradicionales:

# Más legibles y compactas.
#     - Menor cantidad de código.
#     - Eficiencia en términos de velocidad de ejecución en muchos casos.

# Sintaxis básica:

#     - La sintaxis general de una list comprehension es [expr for item in iterable].
#     - Donde expr es la expresión que define los elementos de la nueva lista, item es el elemento actual que se está iterando sobre el iterable, y iterable es la secuencia o estructura de datos de entrada.
# '''

# #######################################
# ## Sintaxis y Ejemplos Básicos
# #######################################

# # Ejemplo 1: Crear una lista de cuadrados usando un bucle for

# cuadrados = []
# for x in range(10):
#     cuadrados.append(x**2)

# # Mismo ejemplo usando list comprehension
# cuadrados_lc = [x**2 for x in range(10)]

# print(cuadrados)    # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(cuadrados_lc) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# #######################################
# ## Condiciones en List Comprehensions
# #######################################

# # Ejemplo 2: Filtrar números pares usando un bucle for

# even_numbers = []
# for x in range(10):
#     if x % 2 == 0:
#         even_numbers.append(x)

# # Mismo ejemplo usando list comprehension con condición
# even_numbers_lc = [x for x in range(10) if x % 2 == 0]

# print(even_numbers)         # Output: [0, 2, 4, 6, 8]
# print(even_numbers_lc)      # Output: [0, 2, 4, 6, 8]



# #######################################
# ## List Comprehensions Anidadas
# #######################################

# # Ejemplo 3: Crear una matriz (lista de listas) usando bucles anidados
# matriz = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(j)
#     matriz.append(row)

# # Mismo ejemplo usando list comprehension anidada
# matriz_lc = [[j for j in range(3)] for i in range(3)]

# print(matriz)           # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# print(matriz_lc)        # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# #######################################
# ####### Actividades Prácticas
# #######################################

# # Actividad 1: Transformar una lista de números en sus valores absolutos usando list comprehensions.

# numeros = [-2, -1, 0, 1, 2]
# valores_absolutos = [abs(num) for num in numeros]

# print(valores_absolutos)  # Output: [2, 1, 0, 1, 2]


# # Actividad 2: Filtrar una lista de palabras para obtener solo aquellas que empiezan con una vocal.

# palabras = ['apple', 'banana', 'pear', 'orange', 'kiwi']
# palabras_empiezan_vocal = [palabra for palabra in palabras if palabra[0] in 'aeiou']

# print(palabras_empiezan_vocal)  # Output: ['apple', 'orange']


# # Actividad 3: Crear una matriz de números aleatorios utilizando list comprehensions.

# import random

# matriz = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

# print(matriz)           # Output: [[7, 2, 5, 10], [3, 4, 1, 9], [8, 6, 4, 2]]


# '''
# Recursos Adicionales:

#     - Documentación oficial de Python sobre list comprehensions: Python Documentation on List Comprehensions
#     - Ejemplos y casos de uso en bibliotecas de análisis de datos como pandas y numpy.
    
#         Python Documentation on List Comprehensions:    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# Conclusiones:

#     - Recapitulación de los conceptos aprendidos.
#     - Importancia de utilizar list comprehensions para escribir código más legible y eficiente.
#     - Uso de list comprehensions en combinación con otras estructuras de datos y bibliotecas de análisis de datos.
# '''

