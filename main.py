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

    def cargar_medicamentos(self):
        self.sistema.agregar_medicamento(Medicamento("Amoxicilina", 12.0, []))
        self.sistema.agregar_medicamento(Medicamento("Cefalexina", 20.0, []))
        self.sistema.agregar_medicamento(Medicamento("Meloxicam", 0.1, []))
        self.sistema.agregar_medicamento(Medicamento("Ibuprofeno", 5.0, ["Gato", "Ave"])) 
        self.sistema.agregar_medicamento(Medicamento("Paracetamol", 10.0, ["Gato", "Perro"]))
        self.sistema.agregar_medicamento(Medicamento("Permetrina", 15.0, ["Gato", "Ave"]))
        self.sistema.agregar_medicamento(Medicamento("Vitaminas Complejo B", 2.0, []))

    def dibujar_elementos(self):
        fuente_titulo_app = ("Segoe UI", 18, "bold")
        fuente_subtitulos = ("Segoe UI", 12, "bold")
        fuente_label_normal = ("Segoe UI", 10, "normal") 
        fuente_entrada = ("Segoe UI", 10)

        tk.Label(self.ventana, text="VetCare Pro", font=fuente_titulo_app, bg=self.color_fondo, fg=self.color_morado_oscuro).pack(pady=(20, 10))

        frame_registro = tk.Frame(self.ventana, bg=self.color_fondo)
        frame_registro.pack(pady=10)

        tk.Label(frame_registro, text="Informacion del Paciente", font=fuente_subtitulos, bg=self.color_fondo, fg=self.color_lila).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        tk.Label(frame_registro, text="Nombre del Animal:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=1, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_nombre = tk.Entry(frame_registro, width=32, font=fuente_entrada, fg=self.color_texto, relief="solid", bd=1)
        self.entrada_nombre.grid(row=1, column=1, sticky="w", pady=6)

        tk.Label(frame_registro, text="Responsable / Dueño:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=2, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_dueno = tk.Entry(frame_registro, width=32, font=fuente_entrada, fg=self.color_texto, relief="solid", bd=1)
        self.entrada_dueno.grid(row=2, column=1, sticky="w", pady=6)

        tk.Label(frame_registro, text="Especie:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=3, column=0, sticky="e", pady=6, padx=(0, 10))
        self.combo_especie = ttk.Combobox(frame_registro, values=list(DICCIONARIO_RAZAS.keys()), state="readonly", width=30)
        self.combo_especie.grid(row=3, column=1, sticky="w", pady=6)
        self.combo_especie.bind("<<ComboboxSelected>>", self.actualizar_lista_razas)

        tk.Label(frame_registro, text="Raza:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=4, column=0, sticky="e", pady=6, padx=(0, 10))
        self.combo_raza = ttk.Combobox(frame_registro, state="readonly", width=30)
        self.combo_raza.grid(row=4, column=1, sticky="w", pady=6)

        tk.Label(frame_registro, text="Sexo:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=5, column=0, sticky="e", pady=6, padx=(0, 10))
        self.combo_sexo = ttk.Combobox(frame_registro, values=["Macho", "Hembra"], state="readonly", width=30)
        self.combo_sexo.grid(row=5, column=1, sticky="w", pady=6)

        tk.Label(frame_registro, text="Edad (Años):", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=6, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_edad = ttk.Spinbox(frame_registro, from_=0, to=30, width=15)
        self.entrada_edad.grid(row=6, column=1, sticky="w", pady=6)

        tk.Label(frame_registro, text="Peso (Kg):", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=7, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_peso = tk.Entry(frame_registro, width=17, font=fuente_entrada, fg=self.color_texto, relief="solid", bd=1)
        self.entrada_peso.grid(row=7, column=1, sticky="w", pady=6)

        tk.Button(frame_registro, text="Registrar y Generar ID", bg=self.color_morado_oscuro, fg="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.procesar_registro).grid(row=8, column=0, columnspan=2, pady=(15, 0), ipadx=15, ipady=4)

        frame_medico = tk.Frame(self.ventana, bg=self.color_fondo)
        frame_medico.pack(pady=15)

        tk.Label(frame_medico, text="Orden Medica y Dosificacion", font=fuente_subtitulos, bg=self.color_fondo, fg=self.color_lila).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        tk.Label(frame_medico, text="ID Registrado:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=1, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_id_buscar = tk.Entry(frame_medico, width=32, font=("Segoe UI", 10, "bold"), fg=self.color_morado_oscuro, relief="solid", bd=1)
        self.entrada_id_buscar.grid(row=1, column=1, sticky="w", pady=6)

        tk.Label(frame_medico, text="Diagnostico:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=2, column=0, sticky="e", pady=6, padx=(0, 10))
        self.entrada_enfermedad = tk.Entry(frame_medico, width=32, font=fuente_entrada, fg=self.color_texto, relief="solid", bd=1)
        self.entrada_enfermedad.grid(row=2, column=1, sticky="w", pady=6)

        tk.Label(frame_medico, text="Medicamento:", bg=self.color_fondo, fg=self.color_texto, font=fuente_label_normal).grid(row=3, column=0, sticky="e", pady=6, padx=(0, 10))
        lista_meds = sorted(list(self.sistema.inventario_farmacia.keys()))
        self.combo_medicina = ttk.Combobox(frame_medico, values=lista_meds, state="readonly", width=30)
        self.combo_medicina.grid(row=3, column=1, sticky="w", pady=6)

        # Botón Generar Receta
        tk.Button(frame_medico, text="Generar Receta", bg=self.color_morado_oscuro, fg="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.procesar_receta).grid(row=4, column=0, columnspan=2, pady=(15, 0), ipadx=15, ipady=4)

        # Botón Ver Historial Clinico
        tk.Button(self.ventana, text="Ver Historial Clinico", bg=self.color_morado_claro, fg=self.color_texto, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.abrir_ventana_reportes).pack(pady=20, ipadx=20, ipady=6)

