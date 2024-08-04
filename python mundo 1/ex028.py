import random
import os
import time

num_sorteado = random.randint(0, 5)

def verificarChute():
    os.system('cls')
    chute = input('Digite um número entre 0 e 5: ')
    if chute.isnumeric():
        int(chute)
    try:
        if 0 >= chute < 6:
            if num_sorteado == chute:
                print('Você acertou!')
            else:
                print(f'Você errou!')
                time.sleep(2) # Esperar 5 segundos para recomençar o jogo
                verificarChute()
        else:
            print('Número inválido. Tente novamente.')
            time.sleep(2)
            verificarChute()
    except:
        print('Por favor, digite um número válido.')
        time.sleep(2)
        verificarChute()

verificarChute()