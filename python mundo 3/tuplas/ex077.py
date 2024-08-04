palavras_aleatorias = ("livro", "montanha", "futuro", "café", "astronauta", "oceano", "música", "jardim", "lua", "neve")
vogais = ['a', 'e', 'i', 'o', 'u']


for i in palavras_aleatorias:
    letras_da_palavra = list(i)
    vogais_usadas = []
    
    for c in letras_da_palavra:
        for vogal in vogais:
            if c == vogal:
                vogais_usadas.append(c) if c not in vogais_usadas else None
                
    print(f'Na palavra {i.upper()} temos as vogais {" ".join(vogais_usadas)}')