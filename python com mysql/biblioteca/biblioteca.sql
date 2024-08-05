-- Criando o banco de dados, se ainda não existir
CREATE DATABASE IF NOT EXISTS biblioteca;

-- Usando o banco de dados biblioteca
USE biblioteca;

-- Tabela para armazenar os livros na biblioteca
CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(100),
    ano_publicacao INT,
    disponivel BOOLEAN DEFAULT TRUE
);

-- Tabela para armazenar os usuários da biblioteca
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

-- Tabela para armazenar as transações de empréstimo/devolução
CREATE TABLE IF NOT EXISTS transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_livro INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_livro) REFERENCES livros(id)
);
