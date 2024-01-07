CREATE DATABASE juncao;

USE juncao;

CREATE TABLE profissoes(
	id INT NOT NULL AUTO_INCREMENT,
	cargo VARCHAR(60) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE clientes(
	id INT NOT NULL AUTO_INCREMENT, 
	nome VARCHAR(60) NOT NULL,
	data_nascimento DATE NOT NULL,
	telefone VARCHAR(10) NOT NULL,
	id_profissao int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id_profissao) REFERENCES profissoes(id)
);


INSERT INTO profissoes (cargo) VALUES ('Programador');
INSERT INTO profissoes (cargo) VALUES ('Analista de Sistemas');
INSERT INTO profissoes (cargo) VALUES ('Suporte');
INSERT INTO profissoes (cargo) VALUES ('Gerente');

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('João Pereira', '1981-06-15', '1234-5688', 1);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Ricardo da Silva', '1973-10-10', '2234-5669', 2);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Felipe Oliveira', '1987-08-01', '4234-5640', 3);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Mário Pirez', '1991-02-05', '5234-5621', 1);


SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo 
	FROM clientes AS c, profissoes AS p
    WHERE c.id_profissao = p.id;


-- Inner Join
SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo
FROM clientes AS c INNER JOIN profissoes AS p
ON  c.id_profissao = p.id;

-- Left Outer Join
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Right Outer Join
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join (Não funciona no MySQL)
SELECT * FROM clientes
FULL OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join (Versão MySQL)
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id
UNION
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;


-- Cross Join
SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo
FROM clientes AS c
CROSS JOIN profissoes AS p;