import pygame,sys
from classes import *
from process import process


pygame.init()

WIDTH,HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0, HEIGHT - 150, 150, 150, "images/pen2.png")
#bug2 = Bug(100, 11, 18, 6, "images/yay.png")
#bug3 = Bug(150, 12, 27, 9, "images/yay.png")
#for_images(png)
img_bug = pygame.image.load("images/pen2.png")
#clr1 = (22, 122, 211) 
#clr2 = (0, 255, 255) 
#clr3 = (0, 128, 128) 
#declare variables
#i = 0
 
while True:
	process(bug)
	

			



	#LOGIC
	bug.motion()
	#bug2.motion()
	#bug3.motion()
	#for flipping screen color 
	#i += 0.1
	#if i > 255:
	#	i %= 255
 

 




	#LOGIC
	#DRAW
	#screenfill
	screen.fill( (0, 0, 0) )
	BaseClass.allsprites.draw(screen)
	#display
	#screen.blit(img, (0.5,0.5))

	

	#pygame.draw.line(screen, clr2, (0 , 0), (640, 360), 10)
	#pygame.draw.rect(screen, clr3, (40, 40, 400, 45))
	#pygame.draw.circle(screen, clr1, (350, 200), 80, 40)


	#DRAW

	clock.tick(FPS)
	pygame.display.flip()




 




 