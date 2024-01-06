CREATE DATABASE secao04;

USE secao04;

CREATE TABLE tipos_produtos(
	codigo INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(30) NOT NULL,
    PRIMARY KEY(codigo)
    );

CREATE TABLE produtos(
	codigo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(30) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    codigo_tipo INT NOT NULL,
    FOREIGN KEY(codigo_tipo) REFERENCES tipos_produtos(codigo)
    
);


insert into tipos_produtos (descricao) values ('Computadores');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressoras');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200.00', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', '1800.00', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Jato de Tinta', '300', 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Laser ', '499.99', 2);

select * from produtos;

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Notebook', '1500.99', 1);

