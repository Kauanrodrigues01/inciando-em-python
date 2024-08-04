from datetime import date
ano_atual = date.today().year

nome = input('Nome: ')
ano_nasc = int(input('Ano de nascimento: '))
carteira_trabalho = int(input('Carteira de trabalho (0 não tem): '))

dados = {
    "Nome": nome,
    "Ano de Nascimento": ano_nasc,
    "Idade": ano_atual - ano_nasc,
    "Carteira de Trabalho": carteira_trabalho
}

if carteira_trabalho != 0:
    ano_contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    aposentadoria = 35 - (ano_atual - ano_contratacao) + (ano_atual - ano_nasc)
    
    dados["Ano de Contratação"] = ano_contratacao
    dados["Salário"] = salario
    dados["Ano de Aposentadoria"] = aposentadoria

print()
print('-=' * 30)
for chave, valor in dados.items():
    if chave == "Salário":
        print(f'{chave}: R${valor:.2f}')
    else:
        print(f'{chave}: {valor}')
