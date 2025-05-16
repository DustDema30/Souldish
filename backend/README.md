# SoulDish - API para Gestión de Recetas por Estado de Ánimo

**SoulDish** es una API REST desarrollada en Python con el framework FastAPI. El sistema permite registrar, consultar, actualizar y eliminar recetas culinarias asociadas a distintos estados de ánimo. Este proyecto forma parte del proceso de formación en el SENA y está diseñado con tecnologías modernas y escalables.

## Descripción

El objetivo principal de SoulDish es proporcionar una base estructurada para una futura aplicación web y móvil que sugiera recetas personalizadas según el estado emocional del usuario.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- PostgreSQL (a través de Supabase)
- SQLAlchemy
- Git y GitHub para control de versiones

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/DustDema30/Souldish.git
cd Souldish/backend

2. Crear y activar el entorno virtual:
python -m venv env
source env/Scripts/activate  # Windows

3. Instalar dependencias:
pip install fastapi sqlalchemy psycopg2 uvicorn

4. Ejecutar el servidor:
uvicorn main:app --reload

      Endpoints disponibles:

Método	Ruta	Descripción
GET	/	Verifica el estado del servidor
POST	/recetas	Crea una nueva receta
GET	/recetas	Lista todas las recetas
PUT	/recetas/{id}	Actualiza una receta existente
DELETE	/recetas/{id}	Elimina una receta existente

Autor:
Jorge Humberto Gómez Libreros
Tecnología en Análisis y Desarrollo de Software – SENA
Repositorio: https://github.com/DustDema30/Souldish
