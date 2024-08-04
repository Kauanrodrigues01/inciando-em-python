import pygame

# Inicializar o mixer
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load("./ex021.mp3")

# Reproduzir o áudio
pygame.mixer.music.play()

# Esperar até que o áudio termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
