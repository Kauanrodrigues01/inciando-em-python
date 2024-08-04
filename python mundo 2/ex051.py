primeiro_termo = int(input('primeiro termo: '))
razao = int(input('razao: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo_termo + 1, razao):
    print(i)