from random import randint
import time

num_de_jogos = int(input('Quantos jogos você quer sortear? '))
for jogo in range(num_de_jogos):
    numeros = list()
    while len(numeros) < 6:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
    numeros.sort()
    print(f'Jogo {jogo + 1}: {numeros}')
    time.sleep(0.5)