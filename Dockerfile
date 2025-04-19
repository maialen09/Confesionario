# Usa una imagen base ligera con Python
FROM python:3-alpine

# Instala dependencias necesarias para Flask y el reloader
RUN apk add --no-cache build-base libffi-dev

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo el requirements.txt (para aprovechar la cache de Docker)
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de Flask
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Ejecuta la app con recarga activada
CMD ["flask", "run", "--host=0.0.0.0", "--reload", "--debugger"]