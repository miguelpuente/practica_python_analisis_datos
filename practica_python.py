'''
    Listas y Tuplas


        Ejercicio: Gestión de Inventario

        - Crea una lista con los nombres de cinco productos y sus respectivas cantidades en una tupla (producto, cantidad).
        - Agrega un nuevo producto con su cantidad al final de la lista.
        - Encuentra e imprime el producto con la mayor cantidad disponible.
        - Convierte la lista en una tupla de tuplas.
'''

# # Lista de productos y cantidades
# inventario = [("Manzanas", 50), ("Bananas", 30), ("Naranjas", 40), ("Peras", 25), ("Uvas", 60)]

# # Agregar un nuevo producto
# nuevo_produto = ("Kiwi", 20)

# inventario.append(nuevo_produto)

# # Encuentra e imprime el producto con la mayor cantidad disponible.
# producto_max = max(inventario, key=lambda x: x[1])
# print(f'Producto con mayor cantidad: {producto_max[0]} ({producto_max[1]} unidades)')

# # Convierte la lista en una tupla de tuplas.
# inventario_tupla = tuple(inventario)
# print(f'Inventario (tupla): {inventario_tupla}')

#################################################################################################
#################################################################################################

'''
    Diccionarios

        Ejercicio: Sistema de Calificaciones

        - Crea un diccionario con los nombres de tres estudiantes y sus respectivas calificaciones.
        - Agrega un nuevo estudiante y su calificación.
        - Calcula e imprime el promedio de las calificaciones.
        - Encuentra e imprime el estudiante con la calificación más alta.
'''

# # Diccionario de estudiantes y calificaciones
# estudiantes = {"Ana": 85, "Juan": 92, "Maria": 78}

# # Agregar un nuevo estudiante
# estudiantes["Carlos"] = 88

# # Calcular el promedio de las calificaciones
# promedio = sum(estudiantes.values()) / len(estudiantes)
# print(f'Promedio de calificaciones: {promedio:.2f}')

# # Encontrar el estudiante con la calificación más alta
# mejor_estudiante = max(estudiantes, key=estudiantes.get)
# print(f'Mejor estudiante: {mejor_estudiante} ({estudiantes[mejor_estudiante]} puntos)')

#################################################################################################
#################################################################################################

''''
    Condicionales

        Ejercicio: Clasificación de Edad

        - Solicita al usuario que ingrese su edad.
        - Imprime una clasificación basada en la edad: 
    
            niño (0-12),

            adolescente (13-17), 

            adulto (18-64), 

            adulto mayor (65+).

'''

# # Solicitar la edad al usuario
# edad = int(input("Ingrese su edad: "))

# # Clasificación basada en la edad
# if 0 < edad <= 12:
#     print('Clasificación: Niño')
# elif edad >=13 and edad <= 17:
#     print('Clasificación: Adolescente')
# elif edad >=18 and edad <= 64:
#     print('Clasificación: Adulto')
# elif edad >= 65:
#     print('Clasificación: Adulto Muyar')
# else:
#     print('Edad no válida')

#################################################################################################
#################################################################################################

'''
        Ejercicio: Cálculo de Impuestos

        - Solicita al usuario que introduzca sus ingresos anuales.
        - Calcula el impuesto a pagar según los siguientes tramos: 

            10% para ingresos hasta 10,000,

            20% para ingresos entre 10,001 y 20,000,

            30% para ingresos entre 20,001 y 30,000,

            y 40% para ingresos superiores a 30,000.
'''

# # Solicitar los ingresos anuales al usuario
# ingresos = float(input("Ingresos anuales: "))


# # Cálculo del impuesto
# if ingresos <= 10000:
#     impuesto = ingresos * 0.10
# elif ingresos <= 20000:
#     impuesto = 10000 * 0.10 + (ingresos - 10000) * 0.20
# elif ingresos <= 30000:
#     impuesto = 10000 * 0.10 + 10000 * 0.20 + (ingresos - 20000) * 0.30
# else:
#     impuesto = 10000 * 0.10 + 10000 * 0.20 + 10000 * 0.30 + (ingresos - 30000) * 0.40

# print(f'Impuesto a pagar: ${impuesto:.2f}')

#################################################################################################
#################################################################################################

'''
    Bucles For
        Ejercicio: Serie Fibonacci

        - Calcula e imprime los primeros 20 números de la serie Fibonacci.
'''

# ## Forma 1

# # Inicializar la serie Fibonacci
# fibonacci = [0, 1]

# # Calcular los primeros 20 números de la serie Fibonacci
# for i in range(2,20):
#     siguiente = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(siguiente)

# print(f'Serie Fibonacci: {fibonacci}')

########

# ## Forma 2 (Taty)

# # Inicializar la serie Fibonacci
# fibonacci = [0, 1]

# # Calcular los primeros 20 números de la serie Fibonacci
# for i in range(1,19):
#     siguiente = fibonacci[i] + fibonacci[i-1]
#     fibonacci.append(siguiente)

# print(f'Serie Fibonacci: {fibonacci}')

#################################################################################################
#################################################################################################

'''
    Bucles While
        Ejercicio: Sumatoria hasta un Límite

        - Solicita al usuario que ingrese números hasta que la suma de todos los números ingresados sea al menos 100.
        - Imprime la suma total y la cantidad de números ingresados.
'''


# # Inicializar la suma y el contador
# suma = 0
# contador = 0

# # Bucle while hasta que la suma sea al menos 100
# while suma < 100:
#     numero = float(input("Ingrese un número: "))
#     suma += numero
#     contador += 1

# # Imprimir la suma total y la cantidad de números ingresados
# print(f"La suma total es: {suma}")
# print(f"Se ingresaron {contador} números.")

##################################################################################################################################################################################################
##################################################################################################################################################################################################


