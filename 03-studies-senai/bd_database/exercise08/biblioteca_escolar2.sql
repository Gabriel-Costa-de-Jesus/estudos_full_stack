CREATE DATABASE IF NOT EXISTS biblioteca_escolar2;
USE biblioteca_escolar2;

CREATE TABLE autores(
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome_autor VARCHAR(50) NOT NULL
    );

CREATE TABLE livros(
	id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL,
    ano_publicacao INT NOT NULL,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
    );

CREATE TABLE emprestimos(
	id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_livro INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON UPDATE CASCADE ON DELETE CASCADE
    );
    
ALTER TABLE livros ADD COLUMN genero VARCHAR(50);
ALTER TABLE usuarios ADD COLUMN telefone VARCHAR(50);

ALTER TABLE autores CHANGE nome_autor autor_nome VARCHAR(50);
ALTER TABLE livros CHANGE titulo titulo_livro VARCHAR(50);

INSERT INTO autores(autor_nome) VALUE ('Machado de Assis');
INSERT INTO livros(titulo_livro, ano_publicacao, id_autor) VALUE ('Dom Casmurro', '2025-10-23', 1);
INSERT INTO usuarios(nome_usuario, email) VALUE ('João Silva', 'joão@email.com');
INSERT INTO emprestimos(id_usuario, id_livro, data_emprestimo) VALUE (1,1, '2025-10-23');

SELECT data_devolucao FROM emprestimos;

UPDATE usuarios
	SET nome_usuario = 'joãosilva@email.com'
    WHERE id_usuario = 1;
    
-- DELETE FROM livros WHERE id_autor = 1;
DELETE FROM autores WHERE id_autor = 1;
DELETE FROM emprestimos WHERE data_devolucao < '2023-01-01';

CREATE TABLE categorias(
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(50)
    );
    
ALTER TABLE livros ADD COLUMN id_categoria INT;

ALTER TABLE livros 
ADD CONSTRAINT fk_livros_categoria
FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria);

 -- DROP DATABASE biblioteca_escolar2;
