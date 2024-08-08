import re #Regex, expressões regulares

texto = 'Curso de Python do CFB Cursos, canal do youtube'

# o FINDALL retorna uma lista com todas as ocorrências
res = re.findall(r'Python', texto) #Procura a palavra Python no texto
print(res, "quantidade de ocorrências: ", len(res)) #Retorna a palavra encontrada


# o SEARCH retorna um objeto com a primeira ocorrência
res = re.search(r'Python', texto) #Procura a palavra Python no texto
pi = res.start() #Retorna a posição inicial da palavra encontrada
pf = res.end() #Retorna a posição final da palavra encontrada
tam = pf - pi #Retorna o tamanho da palavra encontrada
print(texto[pi:pf]) #Retorna a palavra encontrada
print(res.group()) #Retorna a palavra encontrada
print(pi, pf, tam) #Retorna a posição inicial, final e o tamanho da palavra encontrada


# o SPLIT retorna uma lista com as palavras separadas pelo padrão
res = re.split(r'Python', texto) #Procura a palavra Python no texto e separa as palavras
print(res) #Retorna a palavra encontrada


# o SUB substitui o padrão por outra string
res = re.sub(r'Python', 'Android', texto) #Procura a palavra Python no texto e substitui por Android
res = re.sub('\s', '--', res) #Substitui os espaços por --
print(res)