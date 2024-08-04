import re

pessoas = list()
while True:
    nome = input('Digite o nome da pessoa: ').strip()
    peso_str = input('Digite seu peso: ').strip()

    # Remove pontos e vírgulas do peso_str
    peso_str = re.sub(r'[.,]', '', peso_str)

    # Verifica se o nome é válido e se o peso é um número após a substituição
    if nome.replace(" ", "").isalpha() and peso_str.isdigit():
        peso = float(peso_str)  # Convertendo o peso para float
        pessoa = [nome, peso]
        pessoas.append(pessoa)
    else:
        print('Inválido')

    r = input('Quer continuar [S/N]? ').strip().upper()
    if r == 'N':
        break

maior_peso, menor_peso = 0, float('inf')
lista_maior_peso = list()
lista_menor_peso = list()

# Encontrando o maior e menor peso
for pessoa in pessoas:
    peso = pessoa[1]
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

# Criando listas de pessoas com maior e menor peso
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        lista_maior_peso.append(pessoa[0])
    if pessoa[1] == menor_peso:
        lista_menor_peso.append(pessoa[0])

print(f'O MAIOR peso foi {maior_peso}, as pessoas {", ".join(lista_maior_peso)} têm esse peso')
print(f'O MENOR peso foi {menor_peso}, as pessoas {", ".join(lista_menor_peso)} têm esse peso')