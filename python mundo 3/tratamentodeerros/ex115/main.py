from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas', 'Cadastrar Pessoas', 'Remover Pessoas','Sair do Sistema'])
    if resposta == 1:
        ver_pessoas()
    elif resposta == 2:
        cadastrar_pessoas()
    elif resposta == 3:
        remover_pessoas()
    elif resposta == 4:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[91mERRO: Digite uma opção válida\033[0m')
    sleep(1)