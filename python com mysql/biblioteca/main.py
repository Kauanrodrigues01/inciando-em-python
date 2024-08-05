import mysql.connector
from datetime import date

# Configuração da conexão com o banco de dados MySQL
config = {
    'user': 'root',
    'password': '',  # Coloque sua senha do MySQL aqui
    'host': '127.0.0.1',
    'database': 'biblioteca',
    'raise_on_warnings': True
}

# Função para conectar ao banco de dados
def conectar():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Classe para representar um Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def salvar(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            sql = "INSERT INTO livros (titulo, autor, ano_publicacao, disponivel) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.titulo, self.autor, self.ano_publicacao, self.disponivel))
            conn.commit()
            print("Livro adicionado com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao adicionar livro: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livros")
            livros = cursor.fetchall()
            if livros:
                print('Lista de livros:')
                for livro in livros:
                    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano de Publicação: {livro[3]}, Disponível: {'Sim' if livro[4] else 'Não'}")
            else:
                print("Nenhum livro encontrado")
        except mysql.connector.Error as e:
            print(f"Erro ao listar livros: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

# Classe para representar um Usuário
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def salvar(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
            cursor.execute(sql, (self.nome, self.email))
            conn.commit()
            print("Usuário adicionado com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao adicionar usuário: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def listar():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            if usuarios:
                print('Lista de usuários:')
                for usuario in usuarios:
                    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
            else:
                print("Nenhum usuário encontrado")
        except mysql.connector.Error as e:
            print(f"Erro ao listar usuários: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

# Classe para representar uma Transação (Empréstimo/Devolução)
class Transacao:
    def __init__(self, id_usuario, id_livro, data_emprestimo=None, data_devolucao=None):
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def emprestar(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            self.data_emprestimo = date.today()
            sql = "INSERT INTO transacoes (id_usuario, id_livro, data_emprestimo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (self.id_usuario, self.id_livro, self.data_emprestimo))
            conn.commit()
            # Atualiza disponibilidade do livro para False (não disponível)
            cursor.execute("UPDATE livros SET disponivel = FALSE WHERE id = %s", (self.id_livro,))
            conn.commit()
            print("Livro emprestado com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao realizar empréstimo: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def devolver(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            self.data_devolucao = date.today()
            sql = "UPDATE transacoes SET data_devolucao = %s WHERE id_usuario = %s AND id_livro = %s AND data_devolucao IS NULL"
            cursor.execute(sql, (self.data_devolucao, self.id_usuario, self.id_livro))
            conn.commit()
            # Atualiza disponibilidade do livro para True (disponível)
            cursor.execute("UPDATE livros SET disponivel = TRUE WHERE id = %s", (self.id_livro,))
            conn.commit()
            print("Livro devolvido com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao realizar devolução: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

# Função para exibir o menu
def exibir_menu():
    print("\n1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Adicionar usuário")
    print("4 - Listar usuários")
    print("5 - Emprestar livro")
    print("6 - Devolver livro")
    print("7 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função principal
def main():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")
            livro = Livro(titulo, autor, int(ano_publicacao))
            livro.salvar()
        elif opcao == '2':
            Livro.listar()
        elif opcao == '3':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            usuario = Usuario(nome, email)
            usuario.salvar()
        elif opcao == '4':
            Usuario.listar()
        elif opcao == '5':
            id_usuario = input("Digite o ID do usuário: ")
            id_livro = input("Digite o ID do livro: ")
            transacao = Transacao(int(id_usuario), int(id_livro))
            transacao.emprestar()
        elif opcao == '6':
            id_usuario = input("Digite o ID do usuário: ")
            id_livro = input("Digite o ID do livro: ")
            transacao = Transacao(int(id_usuario), int(id_livro))
            transacao.devolver()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == '__main__':
    main()