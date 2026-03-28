# Aplicacion-Consola-VetCarePro
Sistema de Gestión Veterinaria y Dosificación Farmacológica

## Descripción del proyecto
Este software es una solución orientada a objetos desarrollada en python para la administración de pacientes y control de inventario en una clínica veterinaria. El sistema pone especial énfasis en la seguridad clínica, automatizando el cálculo de dosis y estableciendo restricciones de seguridad basadas en la compatibilidad biológica entre especies/razas y componentes químicos.

## Funcionalidades Implementadas
- Gestión de pacientes: Registro detallado que incluye especie y raza para precision diagnostica.
- Gestión de entidades mediante diccionarios: Uso de estructuras tipo dict para busquedas eficientes de pacientes y medicamentos.
- Calculo de dosificacion automatica: Determinación de mg requeridos segun el peso del animal.
- Validacion de toxicidad: Bloqueo de recetas para medicamentos contraindicados por especie.
- Reportes tabulares: Visualización tecnica de datos mediante la libreria Tabulate.
