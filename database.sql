CREATE DATABASE IF NOT EXISTS Confesionario; 

USE Confesionario; 

CREATE TABLE IF NOT EXISTS Usuarios (
    nombre VARCHAR(50) NOT NULL,
    contrasena VARCHAR(100),
    PRIMARY KEY (nombre)
);


CREATE TABLE IF NOT EXISTS Confesiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    texto TEXT
);

    