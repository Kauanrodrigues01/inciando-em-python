from modules.display import exibir_opcoes, escolher_opcoes
from modules.contatos import cadastrar_novo_contato, buscar_contato, remover_contato, listar_contatos

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

if __name__ == '__main__':
    main()
