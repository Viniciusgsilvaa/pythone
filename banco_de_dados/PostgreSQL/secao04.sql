-- CREATE DATA BASE secao04;

-- CREATE TABLE tipos_produtos(
--	id SERIAL PRIMARY KEY,
--	descricao VARCHAR(30) NOT NULL	
-- );

-- CREATE TABLE produtos(
--	id SERIAL PRIMARY KEY,
--	descricao VARCHAR(30) NOT NULL,
--	preco MONEY NOT NULL,
--	codigo_tipo INT REFERENCES tipos_produtos(id) NOT NULL
-- );

-- INSERT INTO tipos_produtos (descricao) VALUES ('Computador');
-- INSERT INTO tipos_produtos (descricao) VALUES ('Impressora');

-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200', 1);
-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', '1800', 1);
-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Jato Tinta', '300', 2);
-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Laser', '500', 2);

-- Select
-- SELECT * FROM tipos_produtos;

-- SELECT id, descricao FROM tipos_produtos;

-- SELECT * FROM produtos;

-- SELECT id, descricao, codigo_tipo FROM produtos;

-- Erro Select
-- SELECT id, descricao, preco, codigo_tipo FROM produtos;

-- Alias 
-- SELECT p.id AS cod, p.descricao AS descr, p.preco AS pre, p.codigo_tipo AS ctp FROM produtos AS p;

-- INSERT INTO tipos_produtos (descricao) VALUES ('vidiu gamy');

-- UPDATE tipos_produtos SET descricao = 'Video Game' WHERE id = 3;

-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Nintendo Switch', 350, 3)

-- INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('PS5', 650, 3);

-- DElETE FROM produtos Where id = 6;

-- UPDATE produtos SET id = 6 where id = 9;

-- INSERT INTO produtos (id, descricao, preco, codigo_tipo) VALUES (7, 'Xbox X', 550, 3);

SELECT * FROM produtos;