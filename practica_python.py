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


'''
    Funciones
        Ejercicio: Operaciones estadísticas

        - Crea una función que calcule el promedio de una lista de números.
        - Crea otra función que calcule la desviación estándar de una lista de números.
            Pasos para calcular la desviación estándar
                Paso 1: calcular la promedio/media.
                Paso 2: calcular el cuadrado de la distancia al promedio/media para cada dato.
                Paso 3: sumar los valores que resultaron del paso 2.
                Paso 4: dividir entre el número de datos. (varianza)
                Paso 5: sacar la raíz cuadrada. 
        - Utiliza estas funciones para analizar un conjunto de datos.
'''

# import math

# # Función para calcular el promedio/media de una lista de números
# def calcular_promedio(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# # Función para calcular la desviación estándar de una lista de números
# def calcular_desviacion_estandar(lista):
#     if len(lista) < 2:
#         return 0

#     promedio = calcular_promedio(lista)
#     # suma_cuadrado_diferencia_media = 0

#     # for x in lista:
#     #     suma_cuadrado_diferencia_media += (x -promedio) ** 2
#     # else:
#     #     varianza = suma_cuadrado_diferencia_media / len(lista)

#     varianza = sum((x -promedio) ** 2 for x in lista) / len(lista)

#     desviacion_estandar = math.sqrt(varianza)

#     return desviacion_estandar


# # Ejemplo de uso
# datos = [25, 38, 24, 33, 35, 23, 27, 59, 36, 55]
# promedio = calcular_promedio(datos)
# desviacion_estandar = calcular_desviacion_estandar(datos)


# print(f'Datos: {datos}')
# print(f'Promedio: {promedio}')
# print(f'Desviación estándar: {desviacion_estandar:.2f}')



'''
    Manejo de Errores y Excepciones
        Ejercicio: Total de ventas

        - Crea una función que lea un archivo CSV con datos de ventas, calcule la suma total de ventas y maneje posibles errores de lectura o cálculo.

'''

import csv

# Función para calcular la suma total de ventas desde un archivo CSV
def calcular_suma_total_ventas(archivo_csv):
    suma_venta = 0
    try:

        with open(archivo_csv, 'r') as archivo:
            lectura = csv.reader(archivo, delimiter=';')
            cabecera = next(lectura)

            # for line in lectura:
            #     suma_venta += float(line[7])

            nombre_columna = 'precio de venta'
            # for line in lectura:
            #     suma_venta += float(line[cabecera.index(nombre_columna)])

            suma_venta = sum([float(line[cabecera.index(nombre_columna)]) for line in lectura])
            

    except FileNotFoundError:
        print(f'Error: El archivo {archivo_csv} no fue encontrado')
    except ValueError:
        print('Error: Se encontró un valor no numérico en el archivo')
    except Exception as error:
        print(f'Error inesperado: {error}')
    else:
        return suma_venta
    finally:
        print('Hola soy el Finally')

# Ejemplo de uso
archivo = 'ventas.csv'
suma_total = calcular_suma_total_ventas(archivo)

if suma_total:
    print(f'La suma total de ventas es: {suma_total:.2f}')













'''
    Manejo de Archivos
        Ejercicio: 

        - Crear una función que tome datos de un diccionario y los escriba en un archivo de texto en formato JSON.
'''

# Función para escribir datos en formato JSON en un archivo
def escribir_datos_json(datos, archivo_salida):
    pass






