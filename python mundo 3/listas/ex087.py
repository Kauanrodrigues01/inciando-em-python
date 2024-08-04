# Inicializando a matriz 3x3 com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variáveis para armazenar a soma dos valores pares, o maior valor e a soma dos valores da terceira coluna
soma_par = 0
maior_valor = 0
soma_coluna = 0

# Preenchendo a matriz com valores fornecidos pelo usuário
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

# Imprimindo a matriz e calculando a soma dos valores pares
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(f'[{matriz[linha][coluna]}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna] 
    print()  # Quebra de linha após cada linha da matriz

print('-=' * 30)

# Calculando a soma dos valores da terceira coluna
for linha in range(len(matriz)):
    soma_coluna += matriz[linha][2] # Soma os valores da terceira coluna, é usado o índice 2 pois a matriz é 3x3

print(f'Soma dos valores pares: {soma_par}')
print(f'Soma dos valores da terceira coluna: {soma_coluna}')

# Encontrando o maior valor na matriz
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] > maior_valor:
            maior_valor = matriz[linha][coluna]


print(f'O maior valor na matriz é: {maior_valor}')