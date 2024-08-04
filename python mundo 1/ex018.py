import math

angulo = int(input('Digite o ângulo: '))
angulos_validos = [30, 40, 45]

if angulo not in angulos_validos:
    print('Ângulo inválido')
else:
    angulo_rad = math.radians(angulo)

    coseno = math.cos(angulo_rad)
    seno = math.sin(angulo_rad)
    tangente = math.tan(angulo_rad)

    print(f'Ângulo: {angulo} graus')
    print(f'Cosseno: {coseno:.4f}')
    print(f'Seno: {seno:.4f}')
    print(f'Tangente: {tangente:.4f}')
