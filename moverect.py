import pygame
pygame.init()

gamecrashed=False

lead_x=300
lead_y=300

black=[0,0,0]
white=(255,255,255)


screen_width=800
screen_height=600
lead_xc=0
lead_yc=0
gamedisplay=pygame.display.set_mode((screen_width,screen_height))

clock=pygame.time.Clock()

pygame.draw.rect(gamedisplay,white,[lead_x,lead_y,40,40])
pygame.display.update()
while not gamecrashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gamecrashed=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				lead_xc=-10
			if event.key==pygame.K_RIGHT:
				lead_xc=10
			if event.key==pygame.K_UP:
				lead_yc=-10
			if event.key==pygame.K_DOWN:
				lead_yc=10
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
				lead_xc=0
				lead_yc=0
	prev_x=lead_x
	prev_y=lead_y
	lead_x+=lead_xc
	lead_y+=lead_yc


	pygame.draw.rect(gamedisplay,black,[prev_x,prev_y,40,40])
	pygame.draw.rect(gamedisplay,white,[lead_x,lead_y,40,40])
	pygame.display.update()

	clock.tick(60)

pygame.quit()