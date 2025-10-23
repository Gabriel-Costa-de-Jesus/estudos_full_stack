CREATE DATABASE IF NOT EXISTS biblioteca_escolar2;
USE biblioteca_escolar2;

CREATE TABLE autores(
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome_autor VARCHAR(50) NOT NULL
    );

CREATE TABLE Livros(
	id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL,
    ano_publicacao INT NOT NULL,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) ON UPDATE CASCADE
    );
    