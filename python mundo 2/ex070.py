condicao = 1
produtos = []

while condicao != 'N':
    nome_produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor: R$'))
    print('-'*30)

    produto = {
        "nome": nome_produto,
        "preco": valor
    }
    produtos.append(produto)

    continuar = input('Quer continuar[S/N]? ').strip().upper()
    condicao = continuar

total = 0
mais_de_mil = 0
menor_valor = 10000000000000000000
nome_menor_valor = 0
for i in produtos:
    total += i["preco"]

    if i["preco"] > 1000:
        mais_de_mil += 1

    if i["preco"] < menor_valor:
        menor_valor = i["preco"]
        nome_menor_valor = i["nome"]

print('O total da compra foi R${}'.format(total))
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor_valor} que custa R${menor_valor}')