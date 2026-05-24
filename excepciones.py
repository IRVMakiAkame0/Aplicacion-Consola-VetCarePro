class VeterinariaError(Exception):
    "Error base para la aplicación"
    pass

class PesoInvalidoError(VeterinariaError):
    "Se lanza si el peso es menor o igual a cero"
    pass

class MedicamentoPeligrosoError(VeterinariaError):
    "Se lanza si el medicamento es tóxico para la especie"
    pass
