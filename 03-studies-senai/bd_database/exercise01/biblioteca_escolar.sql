-- Cria o banco de Dados
create database biblioteca_escolar;

-- Habilita o banco de dados;

use biblioteca_escolar;

-- Passo 2 - Criar a tabela alunos
CREATE TABLE alunos (
	id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    turma VARCHAR(50)
    );

-- Passo 3 - Criar tabela emprestimos
CREATE TABLE emprestimos (
	id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    data_emprestimo DATE NOT NULL,
    id_aluno INT,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno) ON UPDATE CASCADE
    );
    
-- Inserindo Dados
INSERT INTO alunos (nome, turma) VALUES
('Maria Silva', '1A'),
('João Souza', '2B'),
('Ana Pereira', '3C');

INSERT INTO emprestimos(data_emprestimo, id_aluno) VALUES
	('2025-09-01', 1),
    ('2025-09-03',2),
    ('2025-09-05', 3),
    ('2025-09-05',2);
    
SELECT * FROM emprestimos;
SELECT *FROM alunos;

-- Unindo Tabelas

SELECT e.id_emprestimo,
		e.data_emprestimo,
        a.nome,
        a.turma
FROM emprestimos e
INNER JOIN alunos a ON e.id_aluno = a.id_aluno;

SELECT e.data_emprestimo,
		a.nome as alunos,
        a.turma
FROM emprestimos e
INNER JOIN alunos a ON e.id_aluno = a.id_aluno;

select emprestimos.id_aluno, nome, data_emprestimo from alunos, emprestimos;

    