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
