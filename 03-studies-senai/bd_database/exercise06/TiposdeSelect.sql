USE LojaSmart;

-- Listar todos os clientes (Select Simples)
SELECT * FROM clientes;

-- Selecionar apenas o que eu quero, específico
SELECT nome, cidade FROM clientes;

-- Selecionar apenas os nomes dos produtos e preços
SELECT nome, preco FROM produtos;

-- Selecionar todos os produtos da categoria acessorios
SELECT *FROM produtos WHERE categoria = 'Acessórios';

-- Listar todos os clientes que moram em São Paulo.alter
SELECT nome, cidade FROM clientes WHERE cidade = 'São Paulo';

-- Operadores comuns do Banco de dados Or and not, Selecioonar produtos acima de 1000
SELECT nome,preco FROM profutos WHERE preco > 1000;

-- Listar todas as vendas do mes 6 e do ano 2024
SELECT * FROM vendas WHERE MONTH(data_venda) = 6 AND YEAR = 2024; 

-- Listar as cidades distintias dos clientes
SELECT DISTINCT cidade FROM clientes;

-- Mostrar os produtos em ordem do maior para o menor
SELECT nome FROM produtos ORDER BY nome ASC;

-- Mostrar os produtos em ordem do menor para o maior
SELECT nome FROM produtos ORDER BY nome DESC;

-- Mostrar os produtos nome e preco em ordem asc
SELECT nome, preco FROM produtos ORDER BY nome AND preco ASC;

-- Exiba nome, estoque

-- Exiba o nome dos produtos com estoque menor que 20
SELECT nome, estoque FROM produtos WHERE estoque < 20;

-- Mostre o nome dos clientes com idade entre 25 e 35 anos
SELECT nome, idade FROM clientes WHERE idade BETWEEN 25 AND 35;
-- Outra forma lá que descobrir
SELECT nome, idade FROM clientes WHERE idade >= 25 AND idade <= 35;

SELECT nome, preco FROM produtos WHERE categoria = 'Informática' AND preco < 2000;

-- Mostrar as 5 primeiras vendas registradas
SELECT * FROM vendas LIMIT 5;

-- Contar quantos produtos tem
SELECT COUNT(*) AS total_produtos FROM PRODUTOS;

-- Tirar a média de idade
SELECT AVG(idade) AS media_idade FROM clientes; -- Colocar o nome na coluna, apelido

-- Mostre o produto mais caro
SELECT nome, preco FROM produtos
ORDER BY preco DESC LIMIT 1;

-- Mostre o produto mais barato
SELECT nome, preco FROM produtos
ORDER BY preco ASC LIMIT 1;

SELECT categoria , COUNT(*) AS total
FROM produtos GROUP BY categoria;

-- Liste o nome do cliente e o nome do produto em cada venda
SELECT c.nome AS cliente, p.nome AS produto
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN produtos p ON v.id_produto = p.id_produto;

-- Mostre  o nome do cliente, produto e quantidade das vendas, feitas em julho de 2024
