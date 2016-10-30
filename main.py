#The main file where all the code goes
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640,380])

endGame = False

while not endGame:
	for event in pygame.events.get():
		if event.type == pygame.event.QUIT:
			sys.exit()
