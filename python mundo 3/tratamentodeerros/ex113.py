try:
    num = int(input('Digite um número'))
except Exception as erro:
    print(f'Algo deu errado: {erro.__class__}')
else:
    print(f'Você digitou o valor {num}')