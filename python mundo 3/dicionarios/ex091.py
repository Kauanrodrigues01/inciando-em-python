import random

lista_jogadores = list()
for i in range(1, 5):
    num_sorteado = random.randint(1, 6)
    nome_jogador = f'Jogador {i}'
    jogador = {"nome": nome_jogador, "num_sorteado": num_sorteado}
    lista_jogadores.append(jogador)

# Ordenar a lista de jogadores pelo número sorteado em ordem decrescente
lista_jogadores_ordenada = sorted(lista_jogadores, key=lambda x: x['num_sorteado'], reverse=True)

print('-=' * 30)
print(f'{"":<5} == RANKING DOS JOGADORES {"":>5}')
print('-=' * 30)
for idx, jogador in enumerate(lista_jogadores_ordenada, start=1):
    print(f'{idx}º lugar: {jogador["nome"]} com número {jogador["num_sorteado"]}')