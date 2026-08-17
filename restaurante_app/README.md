# restaurante_app - Semana 9

Estudiante: Solange Naomi Velez Cortaza  
Universidad: Universidad Estatal Amazónica  
Proyecto: restaurante_app  
Actividad: Semana 9

## Descripción

El proyecto restaurante_app es un sistema desarrollado en Python para administrar
información básica de un restaurante mediante una aplicación de consola.

El sistema permite registrar, buscar, actualizar, eliminar y listar productos,
además de registrar y listar usuarios. La aplicación mantiene una separación
entre los modelos, los servicios y el archivo principal.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md