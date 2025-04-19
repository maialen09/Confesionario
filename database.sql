CREATE DATABASE IF NOT EXISTS Confesionario; 

USE Confesionario; 

CREATE TABLE IF NOT EXISTS Usuarios (
    nombre VARCHAR(50) NOT NULL,
    contrasena VARCHAR(100),
    PRIMARY KEY (nombre)
);


CREATE TABLE IF NOT EXISTS Confesiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(70),
    usuario VARCHAR(100),
    texto TEXT, 
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_confesion INT,
    usuario VARCHAR(100),
    texto TEXT,
    likes INT DEFAULT 0
); 

    