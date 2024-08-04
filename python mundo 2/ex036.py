valor_casa = input('Qual o valor da casa? R$')
salario = input('Qual o seu salário? R$')
anos = input('Em quantos anos você pretende pagar a casa? ')


if valor_casa.replace('.', '', 1).isdigit():
    valor_casa = float(valor_casa)
else:
    print('Valor da casa inválido')
    valor_casa = None

if salario.replace('.', '', 1).isdigit():
    salario = float(salario)
else:
    print('Salário inválido')
    salario = None

if anos.isdigit():
    anos = int(anos)
else:
    print('Número de anos inválido')
    anos = None

if valor_casa is not None and salario is not None and anos is not None:
    prestacao = valor_casa / (anos * 12)

    if prestacao > (salario * 0.3):
        print('Você não pode fazer esse financiamento')
    else:
        print('Financiamento aprovado')
