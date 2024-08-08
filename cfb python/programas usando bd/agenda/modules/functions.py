import mysql.connector
from mysql.connector import Error
from colorama import Fore, Back, Style
from .utils import *

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

def fechar_conexao(conn, cursor):
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()

def inserir_contato(nome, telefone, email):
    conn = None
    cursor = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            if verificar_nome_valido(nome) and verificar_telefone_valido(telefone) and verificar_email_valido(email):
                query = "INSERT INTO tb_contatos (T_nome, T_telefone, T_email) VALUES (%s, %s, %s)"
                cursor.execute(query, (nome, telefone, email))
                conn.commit()
                print(f'{Fore.GREEN}Contato inserido com sucesso!{Style.RESET_ALL}')
                return True
            else:
                print(f'{Fore.RED}Nome, telefone ou email inválidos!{Style.RESET_ALL}')
                return False
    except Error as e:
        print(f'{Fore.RED}Erro ao inserir contato: {e}{Style.RESET_ALL}')
    finally:
        fechar_conexao(conn, cursor)

def listar_contatos():
    conn = None
    cursor = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tb_contatos')
            contatos = cursor.fetchall()
            if len(contatos) == 0:
                print(f'{Fore.RED}Nenhum contato cadastrado!{Style.RESET_ALL}')
            else:
                for contato in contatos:
                    print(f'{Fore.CYAN}Nome:{Style.RESET_ALL} {contato[1]:<20} | {Fore.CYAN}Telefone:{Style.RESET_ALL} {contato[2]:<15} | {Fore.CYAN}Email:{Style.RESET_ALL} {contato[3]}')
    except Error as e:
        print(f'{Fore.RED}Erro ao listar contatos: {e}{Style.RESET_ALL}')
    finally:
        fechar_conexao(conn, cursor)

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
            if contatos_encontrados:
                return contatos_encontrados
            else:
                print(f'{Fore.RED}Nenhum contato encontrado!{Style.RESET_ALL}')
                return None
    except Error as e:
        print(f'{Fore.RED}Erro ao buscar contato: {e}{Style.RESET_ALL}')
        return None
    finally:
        fechar_conexao(conn, cursor)

def alterar_contato(id, nome, telefone, email, contatos_encontrados):
    conn = None
    cursor = None
    try:
        if contatos_encontrados and verificar_nome_valido(nome) and verificar_telefone_valido(telefone) and verificar_email_valido(email) and verificar_id_valido(id):
            conn = conectar()
            if conn:
                cursor = conn.cursor()
                query = "UPDATE tb_contatos SET T_nome = %s, T_telefone = %s, T_email = %s WHERE N_id = %s"
                cursor.execute(query, (nome, telefone, email, id))
                conn.commit()
                print(f'{Fore.GREEN}Contato alterado com sucesso!{Style.RESET_ALL}')
                return True
    except Error as e:
        print(f'{Fore.RED}Erro ao alterar contato: {e}{Style.RESET_ALL}')
        return False
    finally:
        fechar_conexao(conn, cursor)

def excluir_contato(id, contatos_encontrados):
    conn = None
    cursor = None
    try:
        if contatos_encontrados and verificar_id_valido(id):
            conn = conectar()
            if conn:
                cursor = conn.cursor()
                query = "DELETE FROM tb_contatos WHERE N_id = %s"
                cursor.execute(query, (id,))
                conn.commit()
                print(f'{Fore.GREEN}Contato excluído com sucesso!{Style.RESET_ALL}')
                return True
    except Error as e:
        print(f'{Fore.RED}Erro ao excluir contato: {e}{Style.RESET_ALL}')
        return False
    finally:
        fechar_conexao(conn, cursor)

def exibir_contatos_encontrados(contatos_encontrados):
    if contatos_encontrados:
        for contato in contatos_encontrados:
            print(f'{Fore.CYAN}ID:{Style.RESET_ALL} {contato[0]} | {Fore.CYAN}Nome:{Style.RESET_ALL} {contato[1]:<20} | {Fore.CYAN}Telefone:{Style.RESET_ALL} {contato[2]:<15} | {Fore.CYAN}Email:{Style.RESET_ALL} {contato[3]}')