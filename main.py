import os
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from datos import DICCIONARIO_RAZAS
from modelos import Perro, Gato, Ave, Medicamento, ValidarDatos
from excepciones import PesoInvalidoError, MedicamentoPeligrosoError
