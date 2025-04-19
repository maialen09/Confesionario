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
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario) REFERENCES Usuarios(nombre)
);

CREATE TABLE IF NOT EXISTS Comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_confesion INT,
    usuario VARCHAR(50),
    texto TEXT,
    FOREIGN KEY (id_confesion) REFERENCES Confesiones(id)
);

CREATE TABLE IF NOT EXISTS Likes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    comentario_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT NOW(),
    UNIQUE(usuario, comentario_id), 
    FOREIGN KEY (usuario) REFERENCES Usuarios(nombre),
    FOREIGN KEY (comentario_id) REFERENCES Comentarios(id)
);  