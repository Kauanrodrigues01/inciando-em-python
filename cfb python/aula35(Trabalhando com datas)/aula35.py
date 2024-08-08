import datetime

data = datetime.datetime.now()
data2 = datetime.date.today()

# transformar string em data
data_str3 = '2024-08-16 20:43:00'
data3 = datetime.datetime.strptime(data_str3, '%Y-%m-%d %H:%M:%S')

# transformar data em string
data_str = data3.strftime('%d/%m/%Y %H:%M:%S')

print(data)
print(data2)
print(data3)
print(data_str)

print('-------------------' * 2)
# criar uma data
data4 = datetime.datetime(2023, 8, 16, 20, 43, 00)
print(data4)

print('-------------------' * 2)

# somar ou subtrair datas, tirando 365 dias, 2 horas e 15 minutos
data5 = data4 - datetime.timedelta(days=365, hours=2, minutes=15)
print(data5)

print('-------------------' * 2)

# calcular a diferença entre datas
data6 = datetime.datetime.now()
data7 = datetime.datetime(2023, 8, 16, 20, 43, 00)
diferenca = data7 - data6
print(diferenca)