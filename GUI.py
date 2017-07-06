import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

img = pygame.image.load('Chutes&Ladders1.gif')
while not done:
	screen.blit(img, (0,0))
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			done = True
		pygame.display.flip()
	


