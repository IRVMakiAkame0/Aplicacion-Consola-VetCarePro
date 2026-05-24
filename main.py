import os
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from datos import DICCIONARIO_RAZAS
from modelos import Perro, Gato, Ave, Medicamento, ValidarDatos
from excepciones import PesoInvalidoError, MedicamentoPeligrosoError

class ClinicaVeterinaria:
    def __init__(self, nombre_negocio: str):
        self.nombre_negocio: str = nombre_negocio
        self.registros_mascotas: dict = {}
        self.inventario_farmacia: dict = {}
        self.validar = ValidarDatos()
        self.contadores_ids: dict[str, int] = {"ave": 1, "gato": 1, "perro": 1}
        
    def generar_siguiente_id(self, especie: str) -> str:
        if especie == "ave":
            prefijo = "0"
            consecutivo = self.contadores_ids["ave"]
            self.contadores_ids["ave"] += 1
        elif especie == "gato":
            prefijo = "1"
            consecutivo = self.contadores_ids["gato"]
            self.contadores_ids["gato"] += 1
        else:
            prefijo = "2"
            consecutivo = self.contadores_ids["perro"]
            self.contadores_ids["perro"] += 1
            
        return f"{prefijo}{consecutivo:04d}"
