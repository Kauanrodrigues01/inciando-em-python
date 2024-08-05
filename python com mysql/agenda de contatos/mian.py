import mysql.connector
import os

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'gerenciador_contatos',
    'raise_on_warnings': True
}

def exibir_menu():
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contatos por nome")
    print("4 - Remover contato")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def conectar():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def adicionar_contato(nome, telefone, email, categoria_id):
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()

            # Adicionar contato à tabela contatos
            comando_sql = "INSERT INTO contatos (nome, telefone, categoria_id) VALUES (%s, %s, %s)"
            cursor.execute(comando_sql, (nome, telefone, categoria_id))
            conn.commit()

            # Obter o ID do contato recém-inserido
            contato_id = cursor.lastrowid

            # Adicionar email à tabela emails
            comando_sql_email = "INSERT INTO emails (contato_id, email) VALUES (%s, %s)"
            cursor.execute(comando_sql_email, (contato_id, email))
            conn.commit()

            print("Contato adicionado com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao adicionar contato: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()

def listar_contatos():
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT c.id, c.nome, c.telefone, e.email, cat.nome as categoria \
                            FROM contatos c \
                            LEFT JOIN emails e ON c.id = e.contato_id \
                            LEFT JOIN categorias cat ON c.categoria_id = cat.id")
            contatos = cursor.fetchall()
            
            if contatos:
                print('Lista de contatos:')
                for contato in contatos:
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Categoria: {contato['categoria']}")
            else:
                print("Nenhum contato encontrado")
    except mysql.connector.Error as e:
        print(f"Erro ao listar contatos: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()
        input("Pressione Enter para continuar...")

# Função para buscar contato por nome
def buscar_contatos_por_nome(nome):
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            sql = "SELECT id, nome, telefone FROM contatos WHERE nome LIKE %s"
            cursor.execute(sql, ('%' + nome + '%',))
            contatos = cursor.fetchall()
            if contatos:
                print("ID\tNome\t\tTelefone")
                print("---------------------------------")
                for contato in contatos:
                    print(f"{contato[0]}\t{contato[1]}\t{contato[2]}")
            else:
                print("Nenhum contato encontrado com esse nome.")
    except mysql.connector.Error as e:
        print(f"Erro ao buscar contatos: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        input("Pressione Enter para continuar...")

# Funções para remover contato
def remover_contato_por_id(id_contato):
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contatos WHERE id = %s", (id_contato,))
            contato = cursor.fetchone()
            if contato:
                sql = "DELETE FROM contatos WHERE id = %s"
                cursor.execute(sql, (id_contato,))
                conn.commit()
                print(f"Contato ID {id_contato} removido com sucesso!")
            else:
                print(f"Contato ID {id_contato} não encontrado.")
    except mysql.connector.Error as e:
        print(f"Erro ao remover contato: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

# Função principal para remoção de contato
def remover_contato():
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM contatos")
            contatos = cursor.fetchall()
            if contatos:
                print("Lista de contatos:")
                print("ID\tNome")
                print("---------------------")
                for contato in contatos:
                    print(f"{contato[0]}\t{contato[1]}")
                id_contato = input("Digite o ID do contato que deseja remover: ")
                remover_contato_por_id(id_contato)
            else:
                print("Nenhum contato encontrado.")
    except mysql.connector.Error as e:
        print(f"Erro ao remover contato: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        input("Pressione Enter para continuar...")

# Função principal
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        opcao = exibir_menu()
        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            categoria_id = input("Digite a categoria(): ")
            adicionar_contato(nome, telefone, email, categoria_id)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja buscar: ")
            buscar_contatos_por_nome(nome)
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == '__main__':
    main()
