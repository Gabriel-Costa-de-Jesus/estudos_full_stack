create database loja;

USE loja;

CREATE TABLE clientes (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
    );

CREATE TABLE produtos (
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
    );

CREATE TABLE compras (
	id_compra INT AUTO_INCREMENT PRIMARY KEY,
    data_compra DATE NOT NULL,
    forma_pgto VARCHAR(50) NOT NULL,
    qtd INT NOT NULL,
    id_cliente_compra INT,
    id_produto_compra INT,
    FOREIGN KEY (id_cliente_compra) REFERENCES clientes(id_cliente) ON UPDATE CASCADE,
    FOREIGN KEY (id_produto_compra) REFERENCES produtos(id_produto) ON UPDATE CASCADE
    );
    
    INSERT INTO clientes(nome) VALUES 
	('Maria'),
    ('Fernando'),
    ('Matheus');
    
    INSERT INTO produtos(descricao, preco) VALUES
    ('Arroz', 6.99),
    ('Feijão', 9.99),
    ('Batata', 0.30),
    ('Pepino', 0.50);   
    
    INSERT INTO compras(data_compra, forma_pgto, qtd, id_cliente_compra, id_produto_compra) VALUES
    ('2025-10-01', 'Cartão', 50, 2, 1),
	('2025-10-01', 'Cartão', 50, 2, 2),
	('2025-10-09', 'Pix', 2, 1, 1),
	('2025-10-09', 'Pix', 2, 1, 2),
	('2025-09-20', 'Dinheiro', 1, 3, 4);
    
    SELECT  cl.nome as Cliente,
			cp.forma_pgto,
            cp.data_compra,
            p.descricao as Produto,
            p.preco
	FROM compras cp -- É da tabela que tem a chave estrangeira
    INNER JOIN clientes cl ON cl.id_cliente = cp.id_cliente_compra -- Coloca o nome da tabela, cadastra o apelido cl dps faz o relacionamento com chave estrangeira
    INNER JOIN produtos p ON p.id_produto = cp.id_produto_compra; -- RT
    
    