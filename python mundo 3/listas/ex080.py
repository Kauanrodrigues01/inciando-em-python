lista = []

for i in range(0, 5):
    n = int(input(f'Digite um valor: '))
    
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for c in lista:
            if n <= c:
                lista.insert(lista.index(c), n)# adiciona o valor na posição do valor que é maior que ele
                print(f'Adicionado na posição {lista.index(c)-1} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')