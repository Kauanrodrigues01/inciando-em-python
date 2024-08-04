num = int(input('Digite um número: '))
qtd_de_divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        qtd_de_divisores += 1
        print(f'\033[92m{i}\033[0m', end=' ')
    else:
        print(f'\033[91m{i}\033[0m', end=' ')

print()

if qtd_de_divisores < 3:
    print(f'O número é primo pois só tem {qtd_de_divisores} divisores')
else:
    print('Não é primo')
