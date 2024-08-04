def calcular_e_ebxibir_fatorial(num):
    valor = 1
    while num > 0:
        valor *= num
        if num > 1:   
            print(f'{num} x ', end='')
        else:
            print(f'{num} ', end='')
        num -= 1
    print(f'= {valor}')

calcular_e_ebxibir_fatorial(5)