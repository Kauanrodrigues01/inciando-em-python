import os
from colorama import Fore, Back, Style
from modules.functions import *

def cabecalho(txt):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.LIGHTBLUE_EX}=' * (len(txt) + 10))
    print(f'{Fore.LIGHTBLUE_EX}{txt:^{len(txt) + 10}}{Style.RESET_ALL}')
    print(f'{Fore.LIGHTBLUE_EX}=' * (len(txt) + 10))
    print(Style.RESET_ALL)
    
def exibir_menu():
    print(f'{Fore.LIGHTBLUE_EX}1 - Inserir contato')
    print('2 - Listar contatos')
    print(f'3 - Alterar contato')
    print(f'4 - Excluir contato')
    print(f'5 - Consultar contato')
    print(f'6 - Sair{Style.RESET_ALL}')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho('Agenda de contatos')
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cabecalho('Inserir contato')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            inserir_contato(nome, telefone, email)
        elif opcao == '2':
            cabecalho('Lista de contatos')
            listar_contatos()
        elif opcao == '3':
            cabecalho('Alterar contato')
            nome_procurar = input('Digite o nome do contato a ser alterado: ')
            contatos_encontrados = buscar_contato_por_nome(nome_procurar)
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
                
                identificador = input('Digite o ID do contato a ser alterado: ')
                nome = input('Digite o novo nome: ')
                telefone = input('Digite o novo telefone: ')
                email = input('Digite o novo email: ')
                alterar_contato(identificador, nome, telefone, email, contatos_encontrados)
        elif opcao == '4':
            cabecalho('Excluir contato')
            contatos_encontrados = buscar_contato_por_nome(input('Digite o nome do contato a ser excluído: '))
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
                id = input('Digite o ID do contato a ser excluído: ')
                excluir_contato(id, contatos_encontrados)
        elif opcao == '5':
            cabecalho('Consultar contato')
            nome = input('Digite o nome do contato a ser consultado: ')
            contatos_encontrados = buscar_contato_por_nome(nome)
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
        elif opcao == '6':
            break
        input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()