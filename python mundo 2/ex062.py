primeiro = int(input("Primeiro Termo: "))
razao = int(input('Razão: '))
termo_da_vez = primeiro
i = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while i <= total:
        print(f"{termo_da_vez} - ", end='')
        termo_da_vez += razao
        i += 1
    print('PAUSA')
    mais = int(input('Digite quantos números a mais você quer: '))
print('PA finalizada')