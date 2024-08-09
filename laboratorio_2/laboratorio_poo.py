'''
Desafío 1: Sistema de Gestión de Colaborador

Objetivo: Desarrollar un sistema para gestionar colaboradores de una empresa.

Requisitos:
    • Crear una clase base Colaborador con atributos como nombre, apellido, edad, salario, etc.
    • Definir clases derivadas para diferentes tipos de empleados (por ejemplo, ColaboradorTiempoCompleto, ColaboradorTiempoParcial) con atributos y métodos específicos.
    • Implementar operaciones CRUD para gestionar los empleados.
    • Manejar errores con bloques try-except para validar entradas y gestionar excepciones (por ejemplo, salario negativo, longitud dni, etc).
    • Persistir los datos en archivo JSON.
'''

import mysql.connector
from mysql.connector import Error
from decouple import config
import json

class Colaborador:
    def __init__(self, dni, nombre, apellido, edad, salario):
        self.__dni = self.validar_dni(dni)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = self.validar_salario(salario)

    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def apellido(self):
        return self.__apellido.capitalize()
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        self.__salario = self.validar_salario(nuevo_salario)

    def validar_dni(self, dni):
        try:
            dni_num = int(dni)
            if len(str(dni)) not in [7, 8]:
                raise ValueError("El DNI debe tener 7 u 8 dígitos.")
            if dni_num <= 0:
                raise ValueError("El DNI debe ser numérico positivo.")
            return dni_num
        except ValueError:
            raise ValueError("El DNI debe ser numérico y estar compuesto por 7 u 8 dígitos.")

    def validar_salario(self, salario):
        try:
            salario_num = float(salario)
            if salario_num <= 0:
                raise ValueError("El salario debe ser numérico positivo.")
            return salario_num
        except ValueError:
            raise ValueError("El salario debe ser un número válido.")

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "salario": self.salario
        }

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ColaboradorTiempoCompleto(Colaborador):
    def __init__(self, dni, nombre, apellido, edad, salario, departamento):
        super().__init__(dni, nombre, apellido, edad, salario)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    def to_dict(self):
        data = super().to_dict()
        data["departamento"] = self.departamento
        return data

    def __str__(self):
        return f"{super().__str__()} - Departamento: {self.departamento}"

class ColaboradorTiempoParcial(Colaborador):
    def __init__(self, dni, nombre, apellido, edad, salario, horas_semanales):
        super().__init__(dni, nombre, apellido, edad, salario)
        self.__horas_semanales = horas_semanales

    @property
    def horas_semanales(self):
        return self.__horas_semanales

    def to_dict(self):
        data = super().to_dict()
        data["horas_semanales"] = self.horas_semanales
        return data

    def __str__(self):
        return f"{super().__str__()} - Horas Semanales: {self.horas_semanales}"

class GestionColaboradores:
    def __init__(self):
        self.host = config('DB_HOST')
        self.database = config('DB_NAME')
        self.user= config('DB_USER')
        self.password=config('DB_PASSWORD')
        self.port = config('DB_PORT')

    def connect(self):
        '''Establecer una conexión con la base de datos'''
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )

            if connection.is_connected():
                return connection

        except Error as e:
            print(f'Error al conectar a la base de datos: {e}')
            return None
###
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')
###
    def crear_colaborador(self, colaborador):
        try:
            connection = self.connect()
            if connection:
                with connection.cursor() as cursor:
                    # Verificar si el DNI ya existe
                    cursor.execute('SELECT dni FROM colaboradores WHERE dni = %s', (colaborador.dni,))
                    if cursor.fetchone():
                        print(f'Error: Ya existe un colaborador con DNI {colaborador.dni}')
                        return
                    
                    # Insertar colaborador dependiendo del tipo
                    if isinstance(colaborador, ColaboradorTiempoCompleto):
                        query = '''
                        INSERT INTO colaboradores (dni, nombre, apellido, edad, salario)
                        VALUES (%s, %s, %s, %s, %s)
                        '''
                        cursor.execute(query, (colaborador.dni, colaborador.nombre, colaborador.apellido, colaborador.edad, colaborador.salario))

                        query = '''
                        INSERT INTO colaboradortiempocompleto (dni, departamento)
                        VALUES (%s, %s)
                        '''

                        cursor.execute(query, (colaborador.dni, colaborador.departamento))

                    elif isinstance(colaborador, ColaboradorTiempoParcial):
                        query = '''
                        INSERT INTO colaboradores (dni, nombre, apellido, edad, salario)
                        VALUES (%s, %s, %s, %s, %s)
                        '''
                        cursor.execute(query, (colaborador.dni, colaborador.nombre, colaborador.apellido, colaborador.edad, colaborador.salario))

                        query = '''
                        INSERT INTO colaboradortiempoparcial (dni, horas_semanales)
                        VALUES (%s, %s)
                        '''

                        cursor.execute(query, (colaborador.dni, colaborador.horas_semanales))

                    connection.commit()
                    print(f'Colaborador {colaborador.nombre} {colaborador.apellido} creado correctamente')
        except Exception as error:
            print(f'Error inesperado al crear colaborador: {error}')


    def leer_colaborador(self, dni):
        try:
            connection = self.connect()
            if connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute('SELECT * FROM colaboradores WHERE dni = %s', (dni,))
                    colaborador_data = cursor.fetchone()

                    if colaborador_data:
                        cursor.execute('SELECT departamento FROM colaboradortiempocompleto WHERE dni = %s', (dni,))
                        departamento = cursor.fetchone()

                        if departamento:
                            colaborador_data['departamento'] = departamento['departamento']
                            colaborador = ColaboradorTiempoCompleto(**colaborador_data)
                        else:
                            cursor.execute('SELECT horas_semanales FROM colaboradortiemp    oparcial WHERE dni = %s', (dni,))
                            horas_semanales = cursor.fetchone()
                            if horas_semanales:
                                colaborador_data['horas_semanales'] = horas_semanales['horas_semanales']
                                colaborador = ColaboradorTiempoParcial(**colaborador_data)
                            else:
                                colaborador = Colaborador(**colaborador_data)

                        print(f'Colaborador encontrado: {colaborador}')

                    else:
                        print(f'No se encontró colaborador con DNI {dni}.')

        except Error as e:
            print('Error al leer colaborador: {e}')
        finally:
            if connection.is_connected():
                connection.close()

    def actualizar_colaborador(self, dni, nuevo_salario):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                 datos[dni]['salario'] = nuevo_salario
                 self.guardar_datos(datos)
                 print(f'Salario actualizado para el colalborador DNI:{dni}')
            else:
                print(f'No se encontró colaborador con DNI:{dni}')
        except Exception as e:
            print(f'Error al actualizar el colaborador: {e}')

    def eliminar_colaborador(self, dni):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                 del datos[dni]
                 self.guardar_datos(datos)
                 print(f'colalborador DNI:{dni} eliminado correctamente')
            else:
                print(f'No se encontró colaborador con DNI:{dni}')
        except Exception as e:
            print(f'Error al eliminar el colaborador: {e}')
