# Usa una imagen base de Python
FROM python:3-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . /app/

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación (asegúrate de que `app.py` sea el archivo correcto)
CMD ["flask", "run", "--host=0.0.0.0"]
