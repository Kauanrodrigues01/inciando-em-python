from modules.contato import (
    cadastrar_novo_contato,
    buscar_contato,
    remover_contato,
    listar_contatos,
    carregar_contatos
)
from modules.display import exibir_opcoes, escolher_opcoes

def main():
    contatos = carregar_contatos()
    while True:
        exibir_opcoes()
        opcao = escolher_opcoes()
        if opcao == 1:
            cadastrar_novo_contato(contatos)
        elif opcao == 2:
            buscar_contato(contatos)
        elif opcao == 3:
            remover_contato(contatos)
        elif opcao == 4:
            listar_contatos(contatos)
        elif opcao == 5:
            print('Saindo...')
            break

if __name__ == '__main__':
    main()