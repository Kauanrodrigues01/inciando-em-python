import os
from time import sleep

def leiaInt(txt):
    """
    Lê um valor inteiro do usuário, garantindo que o valor inserido seja válido.

    Parâmetros:
    txt (str): A mensagem a ser exibida ao usuário.

    Retorna:
    int: O valor inteiro inserido pelo usuário.
    """
    while True:
        try:
            num = int(input(txt).strip())
        except (ValueError, TypeError):
            print('\033[91mERRO: Digite um valor válido\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[91mUsuário preferiu não digitar\033[0m')
            return 0
        else:
            return num

def criar_arquivo_pessoas(nome_arquivo):
    """
    Cria um arquivo vazio com o nome especificado.

    Parâmetros:
    nome_arquivo (str): O nome do arquivo a ser criado.
    """
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.close()
    except Exception as e:
        print(f'\033[91mERRO: Não foi possível criar o arquivo. {e}\033[0m')

def linha(tam=30):
    """
    Gera uma linha de caracteres de comprimento especificado.

    Parâmetros:
    tam (int, opcional): O comprimento da linha. O padrão é 30.

    Retorna:
    str: Uma linha de caracteres.
    """
    return '-' * tam

def cabecalho(txt=''):
    """
    Exibe um cabeçalho com um texto centralizado.

    Parâmetros:
    txt (str, opcional): O texto a ser exibido no cabeçalho.
    """
    print(f'\033[96m{linha(len(txt) + 5)}\033[0m')
    print(f'\033[96m{txt.center(len(txt) + 5)}\033[0m')
    print(f'\033[96m{linha(len(txt) + 5)}\033[0m') 

def menu(lista):
    """
    Exibe um menu com opções numeradas e retorna a opção escolhida pelo usuário.

    Parâmetros:
    lista (list): Uma lista de opções a serem exibidas.

    Retorna:
    int: O número da opção escolhida pelo usuário.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista, start=1):
        print(f'\033[93m[{i}] {v}\033[0m')
    
    opc_escolhida = leiaInt('\033[92mSua Opção: \033[0m')
    return opc_escolhida

def ver_pessoas():
    """
    Exibe as pessoas cadastradas em um arquivo. Se o arquivo não existir, cria um novo arquivo e exibe uma mensagem de erro.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    arquivo_nome = 'tratamentodeerros/ex115/pessoas.txt'
    cabecalho('PESSOAS CADASTRADAS')
    
    if not os.path.exists(arquivo_nome):
        criar_arquivo_pessoas(arquivo_nome)
        print('\033[91mERRO: Nenhuma pessoa cadastrada. Cadastre pessoas para vê-las...\033[0m')
    
    try:
        with open(arquivo_nome, 'r') as arquivo:
            for linha in arquivo:
                dado = linha.strip().split(';')
                if len(dado) == 2:
                    print(f'{dado[0]:<20} {dado[1]:>3} anos')
                    sleep(0.2)
    except Exception as e:
        print(f'\033[91mERRO: Não foi possível abrir o arquivo. {e}\033[0m')
    input('\033[92mPressione ENTER para continuar...\033[0m')

def cadastrar_pessoas():
    """
    Cadastra novas pessoas no arquivo, pedindo o nome e a idade. Digitar "Fim" no campo "Nome" encerra o cadastro.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho('CADASTRO DE PESSOAS')
    print('Digite "Fim" no campo "Nome" para sair')
    while True:
        try:
            nome = input('Nome: ').strip()
            idade = leiaInt('Idade: ')
        except Exception as e:
            print(f'\033[91mERRO: Não foi possível ler os dados. {e}\033[0m')
        else:
            if nome.upper() == 'FIM':
                print('\033[93mSaindo do cadastro de pessoas...\033[0m')
                break
            try:
                with open('tratamentodeerros/ex115/pessoas.txt', 'a') as arquivo:
                    arquivo.write(f'{nome};{idade}\n')
            except:
                criar_arquivo_pessoas('tratamentodeerros/ex115/pessoas.txt')
                with open('tratamentodeerros/ex115/pessoas.txt', 'a') as arquivo:
                    arquivo.write(f'{nome};{idade}\n')
            else:
                print(f'\033[92m{nome} cadastrado com sucesso!\033[0m')

def remover_pessoas():
    """
    Remove uma pessoa específica do arquivo baseado no nome. Exibe uma lista de pessoas com o nome especificado para o usuário escolher qual remover.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho('REMOVER PESSOA')
    nome = input('Nome da pessoa para remover: ').strip()
    arquivo_nome = 'tratamentodeerros/ex115/pessoas.txt'
    
    try:
        with open(arquivo_nome, 'r') as arquivo:
            linhas = arquivo.readlines() # salva a lista de pessoas originais
            
        pessoas_encontradas = [linha.strip() for linha in linhas if linha.split(';')[0].strip().lower() == nome.lower()]
        
        if not pessoas_encontradas:
            print(f'\033[91mERRO: {nome} não encontrado\033[0m')
            return

        for i, pessoa in enumerate(pessoas_encontradas, start=1):
            pessoa = pessoa.split(';')
            print(f'{i} - {pessoa[0]}')
            
        pessoa_remover = leiaInt('Digite o número da pessoa que deseja remover: ')
        
        if pessoa_remover <= 0 or pessoa_remover > len(pessoas_encontradas):
            print('\033[91mERRO: Digite um número válido\033[0m')
            return
        
        pessoa_a_remover = pessoas_encontradas[pessoa_remover - 1]
        
        with open(arquivo_nome, 'w') as arquivo: # reescreve o arquivo sem a pessoa removida
            for linha in linhas:
                if linha.strip() != pessoa_a_remover:
                    arquivo.write(linha)
                else:
                    pessoa_a_remover = pessoa_a_remover.split(';')
                    print(f'\033[92m{pessoa_a_remover[0]} removido com sucesso!\033[0m')
                    
    except Exception as e:
        print(f'\033[91mERRO: Não foi possível remover a pessoa. {e}\033[0m')