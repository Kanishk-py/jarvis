import pygame
from pygame import mixer
pygame.init()
mixer.music.load('jarvis-music.mp3')
mixer.music.play(-1)
font = pygame.font.Font('freesansbold.ttf',16)

screen = pygame.display.set_mode((800,600))
is_running=True
while is_running:
	screen.blit(pygame.image.load('download.jpeg'),(250,300))
# 	for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				is_over = True
# 				is_running = False

	pygame.display.update()
