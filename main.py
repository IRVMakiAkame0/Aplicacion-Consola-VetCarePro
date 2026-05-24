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

    def registrar_mascota(self, mascota_nueva) -> None:
        if not self.validar.verificar_numero_correcto(mascota_nueva.peso):
            raise PesoInvalidoError(f"El peso de {mascota_nueva.nombre} debe ser mayor a cero.")
        self.registros_mascotas[mascota_nueva.id_mascota] = mascota_nueva
        
    def agregar_medicamento(self, medicamento_nuevo: Medicamento) -> None:
        self.inventario_farmacia[medicamento_nuevo.nombre] = medicamento_nuevo
        
    def generar_receta(self, id_buscado: str, nombre_medicina: str, enfermedad: str) -> str:
        mascota = self.registros_mascotas.get(id_buscado)
        medicina = self.inventario_farmacia.get(nombre_medicina)

        if not mascota:
            raise ValueError("ID de mascota no encontrado en los registros.")
        if not medicina:
            raise ValueError("Seleccione un medicamento valido.")
        if not enfermedad.strip():
            raise ValueError("Debe ingresar el diagnostico medico.")

        if medicina.verificar_si_es_peligroso(mascota.obtener_especie()):
            raise MedicamentoPeligrosoError(f"ALERTA: El medicamento {medicina.nombre} es TOXICO para la especie {mascota.especie}.")

        total_mg = medicina.calcular_dosis_final(mascota.peso)

        return (f"--- RECETA VETERINARIA ---\n\n"
                f"Fecha Emisión: {mascota.fecha_registro}\n"
                f"Paciente ID: {mascota.id_mascota}\n\n"
                f"Paciente: {mascota.nombre} (Raza: {mascota.raza} - {mascota.sexo})\n"
                f"Edad: {mascota.edad} años | Peso: {mascota.peso} kg\n"
                f"Responsable: {mascota.nombre_dueno}\n"
                f"Diagnóstico: {enfermedad}\n\n"
                f"Medicamento: {medicina.nombre}\n"
                f"Dosis Calculada: {total_mg} mg\n"
                f"--------------------------")

class InterfazGUI:
    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("VetCare Pro - Sistema de Gestion Clinica")
        self.ventana.geometry("520x820")
        
        # --- PALETA DE COLORES ---
        self.color_fondo = "#F4F4F9"            
        self.color_texto = "#000000"            
        self.color_morado_oscuro = "#512DA8"    
        self.color_lila = "#9B59B6"             
        self.color_morado_claro = "#D1C4E9"     
        
        self.ventana.configure(bg=self.color_fondo)

        style = ttk.Style()
        style.theme_use("clam") 

        self.sistema = ClinicaVeterinaria("VetCare Pro")
        self.cargar_medicamentos()
        self.dibujar_elementos()
