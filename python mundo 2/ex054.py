import datetime

ano_atual = datetime.date.today().year
maiores = 0
menores = 0

anos_nascimento = list(map(int, input('Digite os anos de nascimento separados por espaço: ').split()))

for ano_nasc in anos_nascimento:
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Pessoas maiores de 18 anos: {maiores}')
print(f'Pessoas menores de 18 anos: {menores}')
