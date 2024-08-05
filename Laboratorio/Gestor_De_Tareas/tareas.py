import json
import os
import uuid
from datetime import datetime
from enum import Enum

# Funciones para el manejo de fechas

"""parsear_fecha toma una string con formato dd/mm/AAAA y lo tranforma en un objeto datetime
formatear_fecha toma un objeto datetime y lo formatea como una cadena "día/mes/año"
"""

def parsear_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        return None

def formatear_fecha(fecha):
    return fecha.strftime("%d/%m/%Y")

class EstadoTarea(Enum):
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETA = "Completa"

class Tarea:
    def __init__(self, titulo, detalle):
        self._id = str(uuid.uuid4()) # Asigna un identificador único universal
        self._titulo = titulo
        self._detalle = detalle
        self._estado = EstadoTarea.PENDIENTE

    @property
    def id(self):
        return self._id

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
        if isinstance(valor, str):
            valor = valor.upper().replace(" ", "_")
        self._estado = EstadoTarea[valor]

    def marcar_completa(self):
        self.estado = EstadoTarea.COMPLETA

    def to_dict(self):
        return {
            "id": self.id,
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


# Gestor de Tareas
class GestorDeTareas:
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar_tareas()

    def solicitar_fecha(self, mensaje):
        while True:
            fecha_str = input(mensaje)
            fecha = parsear_fecha(fecha_str)
            if fecha:
                return fecha
            else:
                print("Fecha inválida. Por favor, use el formato dd/mm/AAAA.")

    def crear_tarea(self, titulo, detalle):
        tipo_tarea = input("¿Programar? (s/n): ").lower()
        if tipo_tarea == "s":
            fecha_programada = self.solicitar_fecha("Fecha (dd/mm/AAAA): ")
            tarea = TareaProgramada(titulo, detalle, fecha_programada)
        elif tipo_tarea == "n":
            tipo_repetir = input("¿Repetir? (s/n): ").lower()
            if tipo_repetir == "s":
                fecha_inicio = self.solicitar_fecha("Ingrese la fecha de inicio (dd/mm/AAAA): ")
                fecha_fin = self.solicitar_fecha("Ingrese la fecha de fin (dd/mm/AAAA): ")
                frecuencia = input("Ingrese la frecuencia (diaria, semanal, mensual): ")
                tarea = TareaRecurrente(titulo, detalle, fecha_inicio, fecha_fin, frecuencia)
            else:
                tarea = Tarea(titulo, detalle)
        
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"Tarea: {titulo} creada exitosamente.")

    def leer_tareas(self):
        print("Lista de tareas:")
        for tarea in self.tareas:
            print(f"- {tarea.titulo} ({tarea.estado.value}) \n{tarea.detalle}\n")

#    def buscar_tarea_por_titulo(self, titulo):
#        """Busca una tarea por su título y devuelve la tarea si se encuentra."""
#        tareas = [t for t in self.tareas if t.titulo == titulo]
#        if not tareas:
#            return None
        
#        if len(tareas) > 1:
#            return self.seleccionar_tarea(tareas)
#        else:
#            return tareas[0]

    def seleccionar_tarea(self, tareas):
        print("Seleccione la tarea:")
        for idx, tarea in enumerate(tareas):
            print(f"{idx + 1}. {tarea.titulo} ({tarea.estado.value}) \n{tarea.detalle}\n)")
        while True:
            seleccion = input("Ingrese el número de la tarea: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(tareas):
                return tareas[int(seleccion) - 1]
            else:
                print("Selección inválida. Por favor, intente de nuevo.")

    def actualizar_tarea(self, titulo, nuevo_estado):
        tareas = [t for t in self.tareas if t.titulo == titulo]
        if not tareas:
            print(f"Tarea: {titulo} no encontrada.")
            return
        
        if len(tareas) > 1:
            tarea = self.seleccionar_tarea(tareas)
        else:
            tarea = tareas[0]
        
        try:
            tarea.estado = nuevo_estado
            self.guardar_tareas()
            print(f"Tarea {tarea.titulo} actualizada a estado {nuevo_estado}.")
        except KeyError:
            print(f"Estado {nuevo_estado} no es válido. Use pendiente, en progreso o completa.")

    def borrar_tarea(self, titulo):
        tareas = [t for t in self.tareas if t.titulo == titulo]
        if not tareas:
            print(f"Tarea: {titulo} no encontrada.")
            return
        
        if len(tareas) > 1:
            tarea = self.seleccionar_tarea(tareas)
        else:
            tarea = tareas[0]

        self.tareas.remove(tarea)
        self.guardar_tareas()
        print(f"Tarea {tarea.titulo} eliminada correctamente.")

    def guardar_tareas(self):
        with open(self.archivo, "w") as f:
            json.dump([tarea.to_dict() for tarea in self.tareas], f, indent=4)

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                tareas_data = json.load(f)
                self.tareas = []
                for tarea_data in tareas_data:
                    estado = tarea_data.get("estado", "").upper().replace(" ", "_")
                    if "fecha_programada" in tarea_data:
                        tarea = TareaProgramada(
                            tarea_data["titulo"], 
                            tarea_data["detalle"], 
                            parsear_fecha(tarea_data["fecha_programada"])
                        )
                    elif "fecha_inicio" in tarea_data and "fecha_fin" in tarea_data:
                        tarea = TareaRecurrente(
                            tarea_data["titulo"], 
                            tarea_data["detalle"], 
                            parsear_fecha(tarea_data["fecha_inicio"]), 
                            parsear_fecha(tarea_data["fecha_fin"]), 
                            tarea_data["frecuencia"]
                        )
                    else:
                        tarea = Tarea(tarea_data["titulo"], tarea_data["detalle"])
                    tarea.estado = estado
                    tarea._id = tarea_data.get("id", str(uuid.uuid4()))  # Si no tiene un id genera uno nuevo
                    self.tareas.append(tarea)
