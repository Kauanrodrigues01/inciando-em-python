-- Criando o banco de dados, se ainda não existir
CREATE DATABASE IF NOT EXISTS gerenciador_contatos;

-- Usando o banco de dados gerenciador_contatos
USE gerenciador_contatos;

-- Tabela para categorias dos contatos
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Tabela para armazenar os contatos
CREATE TABLE IF NOT EXISTS contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabela para armazenar os emails dos contatos
CREATE TABLE IF NOT EXISTS emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contato_id INT,
    email VARCHAR(100) NOT NULL,
    FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Exemplo de inserção de categorias iniciais (opcional)
INSERT INTO categorias (nome) VALUES ('Amigos'), ('Família'), ('Trabalho');

-- Exemplo de inserção de contatos (opcional)
-- INSERT INTO contatos (nome, telefone, categoria_id) VALUES ('Fulano', '9999-9999', 1);
-- INSERT INTO contatos (nome, telefone, categoria_id) VALUES ('Ciclano', '8888-8888', 2);
-- INSERT INTO contatos (nome, telefone, categoria_id) VALUES ('Beltrano', '7777-7777', 3);

-- Exemplo de inserção de emails dos contatos (opcional)
-- INSERT INTO emails (contato_id, email) VALUES (1, 'fulano@example.com');
-- INSERT INTO emails (contato_id, email) VALUES (1, 'fulano@gmail.com');
-- INSERT INTO emails (contato_id, email) VALUES (2, 'ciclano@example.com');

-- Exemplo de consulta para listar contatos com seus emails e categorias
-- SELECT c.id, c.nome, c.telefone, e.email, cat.nome as categoria
-- FROM contatos c
-- LEFT JOIN emails e ON c.id = e.contato_id
-- LEFT JOIN categorias cat ON c.categoria_id = cat.id;

