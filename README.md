# VetCare Pro - Sistema de Gestión Clínica (GUI)
Sistema desarrollado en Python con Interfaz Gráfica de Usuario (GUI) para la gestión automatizada de pacientes y prescripciones médicas, enfocado en la seguridad del paciente, la precisión en la dosificación y la aplicación estricta de principios de Programación Orientada a Objetos (POO).

## Descripción del proyecto
Este software es una solución de arquitectura modular desarrollada en Python para la administración de pacientes y control de inventario en una clínica veterinaria. El sistema evoluciona de una aplicación de consola a una interfaz gráfica completa, poniendo especial énfasis en la seguridad clínica mediante el cálculo automático de dosis, restricciones de compatibilidad biológica y el control de flujo a través de excepciones personalizadas.

## Tecnologías y librerías
- **Lenguaje:** Python 3.13.
- **Interfaz Grafica Utilizada:**
    - **tkinter / ttk:** Para la creación y estilización moderna de la Interfaz Gráfica de Usuario (ventanas botones, formularios y tablas dinámicas).
- **Librerias:**
    - **datetime:** Para la captura automática y registro de fecha y hora exacta en las historias clínicas y recetas médicas.
    - **abc (Abstract Base Classes):** Para garantizar el cumplimiento de contratos de abstracción en los modelos de datos.
    
## Funcionalidades implementadas
- Interfaz Gráfica Moderna: Diseño intuitivo con formularios alineados, paleta de colores corporativa (lila y gris) y ventanas secundarias para visualización de reportes.
- Generación Automática de IDs: Creación de identificadores únicos de 5 dígitos (ej. 00001) basados en un sistema de prefijos jerárquicos por especie (0 para caninos, 1 para felinos, 2 para aves).
- Sanitización de Datos:* Limpieza automática de las entradas del usuario (capitalización de nombres propios y formato de oración para diagnósticos) para mantener la integridad de la base de datos.
- Gestión de entidades mediante diccionarios: Uso de estructuras tipo dict para almacenamiento temporal y búsquedas eficientes en memoria.
- Cálculo de dosificación automática: Determinación exacta de los miligramos (mg) requeridos multiplicando el peso del animal por la dosis base del fármaco.
- Validación estricta de toxicidad: Bloqueo de recetas médicas contraindicadas por especie, interrumpiendo el flujo mediante excepciones.
- Filtros de Búsqueda: Historial clínico avanzado con capacidad de filtrar datos por coincidencia de texto (nombre o dueño) y rangos de tiempo.


## Estructura del proyecto (Modularización)
El código está organizado en cuatro archivos bajo el paradigma de Programación Orientada a Objetos (POO):
1. **modelos.py**
    - **Mascota:** Clase base abstracta (ABC) que define la estructura biológica y obliga a implementar el método revisar_paciente().
    - **Perro, Gato, Ave:** Subclases especializadas que heredan de Mascota e implementan su propia lógica de revisión.
    - **Medicamento:** Encapsula la lógica matemática de cálculo de dosis y la verificación cruzada de seguridad.
    - **ValidarDatos:** Clase de apoyo lógica para la integridad inicial de la información.

2. **excepciones.py**
    - **VeterinariaError:** Clase base de errores para el ecosistema de la clínica.
    - **PesoInvalidoError:** Lanzada si se ingresan valores negativos o iguales a cero.
    - **MedicamentoPeligrosoError:** Lanzada críticamente si se receta un fármaco tóxico para la especie tratada.

3. **datos.py**
    - Diccionario estático y tipado que actúa como base de datos local, conteniendo las especies y sus respectivas razas ordenadas alfabéticamente.

4. **main.py**
    - **ClinicaVeterinaria:** Controlador principal que gestiona el inventario, los registros y los contadores de IDs.
    - **InterfazGUI:** Gestión de la vista, ventanas emergentes (messagebox) y recolección de eventos de la interfaz.

## Guía de pruebas
1. **Prueba de Registro e ID:** Complete los datos de un paciente y haga clic en "Registrar y Generar ID". El sistema limpiará los errores tipográficos, mostrará una ventana emergente de éxito confirmando el registro y pegará automáticamente el nuevo ID generado en la zona de orden médica.
2. **Validación de peso y edad:** Intente ingresar letras o un número negativo en el peso/edad. El sistema capturará la excepción y desplegará una alerta advirtiendo sobre el error de formato, bloqueando el guardado.
3. **Prueba de Toxicidad (Regla de Negocio):** Registre un paciente de especie "Gato". Luego, en la zona médica, intente recetarle el medicamento "Permetrina" o "Ibuprofeno". El sistema debe lanzar la excepción MedicamentoPeligrosoError, cancelar la receta y mostrar una alerta médica de contraindicación.
4. **Cálculo de dosis exitoso:** Seleccione un medicamento seguro (Ej. "Amoxicilina"). Verifique que la receta final muestre el cálculo correcto (Peso x Dosis Base).
5. **Reportes:** Abra el historial clínico, registre varios pacientes y utilice la barra superior para buscar por el nombre del dueño o filtrar por "Hoy (Día)".


## Instrucciones de instalación y configuración:
### Requisitos previos
- **Python 3.13** o superior.
- Gestor de paquetes `pip` actualizado.
- No se requieren dependencias externas (Tkinter viene preinstalado en la biblioteca estándar de Python).

### Instalación
1. Clone este repositorio en su máquina local:
   git clone https://github.com/IRVMakiAkame0/Aplicacion-Consola-VetCarePro.git
2. Ejecute el archivo principal para iniciar el sistema:
    python main.py

## Autora
- **Isabella Ruiz Velasquez** - Estudiante de Ingeniería de Sistemas (2do Semestre)
- **Institución:** Universidad de Medellín

