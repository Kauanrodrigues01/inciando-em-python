condicao = 0
numeros = []

while condicao != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        numeros.append(num)
    condicao = num

soma = 0

for i in numeros:
    soma += i
print('A soma dos números é: {}'.format(soma))