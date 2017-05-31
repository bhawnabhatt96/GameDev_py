import pygame,sys


def process(bug):

	#PROCESS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 
			pygame.display.quit()
			pygame.quit()
			sys.exit()
	#keyboard keys
	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]:
		bug.image = pygame.image.load("images/pen2.png")
		bug.velx = 5

	elif keys[pygame.K_a]:
		bug.image = pygame.image.load("images/pen1.png")
		bug.velx = -5
	else:
		bug.velx = 0

#for more keys pygame.org/docs

