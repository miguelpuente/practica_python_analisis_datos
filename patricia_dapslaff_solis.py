"""
'''
    Listas y Tuplas


        Ejercicio: Gestión de Inventario

        - Crea una lista con los nombres de cinco productos y sus respectivas cantidades en una tupla (producto, cantidad).
        - Agrega un nuevo producto con su cantidad al final de la lista.
        - Encuentra e imprime el producto con la mayor cantidad disponible.
        - Convierte la lista en una tupla de tuplas.
'''
productos = [
    ("llavero", 25), 
    ("vincha", 32), 
    ("colita", 150), 
    ("broche", 27), 
    ("calco", 65)
]

nuevo_producto = ("anotador", 40)
productos.append(nuevo_producto)

producto_max = max(productos, key = lambda producto: producto[1])
print(f"El producto con mayor disponibilidad es: {producto_max[0]}, con {producto_max[1]} unidades disponibles \n")

tupla_productos = tuple(productos)
print(tupla_productos)


'''
    Diccionarios

        Ejercicio: Sistema de Calificaciones

        - Crea un diccionario con los nombres de tres estudiantes y sus respectivas calificaciones.
        - Agrega un nuevo estudiante y su calificación.
        - Calcula e imprime el promedio de las calificaciones.
        - Encuentra e imprime el estudiante con la calificación más alta.
'''
calificaciones = {
    "Sofía": 9,
    "Elena": 7,
    "Carmen": 10,
}

calificaciones["Hector"] = 6

promedio = sum(calificaciones.values()) / len(calificaciones)
print(f"\n \nPromedio de calificaciones: {promedio}")

calificacion_max = max(calificaciones, key=calificaciones.get)
print(f"El mejor estudiante es: {calificacion_max} con ({calificaciones[calificacion_max]}) puntos\n\n")


'''
    Condicionales

        Ejercicio: Clasificación de Edad

        - Solicita al usuario que ingrese su edad.
        - Imprime una clasificación basada en la edad: 
            niño (0-12),
            adolescente (13-17), 
            adulto (18-64), 
            adulto mayor (65+).
'''

edad = int(input("Por favor, ingrese su edad: "))

if 0 < edad <= 12:
    print(f"Usted es un niño\n\n")
elif edad >=13 and edad <= 17:
    print(f"Usted es un adolescente\n\n")
elif edad >=18 and edad <= 64:
    print(f"Usted es un adulto\n\n")
elif edad >= 65:
    print(f"Usted es un adulto mayor. Por favor, cuídese!\n\n")
else:
    print("Revise la edad.\n\n")


print("*" * 50)


'''
        Ejercicio: Cálculo de Impuestos

        - Solicita al usuario que introduzca sus ingresos anuales.
        - Calcula el impuesto a pagar según los siguientes tramos: 
            10% para ingresos hasta 10,000,
            20% para ingresos entre 10,001 y 20,000,
            30% para ingresos entre 20,001 y 30,000,
            y 40% para ingresos superiores a 30,000.
'''

ingresos = float(input("Por favor indique el total de sus ingresos anuales: "))

if ingresos <= 10000:
    impuestos = ingresos * 0.10
elif ingresos <= 20000:
    impuestos = (10000 * 0.10) + ((ingresos - 10000) * 0.20)
elif ingresos <= 30000:
    impuestos = (10000 * 0.10) + (20000 * 0.20) + ((ingresos - 20000) * 0.30)
else:
    impuestos = (10000 * 0.10) + (20000 * 0.20) + (30000 * 0.30) + ((ingresos - 30000) * 0.40)
    
print(f"Impuesto a pagar: ${impuestos:.2f}\n\n")
    

'''
    Bucles For
        Ejercicio: Serie Fibonacci

        - Calcula e imprime los primeros 20 números de la serie Fibonacci.
'''
fibonacci = [0, 1]

for i in range(2,20):
    next = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next)
    
print(f"Estos son los 20 primeros números de la serie Fibonacci con bucle for:\n{fibonacci}\n")

# Serie fibonacci con bucle while

fibonacci_2 = [0, 1]

while len(fibonacci_2) < 20:
    next_2 = fibonacci_2[-1] + fibonacci_2[-2]
    fibonacci_2.append(next_2)
    
print(f"Estos son los 20 primeros números de la serie Fibonacci con bucle while:\n{fibonacci_2}\n")


'''
    Bucles While
        Ejercicio: Sumatoria hasta un Límite

        - Solicita al usuario que ingrese números hasta que la suma de todos los números ingresados sea al menos 100.
        - Imprime la suma total y la cantidad de números ingresados.
'''
total_suma = 0
total_numeros = 0

while total_suma <= 100:
    numero = int(input("Ingrese números enteros menores a 100: "))
    total_suma += numero
    total_numeros += 1
    
print(f"\nEl total de la suma es: {total_suma}")
print(f"La cantidad de números sumados es: {total_numeros}\n\n")


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
import math


def promedio_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def desvest_lista(lista):
    if len(lista) < 2:
        return 0
    
    promedio = promedio_lista(lista)
    varianza = sum((x - promedio) ** 2 for x in lista) / len(lista)
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar
    
datos = [2, 15, 96, 35, 74, 66, 14, 12, 13, 5, 7]
calcular_promedio = promedio_lista(datos)
calcular_desvest = desvest_lista(datos)


print(f"Lista: {datos}")
print(f"El promedio de la lista es: {calcular_promedio}")
print(f"La desviación estandar de la lista es: {calcular_desvest:.2f}\n\n")

"""
'''
    Manejo de Errores y Excepciones
        Ejercicio: Total de ventas

        - Crea una función que lea un archivo CSV con datos de ventas, calcule la suma total de ventas y maneje posibles errores de lectura o cálculo.

'''
import csv


def calcular_total_ventas(archivo_csv):
    try:
        with open(archivo_csv, "r", encoding="utf-8") as archivo:
            lectura = csv.reader(archivo, delimiter=";")
            next(lectura)
            total_ventas = 0
            for fila in lectura:
                try:
                    venta = float(fila[7])
                    total_ventas += venta
                except ValueError:
                    print(f"Se encontró un valor no numérico en la fila: {fila}")
                    continue
        print(f"El total de ventas es: {total_ventas:.2f}")
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no se encuentra.")
    except Exception as error:
        print(f"Error inesperado: {error}")
    else:
        return total_ventas
    finally:
        print("Hemos finalizado")

archivo_csv = "ventas.csv"
calcular_total_ventas(archivo_csv)
