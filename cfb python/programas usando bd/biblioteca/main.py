import os
from modules.biblioteca import Biblioteca

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar_tela()
    print("MENU PRINCIPAL")
    print("1 - Cadastrar Livros")
    print("2 - Visualizar Livros")
    print("3 - Pesquisar Livros")
    print("4 - Excluir Livros")
    print("5 - Mostrar Livros que estão emprestados")
    print("6 - Cadastrar Membro")
    print("7 - Visualizar Membros")
    print("8 - Pesquisar Membros")
    print("9 - Excluir Membro")
    print("10 - Sair")
    print()

def main():
    biblioteca = Biblioteca() # Instanciando a classe Biblioteca
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            biblioteca.cadastrar_livro() # Chamando o método cadastrar_livro
        elif opcao == '2':
            biblioteca.visualizar_livros() # Chamando o método visualizar_livros
        elif opcao == '3':
            biblioteca.pesquisar_livro() # Chamando o método pesquisar_livro
        elif opcao == '4':
            biblioteca.excluir_livro() # Chamando o método excluir_livro
        elif opcao == '5':
            biblioteca.mostrar_livros_emprestados() # Chamando o método mostrar_livros_emprestados
        elif opcao == '6':
            biblioteca.cadastrar_membro() # Chamando o método cadastrar_membro
        elif opcao == '7':
            biblioteca.visualizar_membros() # Chamando o método visualizar_membros
        elif opcao == '8':
            biblioteca.pesquisar_membro() # Chamando o método pesquisar_membro
        elif opcao == '9':
            biblioteca.excluir_membro() # Chamando o método excluir_membro
        elif opcao == '10':
            break
        else:
            print("Opção inválida! Tente novamente.")
        input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()