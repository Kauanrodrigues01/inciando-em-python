import os
import random
from colorama import Fore, Style, Back
import time

jogarNovamente = 's'
jogadas = 0
quem_joga = 2  # 1 = CPU e 2 = Jogador
max_jogadas = 9

velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def tela():
    global velha
    global jogadas
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"    0   1   2")
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print(f"Jogadas: {Fore.GREEN}{str(jogadas)}{Style.RESET_ALL}")

def jogadorJoga():
    global jogadas
    global quem_joga
    global max_jogadas
    global velha
    
    if quem_joga == 2 and jogadas < max_jogadas:
        try:
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))

            if not (0 <= linha <= 2) or not (0 <= coluna <= 2):
                raise ValueError("Linha e coluna devem estar entre 0 e 2.")
            
            if velha[linha][coluna] != ' ':
                raise ValueError("Esta posição já foi escolhida.")

            velha[linha][coluna] = 'X'
            quem_joga = 1
            jogadas += 1

        except ValueError as ve:
            print(f'{Fore.RED}ERRO: {ve}{Fore.RESET}')
            input("Pressione ENTER para continuar...")
        except Exception as e:
            print(f'{Fore.RED}ERRO: {e}{Fore.RESET}')
            input("Pressione ENTER para continuar...")

def cpuJoga():
    global jogadas
    global quem_joga
    global max_jogadas
    global velha
    
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if velha[linha][coluna] == ' ':
            velha[linha][coluna] = 'O'
            quem_joga = 2
            jogadas += 1
            break

def verificar_vitoria():
    for i in range(3):
        # Verifica linhas
        if velha[i][0] == velha[i][1] == velha[i][2] != ' ':
            return velha[i][0]
        
        # Verifica colunas
        if velha[0][i] == velha[1][i] == velha[2][i] != ' ':
            return velha[0][i]
    
    # Verifica diagonais
    if velha[0][0] == velha[1][1] == velha[2][2] != ' ':
        return velha[0][0]
    if velha[0][2] == velha[1][1] == velha[2][0] != ' ':
        return velha[0][2]
    
    return None

def verificar_empate():
    for linha in velha:
        if ' ' in linha:
            return False  # Se encontrar um espaço vazio, o jogo não terminou em empate
    return True  # Se não houver espaços vazios, é um empate

while True:
    tela()
    jogadorJoga()
    vencedor = verificar_vitoria()
    if vencedor:
        tela()
        if vencedor == 'Empate':
            print(f"{Fore.YELLOW}Empate!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}O jogador {vencedor} venceu!{Style.RESET_ALL}")
        break

    if verificar_empate():
        tela()
        print(f"{Fore.YELLOW}Empate!{Style.RESET_ALL}")
        break

    cpuJoga()
    vencedor = verificar_vitoria()
    if vencedor:
        tela()
        if vencedor == 'Empate':
            print(f"{Fore.YELLOW}Empate!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}A CPU venceu!{Style.RESET_ALL}")
        break

    if verificar_empate():
        tela()
        print(f"{Fore.YELLOW}Empate!{Style.RESET_ALL}")
        break