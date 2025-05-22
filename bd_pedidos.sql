CREATE DATABASE IF NOT EXISTS db_produtos
DEFAULT CHARSET = utf8
DEFAULT COLlATE = utf8_general_ci;

USE db_produtos;

CREATE TABLE tbl_pedidos(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
codigo INT,
descricao VARCHAR(50),
preco DOUBLE,
categoria VARCHAR(20)
);

SELECT * FROM tbl_pedidos;
TRUNCATE tbl_pedidos;
