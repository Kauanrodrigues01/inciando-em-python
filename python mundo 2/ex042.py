'''Para formar um triângulo, a soma de dois segmentos quaisquer tem que ser maior que o outro segmento'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar')
    if r1 == r2 and r2 == r3:
        print('Triângulo Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não pode formar')