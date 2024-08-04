import os
import time
from .utils import normalizar, validar_numero_telefone

contatos = [
    {"nome": 'Larissa', "tel": '85994324916'},
    {"nome": 'Larissa Silva', "tel": '85994324916'},
    {"nome": 'Larissa kAREN', "tel": '85994324916'}
]

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
        if normalizar(contato["nome"]).startswith(normalizar(nome)):
            print(f'Nome: {contato["nome"]}, Telefone: {contato["tel"]}')
            break
    else:
        print('Contato não encontrado.')
    input('Pressione Enter para continuar...')

def remover_contato():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input('Digite o nome do contato a remover: ')
    contatos_correspondentes = [contato for contato in contatos if normalizar(contato["nome"]).startswith(normalizar(nome))]

    if not contatos_correspondentes:
        print('Contato não encontrado.')
    else:
        print('Selecione o contato a remover:')
        for i, contato in enumerate(contatos_correspondentes, start=1):
            print(f'[{i}] - {contato["nome"]}')
        escolha = input('Digite o número do contato que deseja remover: ')

        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(contatos_correspondentes):
                contatos.remove(contatos_correspondentes[escolha - 1])
                print('Contato removido com sucesso!')
            else:
                print('Número inválido.')
        else:
            print('Entrada inválida.')

    input('Pressione Enter para continuar...')

def listar_contatos():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not contatos:
        print('Nenhum contato para listar.')
    else:
        for contato in contatos:
            print(f'Nome: {contato["nome"]}, Telefone: {contato["tel"]}')
    input('Pressione Enter para continuar...')
