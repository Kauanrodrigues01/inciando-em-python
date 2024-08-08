import os
from colorama import Fore, Back, Style
from modules.functions import *

def cabeçalho(txt):
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
        cabeçalho('Agenda de contatos')
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cabeçalho('Inserir contato')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            contato = Contato(None, nome, telefone, email)
            inserir_contato(contato)
        elif opcao == '2':
            cabeçalho('Lista de contatos')
            listar_contatos()
        elif opcao == '3':
            cabeçalho('Alterar contato')
            nome_procurar = input('Digite o nome do contato a ser alterado: ')
            contatos_encontrados = buscar_contato_por_nome(nome_procurar)
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabeçalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
                
                identificador = input('Digite o ID do contato a ser alterado: ')
                nome = input('Digite o novo nome: ')
                telefone = input('Digite o novo telefone: ')
                email = input('Digite o novo email: ')
                contato = Contato(identificador, nome, telefone, email)
                alterar_contato(contato, contatos_encontrados)
            else:
                print(f'{Fore.RED}Nenhum contato encontrado!{Style.RESET_ALL}')
        elif opcao == '4':
            cabeçalho('Excluir contato')
            contatos_encontrados = buscar_contato_por_nome(input('Digite o nome do contato a ser excluído: '))
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabeçalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
                id = input('Digite o ID do contato a ser excluído: ')
                try:
                    excluir_contato(id, contatos_encontrados)
                except Exception as e:
                    print(f'{Fore.RED}Erro ao excluir contato: {e}{Style.RESET_ALL}')
        elif opcao == '5':
            cabeçalho('Consultar contato')
            nome = input('Digite o nome do contato a ser consultado: ')
            contatos_encontrados = buscar_contato_por_nome(nome)
            if contatos_encontrados:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabeçalho('Contatos encontrados')
                exibir_contatos_encontrados(contatos_encontrados)
        elif opcao == '6':
            break
        input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()