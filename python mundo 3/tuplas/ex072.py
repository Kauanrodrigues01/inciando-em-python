numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", 
    "cinco", "seis", "sete", "oito", "nove", 
    "dez", "onze", "doze", "treze", "quatorze", 
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", 
    "vinte"
)

while True:
    num = input('Digite um número entre 0 e 20: ')
    
    if num.isdigit():
        num = int(num)

        if num > 20 or num < 0:
            print('Número invalido')
            
        if num <= 20 and num >= 0:
            break
    else:
        print('Número invalido')
        
print(f'Você digitou o número {numeros_extenso[num]}')