def é_palíndromo(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

texto = input('Digite uma frase: ')

if é_palíndromo(texto):
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
