class Carro:
    def __init__(self, velMax, ligado, cor) -> None:
        self.velMax = velMax
        self.ligado = ligado
        self.cor = cor
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def info(self):
        print(f"Velocidade Máxima: {self.velMax}")
        print(f"Cor: {self.cor}")
        print(f"Ligado: {self.ligado}")
        
    def andar(self):
        if self.ligado:
            print("Carro em movimento")
        else:
            print("Carro parado")
    
    def __del__(self):
        print("Objeto destruido")