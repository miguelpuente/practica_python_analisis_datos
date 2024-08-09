import os
import platform

from laboratorio_poo import (
    ColaboradorTiempoCompleto,
    ColaboradorTiempoParcial,
    GestionColaboradores,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Colaboradores ==========")
    print('1. Agregar Colaborador Tiempo Completo')
    print('2. Agregar Colaborador Tiempo Parcial')
    print('3. Buscar Colaborador por DNI')
    print('4. Actualizar Colaborador')
    print('5. Eliminarar Colaborador por DNI')
    print('6. Mostrar Todos los Colaboradores¿')
    print('7. Salir')
    print('======================================================')

def agregar_colaborador(gestion, tipo_colaborador):
    try:
        dni = input('Ingrese DNI del colaborador: ')
        nombre = input('Ingrese nombre del colaborador: ')
        apellido = input('Ingrese apellido del colaborador: ')
        edad = int(input('Ingrese edad del colaborador: '))
        salario = float(input('Ingrese salario del colaborador: '))

        if tipo_colaborador == '1':
            departamento = input('Ingrese departamento del colaborador: ')
            colaborador = ColaboradorTiempoCompleto(dni, nombre, apellido, edad, salario, departamento)
        elif tipo_colaborador == '2':
            horas_semanales = int(input('Ingrese hora semanales del colaborador: '))
            colaborador = ColaboradorTiempoParcial(dni, nombre, apellido, edad, salario, horas_semanales)
        else:
            print('Opción inválida')
            return

        gestion.crear_colaborador(colaborador)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_colaborador_por_dni(gestion):
    dni = input('Ingrese el DNI del colaborador a buscar: ')
    gestion.leer_colaborador(dni)
    input('Presione enter para continuar...')

def actualizar_salario_colaborador(gestion):
    dni = input('Ingrese el DNI del colaborador para actualizar salario: ')
    salario = float(input('Ingrese el salario del colaborador'))
    gestion.actualizar_colaborador(dni, salario)
    input('Presione enter para continuar...')

def eliminar_colaborador_por_dni(gestion):
    dni = input('Ingrese el DNI del colaborador a eliminar: ')
    gestion.eliminar_colaborador(dni)
    input('Presione enter para continuar...')

def mostrar_todos_los_colaboradores(gestion):
    print('=============== Listado completo de los  Colaboradores ==============')
    for colaborador in gestion.leer_datos().values():
        if 'departamento' in colaborador:
            print(f"{colaborador['nombre']} - Departamento {colaborador['departamento']}")
        else:
            print(f"{colaborador['nombre']} - Horas Semanales {colaborador['horas_semanales']}")
    print('=====================================================================')
    input('Presione enter para continuar...')

if __name__ == "__main__":
    gestion = GestionColaboradores()

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_colaborador(gestion, opcion)
        
        elif opcion == '3':
            buscar_colaborador_por_dni(gestion)

        elif opcion == '4':
            actualizar_salario_colaborador(gestion)

        elif opcion == '5':
            eliminar_colaborador_por_dni(gestion)

        elif opcion == '6':
            mostrar_todos_los_colaboradores(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
        

