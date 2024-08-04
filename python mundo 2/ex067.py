condicao = 1
while condicao > 0:
    num = int(input('Quer ver tabuada de que valor? '))
    print('-'*30)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('-' * 30)

    condicao = num