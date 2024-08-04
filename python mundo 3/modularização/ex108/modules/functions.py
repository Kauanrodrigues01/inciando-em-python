from time import sleep
from modules.utils import normalizar

def pedir_numero():
    while True:
        num = input('Digite um número: ').strip()
        num = num.replace(',', '.')
        
        if normalizar(num).isdigit():
            num = float(num)
            return num
        else:
            print('Valor invalido')
            print('Digite novamente')
            sleep(1)
        
def metade(num):
    return num / 2

def dobro(num):
    return num * 2

def aumentar(num, porcentagem):
    return num + (num * porcentagem)