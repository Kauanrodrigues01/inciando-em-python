import math

soma_idade = 0
media_idade = 0
maioridade_de_homem = 0
homem_mais_velho = 0
total_mulheres_menores_20 = 0

for i in range(1, 5):
    print(f'----- {i} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F')).strip()
    soma_idade += idade

    if i == 1 and sexo in 'Mm':
        maioridade_de_homem = idade
        homem_mais_velho = nome
    if sexo in 'Mm' and idade > maioridade_de_homem:
        maioridade_de_homem = idade
        homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_menores_20 += 1

media_idade = soma_idade / 4
print(math.ceil(media_idade))
print(homem_mais_velho)
print(maioridade_de_homem)
print(total_mulheres_menores_20)