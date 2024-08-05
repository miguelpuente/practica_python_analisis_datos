import os
import platform
import json
from datetime import datetime
from enum import Enum

# Funciones Auxiliares
def limpiar_pantalla():
    '''Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("Menú:\n")
    print("1. Crear tarea")
    print("2. Leer tareas")
    print("3. Actualizar tarea")
    print("4. Borrar tarea")
    print("5. Salir")

def parsear_fecha(fecha_str):
    return datetime.strptime(fecha_str, '%d/%m/%Y')

def formatear_fecha(fecha):
    return fecha.strftime('%d/%m/%Y')

# Clases
class EstadoTarea(Enum):
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETA = "Completa"

class Tarea:
    def __init__(self, titulo, detalle):
        self._titulo = titulo
        self._detalle = detalle
        self._estado = EstadoTarea.PENDIENTE

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, valor):
        self._detalle = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = EstadoTarea(valor)

    def marcar_completa(self):
        self.estado = EstadoTarea.COMPLETA

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "detalle": self.detalle,
            "estado": self.estado.value
        }

class TareaRecurrente(Tarea):
    def __init__(self, titulo, detalle, fecha_inicio, fecha_fin, frecuencia):
        super().__init__(titulo, detalle)
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._frecuencia = frecuencia

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self._fecha_inicio = valor

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, valor):
        self._fecha_fin = valor

    @property
    def frecuencia(self):
        return self._frecuencia

    @frecuencia.setter
    def frecuencia(self, valor):
        self._frecuencia = valor

    def marcar_completa(self):
        if datetime.now() >= self.fecha_fin:
            super().marcar_completa()

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "fecha_inicio": formatear_fecha(self.fecha_inicio),
            "fecha_fin": formatear_fecha(self.fecha_fin),
            "frecuencia": self.frecuencia
        })
        return data

class TareaProgramada(Tarea):
    def __init__(self, titulo, detalle, fecha_programada):
        super().__init__(titulo, detalle)
        self._fecha_programada = fecha_programada

    @property
    def fecha_programada(self):
        return self._fecha_programada

    @fecha_programada.setter
    def fecha_programada(self, valor):
        self._fecha_programada = valor

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "fecha_programada": formatear_fecha(self.fecha_programada)
        })
        return data

class GestorDeTareas:
    def __init__(self, archivo='tareas.json'):
        self.tareas = []
        self.archivo = archivo
        self.cargar_tareas()

    def crear_tarea(self, titulo, detalle):
        tipo_tarea = input("¿Es una tarea programada o recurrente? (p/r/n): ").lower()
        if tipo_tarea == 'p':
            fecha_programada = input("Ingrese la fecha programada (dd/mm/AAAA): ")
            fecha_programada = parsear_fecha(fecha_programada)
            tarea = TareaProgramada(titulo, detalle, fecha_programada)
        elif tipo_tarea == 'r':
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/AAAA): ")
            fecha_fin = input("Ingrese la fecha de fin (dd/mm/AAAA): ")
            frecuencia = input("Ingrese la frecuencia (diaria, semanal, mensual): ")
            fecha_inicio = parsear_fecha(fecha_inicio)
            fecha_fin = parsear_fecha(fecha_fin)
            tarea = TareaRecurrente(titulo, detalle, fecha_inicio, fecha_fin, frecuencia)
        else:
            tarea = Tarea(titulo, detalle)
        
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"Tarea '{titulo}' creada exitosamente.")

    def leer_tareas(self):
        print("Lista de tareas:")
        for tarea in self.tareas:
            print(f"- {tarea.titulo} ({tarea.estado.value})")

    def actualizar_tarea(self, titulo, nuevo_estado):
        try:
            tarea = next(t for t in self.tareas if t.titulo == titulo)
            tarea.estado = nuevo_estado
            self.guardar_tareas()
            print(f"Tarea '{titulo}' actualizada a estado '{nuevo_estado}'.")
        except StopIteration:
            print(f"No se encontró la tarea '{titulo}'.")

    def borrar_tarea(self, titulo):
        try:
            tarea = next(t for t in self.tareas if t.titulo == titulo)
            self.tareas.remove(tarea)
            self.guardar_tareas()
            print(f"Tarea '{titulo}' eliminada correctamente.")
        except StopIteration:
            print(f"No se encontró la tarea '{titulo}'.")

    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump([tarea.to_dict() for tarea in self.tareas], f, indent=4)

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                tareas_data = json.load(f)
                self.tareas = [
                    TareaProgramada(
                        tarea['titulo'], 
                        tarea['detalle'], 
                        parsear_fecha(tarea['fecha_programada'])
                    ) if 'fecha_programada' in tarea else 
                    TareaRecurrente(
                        tarea['titulo'], 
                        tarea['detalle'], 
                        parsear_fecha(tarea['fecha_inicio']), 
                        parsear_fecha(tarea['fecha_fin']), 
                        tarea['frecuencia']
                    ) if 'fecha_inicio' in tarea and 'fecha_fin' in tarea else 
                    Tarea(tarea['titulo'], tarea['detalle'])
                    for tarea in tareas_data
                ]
                for tarea, tarea_data in zip(self.tareas, tareas_data):
                    tarea.estado = EstadoTarea[tarea_data['estado'].upper()]

# Función Principal
def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            detalle = input("Detalle: ")
            gestor.crear_tarea(titulo, detalle)
        elif opcion == "2":
            gestor.leer_tareas()
        elif opcion == "3":
            titulo = input("Título de la tarea a actualizar: ")
            nuevo_estado = input("Ingrese el nuevo estado (pendiente, en progreso, completa): ")
            gestor.actualizar_tarea(titulo, nuevo_estado)
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
