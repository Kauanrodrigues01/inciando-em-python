numeros = list()
while True:
    try:
        n = int(input('Digite um número: '))
        numeros.append(n)
        r = input('Quer continuar? [S/N] ').strip().upper()
        if r == 'N':
            break
    except ValueError:
        print('Digite um número inteiro válido.')
        
# pares = [n for n in numeros if n % 2 == 0]
# impares = [n for n in numeros if n % 2 != 0]
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))
numeros_str = ' '.join(str(num) for num in numeros)

print(f'Os números digitados foram: {numeros_str}')
print(f'Os números pares digitados foram: {", ".join(map(str,pares))}')
print(f'Os números ímpares digitados foram: {", ".join(map(str,impares))}')