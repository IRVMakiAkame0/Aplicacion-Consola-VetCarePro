# Aplicacion-Consola-VetCarePro
Sistema desarrollado en Python para la gestión automatizada de pacientes y prescripciones médicas, enfocado en la seguridad del paciente y la precisión en la dosificación.

## Descripción del proyecto
Este software es una solución orientada a objetos desarrollada en python para la administración de pacientes y control de inventario en una clínica veterinaria. El sistema pone especial énfasis en la seguridad clínica, automatizando el cálculo de dosis y estableciendo restricciones de seguridad basadas en la compatibilidad biológica entre especies/razas y componentes químicos.

## Tecnologías y librerías
- **Lenguaje:** Python 3.13.
- **Librerias:**
    - **tabulate:** Para la creación de tablas estéticas en la terminal.
    - **os:** Para el diseño visual de los reportes tecnicos en la terminal.
    - **datetime:** Para el registro de fecha y hora real en las recetas medicas.
 
## Funcionalidades implementadas
- Gestión de pacientes: Registro detallado que incluye especie y raza para precision diagnostica.
- Gestión de entidades mediante diccionarios: Uso de estructuras tipo dict para busquedas eficientes de pacientes y medicamentos.
- Calculo de dosificacion automatica: Determinación de mg requeridos segun el peso del animal.
- Validacion de toxicidad: Bloqueo de recetas para medicamentos contraindicados por especie.
- Reportes tabulares: Visualización tecnica de datos mediante la libreria tabulate.

## Estructura del proyecto
El código está organizado bajo el paradigma de Programación Orientada a Objetos (POO):
- **Mascota:** Clase base y subclases para la gestión de datos biológicos.
    - **Perro:** Hereda de Mascota.
    - **Gato:** Hereda de Mascota.
    - **Ave:** Hereda de Mascota.
    - **Hamster:** Hereda de Mascota.
    - **Conejo:** Hereda de Mascota.
- **Medicamento:** Lógica de cálculo de dosis y validación de seguridad.
- **ClinicaVeterinaria:** Controlador principal que gestiona el inventario y los registros.
- **ValidarDatos:** Clase de apoyo para la integridad de la información.
- **DisenoReportes:** Gestión de la interfaz de usuario en consola.

## Guía de pruebas
1. **Validación de registro:** Intentar registrar dos mascotas con el mismo ID para verificar la restricción de unicidad; si se registra bien la mascota el sistema lo confirmara y el nombre de la mascota aparecera en la tabla de reportes.
2. **Vadación de peso:** Intentar registrar el peso de un paciente con un numero negativo, el sistema le mostrara `Error: El peso debe ser positivo` y bloquea el registro.
3. **Cálculo de dosis:** Validar que el peso multiplicado por la dosis base genere el resultado correcto en la receta.
4. **Prueba de toxicidad:** Intentar recetar un medicamento marcado como tóxico para una especie; el sistema muestra **¡ALERTA MÉDICA!** y debe bloquear la transacción de la receta.

## Instrucciones de instalación y configuración:
### Requisitos previos
- **Python 3.13** o superior.
- Gestor de paquetes `pip` actualizado.

1. Clone este repositorio en su máquina local:
   git clone https://github.com/IRVMakiAkame0/Aplicacion-Consola-VetCarePro.git
2. Instale las dependencias necesarias (tabulate):
    pip install tabulate
3. Ejecute el archivo principal para iniciar el sistema:
    python main.py

## Autora
- **Isabella Ruiz Velasquez** - Estudiante de Ingeniería de Sistemas (2do Semestre)
- **Institución:** Universidad de Medellín


