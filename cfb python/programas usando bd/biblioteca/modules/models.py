import mysql.connector
from mysql.connector import Error

class Livro:
    def __init__(self, id_livro=None, titulo=None, ano_publicacao=None, id_autor=None, id_categoria=None):
        self.id_livro = id_livro
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.id_autor = id_autor
        self.id_categoria = id_categoria

    def salvar(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            if self.id_livro:
                query = """
                UPDATE livro SET titulo=%s, ano_publicacao=%s, id_autor=%s, id_categoria=%s
                WHERE id_livro=%s
                """
                cursor.execute(query, (self.titulo, self.ano_publicacao, self.id_autor, self.id_categoria, self.id_livro))
            else:
                query = """
                INSERT INTO livro (titulo, ano_publicacao, id_autor, id_categoria)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (self.titulo, self.ano_publicacao, self.id_autor, self.id_categoria))
            conn.commit()
            cursor.close()
            conn.close()

    def excluir(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM livro WHERE id_livro = %s"
            cursor.execute(query, (self.id_livro,))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def buscar(id_livro):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM livro WHERE id_livro = %s"
            cursor.execute(query, (id_livro,))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            if resultado:
                return Livro(*resultado)
            return None

    @staticmethod
    def listar():
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livro")
            livros = cursor.fetchall()
            cursor.close()
            conn.close()
            return [Livro(*livro) for livro in livros]

class Membro:
    def __init__(self, id_membro=None, nome_membro=None, telefone=None, endereco=None):
        self.id_membro = id_membro
        self.nome_membro = nome_membro
        self.telefone = telefone
        self.endereco = endereco

    def salvar(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            if self.id_membro:
                query = """
                UPDATE membro SET nome_membro=%s, telefone=%s, endereco=%s
                WHERE id_membro=%s
                """
                cursor.execute(query, (self.nome_membro, self.telefone, self.endereco, self.id_membro))
            else:
                query = """
                INSERT INTO membro (nome_membro, telefone, endereco)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (self.nome_membro, self.telefone, self.endereco))
            conn.commit()
            cursor.close()
            conn.close()

    def excluir(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM membro WHERE id_membro = %s"
            cursor.execute(query, (self.id_membro,))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def buscar(id_membro):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM membro WHERE id_membro = %s"
            cursor.execute(query, (id_membro,))
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            if resultado:
                return Membro(*resultado)
            return None

    @staticmethod
    def listar():
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM membro")
            membros = cursor.fetchall()
            cursor.close()
            conn.close()
            return [Membro(*membro) for membro in membros]

def conectar():
    config = {
        'user': 'root',
        'password': '',  # Substitua pela sua senha
        'host': '127.0.0.1',
        'database': 'biblioteca_relacional',
        'raise_on_warnings': True
    }
    try:
        conexao = mysql.connector.connect(**config)
        return conexao
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        return None
