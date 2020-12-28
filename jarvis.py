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
	screen.blit( font.render("HEHEHEHE ",True,(255, 0, 0)), (350,100))
	screen.blit( font.render("KARO DEBUG ",True,(255, 0, 0)), (350,120))
	screen.blit( font.render("AND FOR CLASSIC RICKROLL I HAVE NOT ADDED QUIT OPTION SO...(TASK MANAGER) ",True,(255, 0, 0)), (50,140))
	screen.blit( font.render("NEVER GONNA GIVE UP RICK ROLLING ITS TOO MUCH FUN ",True,(255, 0, 0)), (100,160))
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_over = True
				is_running = False

	pygame.display.update()