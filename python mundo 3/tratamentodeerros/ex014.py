import webbrowser

url = 'https://pudim.com.br'

try:
    webbrowser.open(url)
except:
    print('Algo deu errado')
else:
    print('Tudo funcionado')