from datetime import date

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

data_atual = date.today()

data_nascimento = date(ano, mes, dia)

idade = data_atual.year - data_nascimento.year

if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

if idade >= 18:
    print(f'Você tem {idade} anos e precisa se alistar.')
else:
    anos_faltantes = 18 - idade
    ano_alistamento = data_nascimento.year + 18
    print(f'Você tem {idade} anos. Ainda faltam {anos_faltantes} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_alistamento}.')
