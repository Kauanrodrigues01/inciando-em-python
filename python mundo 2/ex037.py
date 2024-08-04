def exibi_opcoes_e_pega_numero_da_opcao():
    print('Escolha a base para converter\n')
    print('1. Binário')
    print('2. Octal')
    print('3. Hexadecimal\n')
    
    opcao_escolhida = input('Digite o número da opção: ')
    
    if opcao_escolhida.isdigit():
        return int(opcao_escolhida)
    else:
        print('Digite uma opção válida')
        return 

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    
    opcao = exibi_opcoes_e_pega_numero_da_opcao()
    
    if opcao:
        if opcao == 1:
            print(f'O número {num} em binário é: {bin(num)}')
        elif opcao == 2:
            print(f'O número {num} em octal é: {oct(num)}')
        elif opcao == 3:
            print(f'O número {num} em hexadecimal é: {hex(num)}')
        else:
            print('Opção inválida')
else:
    print('Digite um número inteiro válido')
