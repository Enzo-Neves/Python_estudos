import pygame 
from pygame.mixer import Sound
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Escuto?')
pygame.event.wait()
