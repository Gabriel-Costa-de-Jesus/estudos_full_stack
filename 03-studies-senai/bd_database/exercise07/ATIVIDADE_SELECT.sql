-- Criação do banco
CREATE DATABASE EscolaTech;
USE EscolaTech;

-- Tabela de alunos
CREATE TABLE alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50),
    idade INT,
    genero CHAR(1)
);

-- Tabela de cursos
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    area VARCHAR(50),
    carga_horaria INT,
    valor DECIMAL(10,2)
);

-- Tabela de professores
CREATE TABLE professores (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    especialidade VARCHAR(50),
    cidade VARCHAR(50)
);

-- Tabela de matrículas
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    id_curso INT,
    id_professor INT,
    data_matricula DATE,
    nota_final DECIMAL(5,2),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
    FOREIGN KEY (id_professor) REFERENCES professores(id_professor)
);

-- Inserindo alunos
INSERT INTO alunos (nome, cidade, idade, genero) VALUES
('Ana Lima', 'São Paulo', 20, 'F'),
('Bruno Costa', 'Rio de Janeiro', 23, 'M'),
('Carla Souza', 'Curitiba', 19, 'F'),
('Diego Nunes', 'Belo Horizonte', 25, 'M'),
('Elisa Rocha', 'Salvador', 22, 'F'),
('Fernando Alves', 'Porto Alegre', 24, 'M'),
('Gabriela Teles', 'Fortaleza', 21, 'F'),
('Henrique Dias', 'Recife', 26, 'M'),
('Isabela Martins', 'Natal', 20, 'F'),
('João Pedro', 'Manaus', 27, 'M');

-- Inserindo cursos
INSERT INTO cursos (nome, area, carga_horaria, valor) VALUES
('Banco de Dados', 'Tecnologia', 60, 800.00),
('Programação Web', 'Tecnologia', 80, 1000.00),
('Redes de Computadores', 'Tecnologia', 70, 950.00),
('Design Gráfico', 'Artes', 50, 750.00),
('Excel Avançado', 'Gestão', 40, 600.00),
('Segurança da Informação', 'Tecnologia', 90, 1200.00),
('Marketing Digital', 'Gestão', 60, 850.00),
('Fotografia Digital', 'Artes', 45, 700.00),
('Desenvolvimento Mobile', 'Tecnologia', 100, 1300.00),
('Edição de Vídeo', 'Artes', 55, 800.00);

-- Inserindo professores
INSERT INTO professores (nome, especialidade, cidade) VALUES
('Carlos Pereira', 'Banco de Dados', 'São Paulo'),
('Fernanda Souza', 'Programação', 'Rio de Janeiro'),
('Rafael Lima', 'Redes', 'Curitiba'),
('Mariana Costa', 'Design', 'Recife'),
('André Silva', 'Gestão', 'Salvador'),
('Paula Mendes', 'Segurança', 'Fortaleza'),
('Ricardo Alves', 'Marketing', 'São Paulo'),
('Joana Rocha', 'Fotografia', 'Belo Horizonte'),
('Tiago Santos', 'Mobile', 'Manaus'),
('Luciana Ribeiro', 'Edição', 'Porto Alegre');

-- Inserindo matrículas
INSERT INTO matriculas (id_aluno, id_curso, id_professor, data_matricula, nota_final) VALUES
(1, 1, 1, '2024-01-15', 8.5),
(2, 2, 2, '2024-02-10', 7.0),
(3, 3, 3, '2024-02-25', 9.0),
(4, 4, 4, '2024-03-05', 8.0),
(5, 5, 5, '2024-03-20', 7.5),
(6, 6, 6, '2024-04-12', 9.5),
(7, 7, 7, '2024-05-01', 8.0),
(8, 8, 8, '2024-06-18', 7.0),
(9, 9, 9, '2024-07-05', 9.0),
(10, 10, 10, '2024-07-25', 8.5),
(1, 2, 2, '2024-08-02', 9.0),
(2, 3, 3, '2024-08-15', 8.0),
(3, 1, 1, '2024-09-10', 7.5),
(4, 5, 5, '2024-09-18', 8.0),
(5, 7, 7, '2024-10-02', 9.5),
(6, 9, 9, '2024-10-15', 8.0),
(7, 6, 6, '2024-11-05', 8.5),
(8, 4, 4, '2024-11-12', 7.5),
(9, 8, 8, '2024-12-01', 9.0),
(10, 10, 10, '2024-12-10', 8.5);
