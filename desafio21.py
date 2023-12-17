#ABRIR E REPRODUZIR UM ARQUIVO MP3
import pygame
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
