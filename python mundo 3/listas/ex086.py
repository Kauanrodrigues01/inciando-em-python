matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()