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

ingresos = float(input("Por favor indique el total de sus ingresos anuales: \n"))

if ingresos <= 10000:
    impuestos = ingresos * 0.10
elif ingresos <= 20000:
    impuestos = (10000 * 0.10) + ((ingresos - 10000) * 0.20)
elif ingresos <= 30000:
    impuestos = (10000 * 0.10) + (20000 * 0.20) + ((ingresos - 20000) * 0.30)
else:
    impuestos = (10000 * 0.10) + (20000 * 0.20) + (30000 * 0.30) + ((ingresos - 30000) * 0.40)
    
print(f"Impuesto a pagar: ${impuestos:.2f}")
    
