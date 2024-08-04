import os
import time
import re
import unicodedata

contatos = []


def remover_acentos_caracteres_especiais(texto):
    # Normalize the unicode string to decompose combined characters
    texto_normalizado = unicodedata.normalize('NFKD', texto)

    # Remove accents by filtering out combining characters (category "Mn")
    texto_sem_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

    # Remove special characters, keeping only alphanumeric characters and spaces
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acentos)

    return texto_limpo.lower()

def exibir_opcoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
[1] Adicionar contato
[2] Buscar contato
[3] Remover contatos
[4] Listar contatos
[5] Sair''')

def validar_opcoes_e_retornar_opcao(opcao='0'):
    if opcao.isdigit():
        opcao = int(opcao)
    else:
        return None

    if 1 <= opcao <= 5:
        return opcao
    else:
        return None

def escolher_opcoes():
    while True:
        print()
        opcao = input('Digite o número da opção: ')
        opcao = validar_opcoes_e_retornar_opcao(opcao)
        if opcao is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Entrada inválida, tente novamente')
            time.sleep(1)
            exibir_opcoes()
        else:
            return opcao

def validar_numero_telefone(numero):
    padrao = r'^(\d{10}|\d{11})$'
    return bool(re.match(padrao, numero))

def cadastrar_novo_contato():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input('Digite o nome do contato: ')
    tel = input('Digite o telefone (apenas números): ')
    tel = tel.strip().replace(' ', '')

    if validar_numero_telefone(tel):
        novo_contato = {"nome": nome, "tel": tel}
        contatos.append(novo_contato)
        print('Contato adicionado com sucesso!')
    else:
        print('Telefone inválido, digite novamente')
        time.sleep(1.5)
        cadastrar_novo_contato()

def buscar_contato():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input('Digite o nome do contato a buscar: ')
    for contato in contatos:
        if remover_acentos_caracteres_especiais(contato["nome"]) == remover_acentos_caracteres_especiais(nome):
            print(f'Nome: {contato["nome"]}, Telefone: {contato["tel"]}')
            break
    else:
        print('Contato não encontrado.')
    input('Pressione Enter para continuar...')

def remover_contato():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input('Digite o nome do contato a remover: ')
    for contato in contatos:
        if remover_acentos_caracteres_especiais(contato["nome"]) == remover_acentos_caracteres_especiais(nome):
            contatos.remove(contato)
            print('Contato removido com sucesso!')
            break
    else:
        print('Contato não encontrado.')
    input('Pressione Enter para continuar...')

def listar_contatos():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not contatos:
        print('Nenhum contato para listar.')
    else:
        for contato in contatos:
            print(f'Nome: {contato["nome"]}, Telefone: {contato["tel"]}')
    input('Pressione Enter para continuar...')

def main():
    while True:
        exibir_opcoes()
        opcao = escolher_opcoes()
        if opcao == 1:
            cadastrar_novo_contato()
        elif opcao == 2:
            buscar_contato()
        elif opcao == 3:
            remover_contato()
        elif opcao == 4:
            listar_contatos()
        elif opcao == 5:
            print('Saindo...')
            break