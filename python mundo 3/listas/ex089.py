alunos = list()
while True:
    nome = input('Nome: ').strip()
    nota1 = input('Nota 1: ').strip()
    nota2 = input('Nota 2: ').strip()
    nota3 = input('Nota 3: ').strip()
    
    if nota1.replace('.', '').replace(',', '').isdigit() and nota2.replace('.', '').replace(',', '').isdigit() and nota3.replace('.', '').replace(',', '').isdigit():
        
        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        aluno = [nome, [nota1, nota2, nota3]]
        alunos.append(aluno[:])
        
        r = input('Quer continuar[S/N]? ').strip().upper()
    else:
        print()
        print('Você digitou algum valor invalido, insira os valores novamente.')
    
    if r != 'S':
        break

if alunos:
    print()
    print(f'{'N0.':<5} {'NOME':<15} {'Média'}')
    print('-'*40)
    for i in range(len(alunos)):
        nome = alunos[i][0]
        notas = alunos[i][1]
        soma_notas = 0
        for nota in notas:
            soma_notas += nota
        media = soma_notas / len(notas)
        media_str = str(media)
        print(f'{i:<5} {nome:<15} {media_str}')