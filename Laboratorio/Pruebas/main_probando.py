import os
import platform

from tareas import GestorDeTareas, TareaProgramada, TareaRecurrente

def limpiar_pantalla():
    """Limpiar la pantalla según el sistema operativo"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("\nMenú:\n ")
    print("1. Crear una tarea")
    print("2. Consultar tareas")
    print("3. Actualizar estado")
    print("4. Borrar una tarea")
    print("5. Salir")

def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            titulo = input("\nTítulo: ")
            detalle = input("Detalle: ")
            gestor.crear_tarea(titulo, detalle)
        elif opcion == "2":
            gestor.leer_tareas()
        elif opcion == "3":
            titulo = input("\nTítulo de la tarea a actualizar: ")
            tarea = gestor.buscar_tarea_por_titulo(titulo)
            if tarea is None:
                print(f"\nTarea: {titulo} no encontrada.")
            else:
                nuevo_estado = input("Ingrese el nuevo estado (pendiente, en progreso, completa): ")
                try:
                    tarea.estado = nuevo_estado
                    gestor.guardar_tareas()
                    print(f"\nTarea {tarea.titulo} actualizada a estado {nuevo_estado}.")
                except KeyError:
                    print(f"\nEstado {nuevo_estado} no es válido. Use pendiente, en progreso o completa.")
        elif opcion == "4":
            titulo = input("Título de la tarea a borrar: ")
            gestor.borrar_tarea(titulo)
        elif opcion == "5":
            print("Ha finalizado el sistema ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()
