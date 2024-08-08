import mysql.connector
from mysql.connector import Error
from colorama import Fore, Back, Style
from .utils import *
from .contato import Contato

config = {
    'user': 'root',
    'password': '',  # Coloque sua senha do MySQL aqui
    'host': '127.0.0.1',
    'database': 'agenda',
    'raise_on_warnings': True
}

def conectar():
    try:
        conexao = mysql.connector.connect(**config)
        return conexao
    except Error as e:
        print(f'{Fore.RED}Erro ao conectar ao MySQL: {e}{Style.RESET_ALL}')
        return None

def inserir_contato(contato):
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        if verificar_nome_valido(contato.nome) and verificar_telefone_valido(contato.telefone) and verificar_email_valido(contato.email):
            query = "INSERT INTO tb_contatos (T_nome, T_telefone, T_email) VALUES (%s, %s, %s)"
            cursor.execute(query, (contato.nome, contato.telefone, contato.email))
            conn.commit()
            print(f'{Fore.GREEN}Contato inserido com sucesso!{Style.RESET_ALL}')
            cursor.close()
            conn.close()
            return True
        else:
            print(f'{Fore.RED}Nome, telefone ou email inválidos!{Style.RESET_ALL}')
            return False
    except Error as e:
        print(f'{Fore.RED}Erro ao inserir contato: {e}{Style.RESET_ALL}')
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def listar_contatos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tb_contatos')
        contatos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        for contato_tuple in contatos:
            contato = Contato.from_tuple(contato_tuple)
            print(contato)
    except Error as e:
        print(f'{Fore.RED}Erro ao listar contatos: {e}{Style.RESET_ALL}')
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def buscar_contato_por_nome(nome):
    conn = None
    cursor = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM tb_contatos WHERE T_nome LIKE %s"
            cursor.execute(query, (f"%{nome}%",))
            contatos_encontrados = cursor.fetchall()
            
            if len(contatos_encontrados) > 0:
                return [Contato.from_tuple(contato) for contato in contatos_encontrados]
            else:
                print(f'{Fore.RED}Nenhum contato encontrado!{Style.RESET_ALL}')
                return None
        else:
            print(f'{Fore.RED}Não foi possível conectar ao banco de dados.{Style.RESET_ALL}')
            return None
    except Error as e:
        print(f'{Fore.RED}Erro ao buscar contato: {e}{Style.RESET_ALL}')
        return None
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def alterar_contato(contato, contatos_encontrados):
    conn = None
    cursor = None
    try:
        if contatos_encontrados is not None:
            if verificar_nome_valido(contato.nome) and verificar_telefone_valido(contato.telefone) and verificar_email_valido(contato.email) and verificar_id_valido(contato.id):
                conn = conectar()
                if conn:
                    cursor = conn.cursor()
                    query = """
                        UPDATE tb_contatos
                        SET T_nome = %s, T_telefone = %s, T_email = %s
                        WHERE N_id = %s
                    """
                    cursor.execute(query, (contato.nome, contato.telefone, contato.email, contato.id))
                    conn.commit()
                    print(f'{Fore.GREEN}Contato alterado com sucesso!{Style.RESET_ALL}')
                    return True
                else:
                    print(f'{Fore.RED}Não foi possível conectar ao banco de dados.{Style.RESET_ALL}')
                    return False
            else:
                print(f'{Fore.RED}Nome, telefone ou email inválidos!{Style.RESET_ALL}')
                return False
        else:
            print(f'{Fore.RED}Contato não encontrado!{Style.RESET_ALL}')
            return False
    except Error as e:
        print(f'{Fore.RED}Erro ao alterar contato: {e}{Style.RESET_ALL}')
        return False
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def excluir_contato(id, contatos_encontrados):
    conn = None
    cursor = None
    try:
        if contatos_encontrados is not None:
            conn = conectar()
            if conn:
                if not verificar_id_valido(id):
                    print(f'{Fore.RED}ID inválido!{Style.RESET_ALL}')
                    return False
                cursor = conn.cursor()
                query = "DELETE FROM tb_contatos WHERE N_id = %s"
                cursor.execute(query, (id,))
                conn.commit()
                print(f'{Fore.GREEN}Contato excluído com sucesso!{Style.RESET_ALL}')
                return True
            else:
                print(f'{Fore.RED}Não foi possível conectar ao banco de dados.{Style.RESET_ALL}')
                return False
        else:
            print(f'{Fore.RED}Contato não encontrado!{Style.RESET_ALL}')
            return False
    except Error as e:
        print(f'{Fore.RED}Erro ao excluir contato: {e}{Style.RESET_ALL}')
        return False
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            
def exibir_contatos_encontrados(contatos):
    for contato in contatos:
        print(contato)