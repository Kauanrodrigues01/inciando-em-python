import re

def verificar_nome_valido(nome):
    # Verifica se o nome contém pelo menos uma letra e não contém caracteres especiais
    return len(nome.strip()) > 0 and all(char.isalpha() or char.isspace() for char in nome)

def verificar_telefone_valido(telefone):
    # Remove todos os caracteres não numéricos
    telefone_numerico = ''.join(char for char in telefone if char.isdigit())
    # Verifica se o número tem 10 ou 11 dígitos
    return len(telefone_numerico) in [10, 11]

def verificar_email_valido(email):
    # Expressão regular para validar o formato do email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def verificar_id_valido(id):
    return id.isdigit() and int(id) > 0