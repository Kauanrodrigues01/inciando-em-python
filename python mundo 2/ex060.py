num = int(input("Digite um número: "))
contador = num
fatores = []
fatorial = 1

while contador >= 1:
    fatorial *= contador
    fatores.append(str(contador))
    contador -= 1

fatores_str = " x ".join(fatores)
print(f"{fatores_str} = {fatorial}")
