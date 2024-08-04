preco_total = float(input('Digite o valor final das compras: R$'))

print('''
    FORMAS DE PAGAMENTO
    [1] À vista dinheiro
    [2] À vista cartão
    [3] 2x no cartão
    [4] 3x no cartão''')

opcao_escolhida = int(input("Digite o número da forma de pagamento: "))

match opcao_escolhida:
    case 1:
        print('No dinheiro tem 10% de desconto')
        preco_total = preco_total - (preco_total * 0.10)
        print(f'O valor final é R$ {preco_total:.2f}')
    case 2:
        print('À vista no cartão tem 5% de desconto')
        preco_total = preco_total - (preco_total * 0.05)
        print(f'O valor final é R$ {preco_total:.2f}')
    case 3:
        print(f'Preço normal em 2x no cartão')
        print(f'O valor final é R$ {preco_total:.2f}')
    case 4:
        preco_total = preco_total + (preco_total * 0.20)
        print(f'O valor final é R$ {preco_total:.2f}')
    case _:
        print('Opção inválida. Por favor, escolha uma opção válida.')