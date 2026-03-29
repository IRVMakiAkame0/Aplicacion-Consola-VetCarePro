import os
from datetime import datetime
from tabulate import tabulate

class Mascota:
    def __init__(self, id_mascota: str, nombre: str, especie: str, raza: str, peso: float, edad: int):
        self.id_mascota: str = id_mascota
        self.nombre: str = nombre
        self.especie: str = especie  
        self.raza: str = raza
        self.peso: float = peso       
        self.edad: int = edad

    def obtener_especie(self) -> str:
        return self.especie

    def obtener_peso(self) -> float:
        return self.peso
        
    def preparar_datos_tabla(self) -> list:
        return [self.id_mascota, self.nombre, self.especie, self.raza, f"{self.peso} kg", self.edad]

class Perro(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, peso: float, edad: int):
        Mascota.__init__(self, id_mascota, nombre, "Perro", raza, peso, edad)  
        
class Gato(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, peso: float, edad: int):
        Mascota.__init__(self, id_mascota, nombre, "Gato", raza, peso, edad)

class Ave(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, peso: float, edad: int):
        Mascota.__init__(self, id_mascota, nombre, "Ave", raza, peso, edad)

class Hamster(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, peso: float, edad: int):
        Mascota.__init__(self, id_mascota, nombre, "Hamster", raza, peso, edad)

class Conejo(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, peso: float, edad: int):
        Mascota.__init__(self, id_mascota, nombre, "Conejo", raza, peso, edad)

class Medicamento:
    def __init__(self, codigo: str, nombre: str, dosis_base_mg: float, especies_toxicas: list[str]):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.dosis_base_mg: float = dosis_base_mg
        self.especies_toxicas: list[str] = especies_toxicas 
        
    def calcular_dosis_final(self, peso_animal: float) -> float:
        return peso_animal * self.dosis_base_mg

    def verificar_si_es_peligroso(self, especie_paciente: str) -> bool:
        return especie_paciente.lower() in [e.lower() for e in self.especies_toxicas]

    def preparar_datos_tabla(self):
        toxicos = ", ".join(self.especies_toxicas) if self.especies_toxicas else "Seguro para todos"
        return [self.codigo, self.nombre, f"{self.dosis_base_mg} mg/kg", toxicos]

class ValidarDatos:
    def verificar_numero_correcto(self, valor: str) -> bool:
        if valor >= 0:
            return True 
        else:
            return False 
        
    def verificar_texto_lleno(self, texto: str) -> bool:
        if texto.strip():
            return True 
        else:
            return False
            
class DisenoReportes:
    def __init__(self, clinica_nombre: str):
        self.clinica_nombre: str = clinica_nombre
        
    def limpiar_la_pantalla(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def imprimir_titulo(self) -> None:
        print("_" *60)
        print(f"\n {self.clinica_nombre.upper()} - SISTEMA DE GESTION".center(60))
        print("_" *60)
        
    def mostrar_alerta(self, mensaje: str) -> None:
        print(f"\n ¡ALERTA MEDICA! \n {mensaje}")

class ClinicaVeterinaria:
    def __init__(self, nombre_negocio: str):
        self.nombre_negocio: str = nombre_negocio
        self.registros_mascotas: dict[str, Mascota] = {}
        self.inventario_farmacia: dict[str, Medicamento] = {}
        self.diseno: DisenoReportes = DisenoReportes(nombre_negocio)
        self.validar: ValidarDatos = ValidarDatos()
        
    def registrar_mascota(self, mascota_nueva: Mascota) -> None:
        if not self.validar.verificar_numero_correcto(mascota_nueva.peso):
            print(f"Error: El peso de {mascota_nueva.nombre} debe ser positivo.")
            return

        if mascota_nueva.id_mascota in self.registros_mascotas:
            print(f"Error: El ID {mascota_nueva.id_mascota} ya existe.")
            return
        self.registros_mascotas[mascota_nueva.id_mascota] = mascota_nueva
        
    def agregar_medicamento(self, medicamento_nuevo: Medicamento) -> None:
        if medicamento_nuevo.codigo in self.inventario_farmacia:
            print("Error: El codigo ya existe.")
            return
        self.inventario_farmacia[medicamento_nuevo.codigo] = medicamento_nuevo

    def mostrar_reportes(self) -> None:
        self.diseno.limpiar_la_pantalla()
        self.diseno.imprimir_titulo()
        
        lista_mascotas = [m.preparar_datos_tabla() for m in self.registros_mascotas.values()]
        lista_medicina = [med.preparar_datos_tabla() for med in self.inventario_farmacia.values()]
        
        print(f"\n         PACIENTES REGISTRADOS EN {self.nombre_negocio.upper()}    ")
        print(tabulate(lista_mascotas, headers=["ID", "Nombre", "Especie", "Raza", "Peso", "Edad"], tablefmt="fancy_grid"))
        
        print("\n          INVENTARIO DE MEDICAMENTOS    ")
        print(tabulate(lista_medicina, headers=["Código", "Nombre", "Dosis", "Toxicidad"], tablefmt="fancy_grid"))

    def generar_receta(self, id_buscado: str, cod_buscado: str):
        mascota = self.registros_mascotas.get(id_buscado)
        medicina = self.inventario_farmacia.get(cod_buscado)

        if not mascota or not medicina:
            return "Error: Mascota o medicamento no encontrados."

        if medicina.verificar_si_es_peligroso(mascota.obtener_especie()):
            self.diseno.mostrar_alerta(f"El medicamento {medicina.nombre} NO ES APTO para un {mascota.especie}.")
            return "\n RECETA CANCELADA \n"

        total_mg = medicina.calcular_dosis_final(mascota.obtener_peso())
        fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M")

        return (f"\nRECETA GENERADA {fecha_hoy}    \n"
                f"  Paciente: {mascota.nombre} ({mascota.raza})\n"
                f"  Medicamento: {medicina.nombre}\n"
                f"  Dosis Recomendada: {total_mg} mg\n"
                f"________________________________________")

#seccion de pruebas
sistema = ClinicaVeterinaria("VetCare Pro")

#comprobacion del funcioanmiento de registro de las mascotas (id, nombre, especie, raza, peso, edad)
p1 = Perro("10", "Max", "Golden", 30.5, 5)
p2 = Gato("20", "Luna", "Persa", 4.2, 3)
sistema.registrar_mascota(p1)
sistema.registrar_mascota(p2)

#prueba del funcionamiento de la clase Medicamento (codigo, nombre del medicamento, dosis, toxicidad)
med1 = Medicamento("M01", "Amoxicilina", 12.0, [])
med2 = Medicamento("M02", "Ibuprofeno", 5.0, ["Gato"]) 
sistema.agregar_medicamento(med1)
sistema.agregar_medicamento(med2)

#comprobacion del funcionamiento de las recetas y la toxicidad en animales (id del paciente, codigo)
sistema.mostrar_reportes()
print(sistema.generar_receta("10", "M01")) 
print(sistema.generar_receta("20", "M02")) 


