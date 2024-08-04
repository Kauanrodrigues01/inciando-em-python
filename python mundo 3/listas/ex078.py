lista = []

for i in range(0, 5):
    n = int(input(f'Digite um valor para a posição {i}: ')) 
    lista.append(n)

max_valor = max(lista)
min_valor = min(lista)
max_posicoes = []
min_posicoes = []

for i, v in enumerate(lista):
    if v == max_valor:
        max_posicoes.append(i)
    if v == min_valor:
        min_posicoes.append(i)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max_valor} nas posições {" - ".join(map(str, max_posicoes))}')
print(f'O menor valor digitado foi {min_valor} nas posições {" - ".join(map(str, min_posicoes))}')
