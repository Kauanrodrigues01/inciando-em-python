from .models import Livro, Membro, conectar

class Biblioteca:
    def cadastrar_livro(self):
        titulo = input('Título do livro: ')
        ano_publicacao = input('Ano de publicação (YYYY): ')
        self.mostrar_autores()
        id_autor = input('ID do autor: ')
        self.mostrar_categorias()
        id_categoria = input('ID da categoria (opcional): ')
        livro = Livro(titulo=titulo, ano_publicacao=ano_publicacao, id_autor=id_autor, id_categoria=id_categoria if id_categoria else None)
        livro.salvar()
        print('Livro cadastrado com sucesso!')

    def visualizar_livros(self):
        livros = Livro.listar()
        for livro in livros:
            print(f'ID: {livro.id_livro}, Título: {livro.titulo}, Ano: {livro.ano_publicacao}, Autor ID: {livro.id_autor}, Categoria ID: {livro.id_categoria}')

    def pesquisar_livro(self):
        self.visualizar_livros()
        id_livro = input('Digite o ID do livro para pesquisar: ')
        livro = Livro.buscar(id_livro)
        if livro:
            print(f'ID: {livro.id_livro}, Título: {livro.titulo}, Ano: {livro.ano_publicacao}, Autor ID: {livro.id_autor}, Categoria ID: {livro.id_categoria}')
        else:
            print('Livro não encontrado.')

    def excluir_livro(self):
        id_livro = input('Digite o ID do livro a ser excluído: ')
        livro = Livro.buscar(id_livro)
        if livro:
            livro.excluir()
            print('Livro excluído com sucesso!')
        else:
            print('Livro não encontrado.')

    def cadastrar_membro(self):
        nome_membro = input('Nome do membro: ')
        telefone = input('Telefone do membro: ')
        endereco = input('Endereço do membro: ')
        membro = Membro(nome_membro=nome_membro, telefone=telefone, endereco=endereco)
        membro.salvar()
        print('Membro cadastrado com sucesso!')

    def visualizar_membros(self):
        membros = Membro.listar()
        for membro in membros:
            print(f'ID: {membro.id_membro}, Nome: {membro.nome_membro}, Telefone: {membro.telefone}, Endereço: {membro.endereco}')

    def pesquisar_membro(self):
        id_membro = input('Digite o ID do membro para pesquisar: ')
        membro = Membro.buscar(id_membro)
        if membro:
            print(f'ID: {membro.id_membro}, Nome: {membro.nome_membro}, Telefone: {membro.telefone}, Endereço: {membro.endereco}')
        else:
            print('Membro não encontrado.')

    def excluir_membro(self):
        id_membro = input('Digite o ID do membro a ser excluído: ')
        membro = Membro.buscar(id_membro)
        if membro:
            membro.excluir()
            print('Membro excluído com sucesso!')
        else:
            print('Membro não encontrado.')

    def mostrar_livros_emprestados(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            query = """
            SELECT livro.id_livro, livro.titulo
            FROM livro
            JOIN emprestimos ON livro.id_livro = emprestimos.id_livro
            WHERE emprestimos.data_devolucao IS NULL
            """
            cursor.execute(query)
            livros_emprestados = cursor.fetchall()
            for livro in livros_emprestados:
                print(f'ID: {livro[0]}, Título: {livro[1]}')
            cursor.close()
            conn.close()
    
    def mostrar_autores(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM autor")
            autores = cursor.fetchall()
            if not autores:
                print('Nenhum autor cadastrado.')
                cursor.close()
                conn.close()
                return
            for autor in autores:
                print(f'ID: {autor[0]}, Nome: {autor[1]}')
            cursor.close()
            conn.close()
        
    def mostrar_categorias(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()
            if not categorias:
                print('Nenhuma categoria cadastrada.')
                cursor.close()
                conn.close()
                return
            for categoria in categorias:
                print(f'ID: {categoria[0]}, Nome: {categoria[1]}')
            cursor.close()
            conn.close()