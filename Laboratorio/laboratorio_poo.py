from datetime import datetime, timedelta
from enum import Enum


class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def crear_tarea(self, titulo, detalle):
        try:
            tarea = Tarea(titulo, detalle)
            self.tareas.append(tarea)
            print(f"Tarea '{titulo}' creada exitosamente.")
        except ValueError as e:
            print(f"Error al crear la tarea: {e}")

    def leer_tareas(self):
        print("Lista de tareas:")
        for tarea in self.tareas:
            print(f"- {tarea.titulo} ({tarea.estado.value})")

    def actualizar_tarea(self, titulo, nuevo_estado):
        try:
            tarea = next(t for t in self.tareas if t.titulo == titulo)
            tarea.estado = EstadoTarea[nuevo_estado.upper()]
            print(f"Tarea '{titulo}' actualizada a estado '{nuevo_estado}'.")
        except StopIteration:
            print(f"No se encontró la tarea '{titulo}'.")

    def borrar_tarea(self, titulo):
        try:
            tarea = next(t for t in self.tareas if t.titulo == titulo)
            self.tareas.remove(tarea)
            print(f"Tarea '{titulo}' eliminada correctamente.")
        except StopIteration:
            print(f"No se encontró la tarea '{titulo}'.")

class EstadoTarea(Enum):
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETA = "Completa"

class Tarea:
    def __init__(self, titulo, detalle):
        self.titulo = titulo
        self.detalle = detalle
        self.estado = EstadoTarea.PENDIENTE

    def marcar_completa(self):
        self.estado = EstadoTarea.COMPLETA

class TareaRecurrente(Tarea):
    def __init__(self, titulo, detalle, fecha_inicio, fecha_fin, frecuencia):
        super().__init__(titulo, detalle)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.frecuencia = frecuencia

    def marcar_completa(self):
        if datetime.now() >= self.fecha_fin:
            super().marcar_completa()

class TareaProgramada(Tarea):
    def __init__(self, titulo, detalle, fecha_programada):
        super().__init__(titulo, detalle)
        self.fecha_programada = fecha_programada
        
