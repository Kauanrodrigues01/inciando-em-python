import os
import time

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
