# import time
# for i in range(3, -1, -1):
#     print(i)
#     time.sleep(1)
# print('BOOM!!!!!')



# numeros_pares = []
# for i in range(0, 51, 2):
#     numeros_pares.append(i)
# print(numeros_pares)


from random import randint
num = int(input(':'))
numeros_sorteados : list = [randint(1, 11) for i in range(1, num)]
print(numeros_sorteados)