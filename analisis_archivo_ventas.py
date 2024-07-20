# #######################################
# ## Trabajo con datos de ventas.csv
# #######################################

'''
Ejemplo 1: Filtrado por marca y calcular:
    - Precio Promedio
    - Desviación Estándar
    - Precio Máximo
    - Precio Mínimo
    - Cantidad Total Vendida
    - Ingresos Totales
    - Frecuencia de Ventas
'''

import csv
from collections import defaultdict
import statistics

def analisis_estadistico_ventas(archivo_csv):
    """
    Realiza un análisis estadístico de ventas a partir de un archivo CSV.
    
    Args:
    - archivo_csv (str): Nombre del archivo CSV a procesar.
    
    Returns:
    - dict: Diccionario con resultados por marca.
    """
    # Utilizar defaultdict para acumular datos por marca
    marca_datos = defaultdict(list)

    try:
        # Abrir el archivo CSV en modo lectura
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            # Crear un objeto lector de CSV
            csv_reader = csv.DictReader(file, delimiter=';')

            # Iterar sobre cada fila del archivo CSV
            for row_num, row in enumerate(csv_reader, start=1):
                try:
                    marca = row['Marca']
                    precio_venta = float(row['precio de venta'])
                    cantidad_vendida = 1  # Asumimos que cada fila representa una venta

                    # Acumular precios, cantidades y calcular ingresos por marca
                    marca_datos[marca].append({
                        'precio_venta': precio_venta,
                        'cantidad_vendida': cantidad_vendida,
                        'ingresos': precio_venta * cantidad_vendida
                    })
                except ValueError as e:
                    print(f"Error de conversión de datos en la fila {row_num}: {e}")
                except KeyError as e:
                    print(f"Dato faltante en la fila {row_num}: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row_num}: {e}")

        # Preparar diccionario para almacenar resultados por marca
        resultados = {}

        # Calcular métricas por marca
        for marca, datos in marca_datos.items():
            precios = [d['precio_venta'] for d in datos]
            cantidades = [d['cantidad_vendida'] for d in datos]
            ingresos = [d['ingresos'] for d in datos]

            if len(precios) > 1:
                precio_promedio = statistics.mean(precios)
                desviacion_estandar = statistics.stdev(precios)
            else:
                precio_promedio = precios[0] if precios else 0
                desviacion_estandar = 0
            
            precio_maximo = max(precios) if precios else 0
            precio_minimo = min(precios) if precios else 0
            cantidad_total_vendida = sum(cantidades)
            ingresos_totales = sum(ingresos)
            frecuencia_ventas = len(datos)  # Cantidad de transacciones por marca

            # Almacenar resultados por marca en el diccionario
            resultados[marca] = {
                'Precio Promedio': precio_promedio,
                'Desviación Estándar': desviacion_estandar,
                'Precio Máximo': precio_maximo,
                'Precio Mínimo': precio_minimo,
                'Cantidad Total Vendida': cantidad_total_vendida,
                'Ingresos Totales': ingresos_totales,
                'Frecuencia de Ventas': frecuencia_ventas
            }

    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo_csv}")
    except csv.Error as e:
        print(f"Error al procesar el archivo CSV: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        return resultados

# Ejemplo de uso:
if __name__ == "__main__":
    archivo_csv = 'ventas.csv'
    resultados = analisis_estadistico_ventas(archivo_csv)
    
    # Imprimir resultados
    for marca, datos in resultados.items():
        print(f'Marca: {marca}')
        for metrica, valor in datos.items():
            print(f'  {metrica}: {valor:.2f}')
        print()


'''
Explicación de librerías:

    1 - csv: Esta es una biblioteca estándar de Python que proporciona funcionalidades para leer y escribir archivos CSV. El módulo csv.DictReader se utiliza en este caso para leer el archivo CSV como un diccionario, donde las claves son los nombres de las columnas y los valores son los datos de cada fila.

    2 - collections.defaultdict: Este es un contenedor especializado en la biblioteca estándar de Python que se comporta como un diccionario estándar, excepto cuando intentas acceder a una clave que no existe, en cuyo caso crea automáticamente un nuevo valor utilizando una función que le proporcionas al crearlo. En este caso, defaultdict(list) se utiliza para marca_datos, permitiendo acumular datos (en forma de listas) para cada clave de marca sin necesidad de inicializar explícitamente cada lista.

    3 - statistics: Este es un módulo de la biblioteca estándar de Python que proporciona funciones matemáticas y estadísticas básicas. Se utiliza principalmente para calcular el promedio (statistics.mean) y la desviación estándar (statistics.stdev) de una lista de números. Estas funciones son útiles para calcular métricas estadísticas como el precio promedio y la desviación estándar de los precios de venta por cada marca.

    
Explicación del código:
    
    1 - Función analisis_estadistico_ventas:

        - Esta función encapsula todo el proceso de análisis estadístico de ventas a partir de un archivo CSV.
        - Toma como argumento archivo_csv, el nombre del archivo CSV a procesar.
        - Devuelve un diccionario resultados que contiene métricas calculadas por cada marca.

    2 - Manejo de excepciones:

        - Se utilizan bloques try-except para manejar posibles errores durante la lectura y procesamiento del archivo CSV.
        - Se capturan y manejan errores como FileNotFoundError (archivo no encontrado), csv.Error (errores genéricos de CSV) y Exception (cualquier otro error inesperado).

    3 - Cálculo de métricas por marca:

        - Dentro del bloque try, se itera sobre cada fila del archivo CSV utilizando csv.DictReader.
        - Se acumulan los datos relevantes (precios de venta, cantidades vendidas, ingresos) por marca en marca_datos.
        - Se calculan métricas como precio_promedio, desviacion_estandar, precio_maximo, precio_minimo, cantidad_total_vendida, ingresos_totales y frecuencia_ventas para cada marca.

    4 - Almacenamiento y retorno de resultados:

        - Los resultados calculados por marca se almacenan en el diccionario resultados.
        - Finalmente, la función retorna el diccionario resultados que contiene todas las métricas calculadas por cada marca.

    5 - Ejemplo de uso:

        - En el bloque if __name__ == "__main__":, se muestra un ejemplo de cómo utilizar la función analisis_estadistico_ventas con el archivo ventas.csv.
        - Se imprime cada métrica calculada para cada marca obtenida de resultados.

    
    Este enfoque estructurado y modular no solo mejora la legibilidad y mantenibilidad del código, sino que también proporciona una manera robusta de manejar y analizar datos de ventas desde un archivo CSV, asegurando que se capturen y manejen adecuadamente los posibles errores que puedan surgir durante el procesamiento de datos.
'''
