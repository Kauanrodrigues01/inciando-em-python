CREATE DATABASE biblioteca_relacional CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca_relacional;

CREATE TABLE autor (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    categoria VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE livro (
    id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL,
    ano_publicacao YEAR NOT NULL,
    id_autor INT NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
    ON UPDATE CASCADE
    ON DELETE SET NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE membro (
    id_membro INT AUTO_INCREMENT PRIMARY KEY,
    nome_membro VARCHAR(50) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    endereco VARCHAR(30) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_livro INT NOT NULL,
    id_membro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE DEFAULT NULL,
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (id_membro) REFERENCES membro(id_membro)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
