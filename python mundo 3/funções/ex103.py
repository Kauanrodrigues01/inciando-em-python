def exibir_dados_jogador(nome='<desconhecido>', gols='0'):
    nome = nome.strip()
    gols = gols.strip()
    
    if gols == '':
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isdigit():
        gols = 0
    
    print(f'O Jogador {nome} fez {gols} gol(s)')

exibir_dados_jogador('   ', 'tres')