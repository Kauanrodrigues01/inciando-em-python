def contar(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim and passo < 0 or inicio > fim and passo > 0: # Se o início for menor que o fim e o passo for negativo ou se o início for maior que o fim e o passo for positivo, inverte o passo
        passo = -passo
    
    if passo > 0:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim-1, passo):
            print(i, end=' ')

incio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('passo: '))

contar(incio, fim, passo)