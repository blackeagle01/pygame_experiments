import pygame
import random
import math

pygame.init()


screen=pygame.display.set_mode((600,600))
exit=False

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

fps=10
inside=0
total=0

clock=pygame.time.Clock()

font=pygame.font.SysFont("comicsansms", 34)


while not exit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit=True

	screen.fill(black,[100,500,500,400])

	pygame.draw.rect(screen,white,[100,100,300,300],1)
	pygame.draw.circle(screen,white,(250,250),150,1)

	x=random.randint(100,400)
	y=random.randint(100,400)

	pygame.draw.rect(screen,red,[x,y,1,1])

	if math.sqrt((x-250)**2+(y-250)**2)<=150:
		inside+=1
	total+=1

	text='pi = {}'.format(4*(inside/total))

	output=font.render(text[:10], True,red)

	screen.blit(output,(100,500))




	pygame.display.update()

	clock.tick(fps)







