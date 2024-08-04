condicao = 0
numeros = []

while condicao != 'N':
    num = input('Digite um número [Digite N para parar]: ')

    if num.isdigit():
        num = int(num)
        numeros.append(num)
    else:
        num = num.strip().upper()

    condicao = num

if numeros:
    soma_numeros = sum(numeros)
    media = soma_numeros / len(numeros)
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    print(f'Você digitou {len(numeros)} números')
    print(f'A média entre eles é {media:.2f}')
    print(f'Menor número: {menor_numero} / Maior número: {maior_numero}')
else:
    print('Nenhum número foi digitado.')
