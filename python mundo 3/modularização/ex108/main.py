from modules.functions import pedir_numero, metade, dobro, aumentar

num = pedir_numero()

print(f'A medate de R${num:>.2f} é R${metade(num)}')
print(f'O dobro de R${num:>.2f} é R${dobro(num)}')
print(f'Aumentando 10% temos R${aumentar(num, 10)}')