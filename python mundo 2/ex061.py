primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
i = 1

while i < 11:
    if i == 10:
        print(f"{termo}", end="")
        break
    print(f"{termo} - ", end="")
    termo += razao
    i += 1