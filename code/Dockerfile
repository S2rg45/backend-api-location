# Usa una imagen base de Python
FROM python:3.12-slim

# Configura el directorio de trabajo
WORKDIR /app

# Instala Poetry
RUN pip install poetry

# Copia el archivo de configuración de Poetry
COPY pyproject.toml poetry.lock /app/

# Instala las dependencias del proyecto usando Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copia el código de la aplicación
COPY app /app/app

# Expone el puerto de FastAPI
EXPOSE 8000

# Comando para iniciar Uvicorn y Celery al iniciar el contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]