import os
from datetime import datetime
from tabulate import tabulate

class Mascota:
    def __init__(self, id_mascota, nombre, especie, raza, peso, edad):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie  
        self.raza = raza
        self.peso = peso       
        self.edad = edad

    def obtener_especie(self):
        return self.especie

    def obtener_peso(self):
        return self.peso
        
    def preparar_datos_tabla(self):
        return [self.id_mascota, self.nombre, self.especie, self.raza, f"{self.peso} kg", self.edad]

class Perro(Mascota):
    def __init__(self, id_mascota, nombre, raza, peso, edad):
        Mascota.__init__(self, id_mascota, nombre, "Perro", raza, peso, edad)  
        
class Gato(Mascota):
    def __init__(self, id_mascota, nombre, raza, peso, edad):
        Mascota.__init__(self, id_mascota, nombre, "Gato", raza, peso, edad)

class Ave(Mascota):
    def __init__(self, id_mascota, nombre, raza, peso, edad):
        Mascota.__init__(self, id_mascota, nombre, "Ave", raza, peso, edad)

class Hamster(Mascota):
    def __init__(self, id_mascota, nombre, raza, peso, edad):
        Mascota.__init__(self, id_mascota, nombre, "Hamster", raza, peso, edad)

class Conejo(Mascota):
    def __init__(self, id_mascota, nombre, raza, peso, edad):
        Mascota.__init__(self, id_mascota, nombre, "Conejo", raza, peso, edad)

class Medicamento:
    def __init__(self, codigo, nombre, dosis_base_mg, especies_toxicas):
        self.codigo = codigo
        self.nombre = nombre
        self.dosis_base_mg = dosis_base_mg
        self.especies_toxicas = especies_toxicas 
        
    def calcular_dosis_final(self, peso_animal):
        return peso_animal * self.dosis_base_mg

    def es_peligroso_para(self, especie_paciente):
        return especie_paciente.lower() in [e.lower() for e in self.especies_toxicas]

    def preparar_datos_tabla(self):
        toxicos = ", ".join(self.especies_toxicas) if self.especies_toxicas else "Seguro para todos"
        return [self.codigo, self.nombre, f"{self.dosis_base_mg} mg/kg", toxicos]
