USE escolatech;

SELECT *FROM alunos;

SELECT nome, cidade FROM alunos;

SELECT *FROM cursos;

SELECT  a.nome AS Nomes,
		m.data_matricula
	FROM matriculas m
	JOIN alunos a ON m.id_aluno = a.id_aluno;
    
SELECT *FROM matriculas;

SELECT a.nome, m.data_matricula
FROM matriculas m
JOIN alunos a ON a.id_aluno = m.id_aluno;

SELECT nome,data_matricula 
FROM  matriculas m
JOIN alunos a ON m.id_aluno = a.id_aluno;