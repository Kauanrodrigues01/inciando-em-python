def mostrar_digitos(numero):
    if 1 <= numero <= 9999:
        # Unidades
        unidade = numero % 10
        
        # Dezenas
        dezena = (numero // 10) % 10
        
        # Centenas
        centena = (numero // 100) % 10
        
        # Milhares
        milhar = (numero // 1000) % 10

        print(f"Unidade: {unidade}")
        print(f"Dezena: {dezena}")
        print(f"Centena: {centena}")
        print(f"Milhar: {milhar}")
    else:
        print("Número fora do intervalo (1 a 9999)")

# Ler o número do usuário
try:
    numero = int(input("Digite um número de 1 a 9999: "))
    mostrar_digitos(numero)
except ValueError:
    print("Por favor, digite um número válido.")
