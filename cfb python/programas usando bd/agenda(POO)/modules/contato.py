class Contato:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    @staticmethod
    def from_tuple(contato_tuple):
        return Contato(contato_tuple[0], contato_tuple[1], contato_tuple[2], contato_tuple[3])
    
    def __str__(self):
        return f'ID: {self.id} | Nome: {self.nome} | Telefone: {self.telefone} | Email: {self.email}'
