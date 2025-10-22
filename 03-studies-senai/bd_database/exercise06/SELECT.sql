-- Criação do banco de dados
CREATE DATABASE LojaSmart;
USE LojaSmart;

-- Tabela de clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50),
    idade INT,
    genero CHAR(1)
);

-- Tabela de produtos
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    estoque INT
);

-- Tabela de vendas
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    data_venda DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Inserindo clientes
INSERT INTO clientes (nome, cidade, idade, genero) VALUES
('Ana Souza', 'São Paulo', 25, 'F'),
('Bruno Lima', 'Rio de Janeiro', 30, 'M'),
('Carlos Mendes', 'Belo Horizonte', 40, 'M'),
('Daniela Alves', 'Curitiba', 22, 'F'),
('Eduardo Silva', 'São Paulo', 35, 'M'),
('Fernanda Costa', 'Recife', 28, 'F'),
('Gabriel Rocha', 'Porto Alegre', 45, 'M'),
('Helena Castro', 'Fortaleza', 33, 'F'),
('Igor Santos', 'São Paulo', 19, 'M'),
('Julia Mendes', 'Salvador', 26, 'F');

-- Inserindo produtos
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Notebook Dell', 'Informática', 4500.00, 10),
('Mouse Logitech', 'Informática', 120.00, 50),
('Teclado Mecânico', 'Informática', 350.00, 30),
('Monitor LG', 'Informática', 950.00, 20),
('Smartphone Samsung', 'Telefonia', 2500.00, 15),
('Capa Celular', 'Acessórios', 50.00, 100),
('Fone Bluetooth', 'Acessórios', 300.00, 40),
('Impressora HP', 'Periféricos', 800.00, 8),
('Cabo HDMI', 'Acessórios', 40.00, 70),
('Tablet Lenovo', 'Informática', 1800.00, 12);

-- Inserindo vendas
INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES
(1, 1, 1, '2024-01-10'),
(2, 2, 2, '2024-02-05'),
(3, 5, 1, '2024-02-10'),
(4, 3, 1, '2024-03-01'),
(5, 6, 3, '2024-03-15'),
(6, 7, 2, '2024-04-05'),
(7, 8, 1, '2024-04-12'),
(8, 9, 4, '2024-05-01'),
(9, 10, 1, '2024-06-02'),
(10, 4, 2, '2024-06-10'),
(1, 5, 1, '2024-06-20'),
(2, 7, 1, '2024-07-05'),
(3, 2, 3, '2024-07-15'),
(4, 6, 2, '2024-08-01'),
(5, 9, 5, '2024-08-10'),
(6, 10, 1, '2024-09-05'),
(7, 1, 2, '2024-09-10'),
(8, 3, 1, '2024-09-15'),
(9, 4, 3, '2024-09-20'),
(10, 8, 1, '2024-09-25');
