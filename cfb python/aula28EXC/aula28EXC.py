import os
import json

class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
        
    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Preço: {self.preco}")
        print("-" * 30)
        
    def ver_financiamento(self, parcelas, juros, valor_entrada=0):
        valor_financiamento = self.preco - valor_entrada
        total = valor_financiamento + (valor_financiamento * (juros / 100))
        print(f"Valor total do carro: {total}")
        print(f"Valor da parcela: {total / parcelas}")
        print("-" * 30)
        
    def to_dict(self):
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'cor': self.cor,
            'preco': self.preco
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            marca=data['marca'],
            modelo=data['modelo'],
            ano=data['ano'],
            cor=data['cor'],
            preco=data['preco']
        )

class LojaDeCarros:
    def __init__(self):
        self.carros = []
        self.load_carros()

    def save_carros(self):
        with open('aula28EXC/carros.json', 'w') as f:
            json.dump([carro.to_dict() for carro in self.carros], f)

    def load_carros(self):
        if os.path.exists('aula28EXC/carros.json'):
            with open('aula28EXC/carros.json', 'r') as f:
                data = json.load(f)
                self.carros = [Carro.from_dict(carro) for carro in data]

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1 - Cadastrar Carro")
            print("2 - Listar Carros")
            print("3 - Ver financiamento")
            print("4 - Remover Carro")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_carro()
            elif opcao == "2":
                self.listar_carros()
            elif opcao == "3":
                self.financiar()
            elif opcao == "4":
                self.remover_carro()
            elif opcao == "5":
                self.save_carros()
                exit()
            else:
                print("Opção inválida")
            input("Pressione ENTER para continuar...")
    
    def cadastrar_carro(self):
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        cor = input("Cor: ")
        preco = float(input("Preço: "))
        carro = Carro(marca, modelo, ano, cor, preco)
        self.carros.append(carro)
        print("Carro cadastrado com sucesso!")
    
    def listar_carros(self):
        if not self.carros:
            print("Nenhum carro cadastrado.")
        else:
            for i, carro in enumerate(self.carros, start=1):
                print("-" * 30)
                print(f'{i} - {carro.marca} {carro.modelo} ({carro.ano}) - {carro.cor} - R${carro.preco}')
                print("-" * 30)
    
    def financiar(self):
        self.listar_carros()
        try:
            carro = int(input("Escolha um carro pelo número: "))
            if carro < 1 or carro > len(self.carros):
                print("Carro não encontrado")
                return
        except ValueError:
            print("Valor inválido")
            return
        else:
            car = self.carros[carro - 1]
            try:
                parcelas = int(input("Número de parcelas: "))
                juros = float(input("Taxa de juros (em %): "))
                valor_entrada = float(input("Valor da entrada: "))
            except ValueError:
                print("Valor inválido")
                return
            car.ver_financiamento(parcelas, juros, valor_entrada)
    
    def remover_carro(self):
        self.listar_carros()
        try:
            carro = int(input("Escolha um carro pelo número: "))
            if carro < 1 or carro > len(self.carros):
                print("Carro não encontrado")
                return
        except ValueError:
            print("Valor inválido")
            return
        else:
            self.carros.pop(carro - 1)
            print("Carro removido com sucesso")

loja = LojaDeCarros()
loja.menu()
