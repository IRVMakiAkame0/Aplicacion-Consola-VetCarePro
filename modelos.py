from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, id_mascota: str, nombre: str, especie: str, raza: str, sexo: str, peso: float, edad: int, nombre_dueno: str, fecha_registro: str):
        self.id_mascota: str = id_mascota
        self.nombre: str = nombre
        self.especie: str = especie  
        self.raza: str = raza
        self.sexo: str = sexo
        self.peso: float = peso       
        self.edad: int = edad
        self.nombre_dueno: str = nombre_dueno
        self.fecha_registro: str = fecha_registro 
        
    def obtener_especie(self) -> str:
        return self.especie

    def obtener_peso(self) -> float:
        return self.peso

    @abstractmethod
    def revisar_paciente(self) -> str:
        pass

class Perro(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, sexo: str, peso: float, edad: int, nombre_dueno: str, fecha_registro: str):
        super().__init__(id_mascota, nombre, "Perro", raza, sexo, peso, edad, nombre_dueno, fecha_registro)  
    
    def revisar_paciente(self) -> str:
        return "Inspección canina"
        
class Gato(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, sexo: str, peso: float, edad: int, nombre_dueno: str, fecha_registro: str):
        super().__init__(id_mascota, nombre, "Gato", raza, sexo, peso, edad, nombre_dueno, fecha_registro)
        
    def revisar_paciente(self) -> str:
        return "Inspección felina"

class Ave(Mascota):
    def __init__(self, id_mascota: str, nombre: str, raza: str, sexo: str, peso: float, edad: int, nombre_dueno: str, fecha_registro: str):
        super().__init__(id_mascota, nombre, "Ave", raza, sexo, peso, edad, nombre_dueno, fecha_registro)
        
    def revisar_paciente(self) -> str:
        return "Inspección aviar"
