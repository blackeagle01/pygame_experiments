import pygame

pygame.init()

screen_size=(800,600)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

screen=pygame.display.set_mode(screen_size)


font=pygame.font.SysFont("comicsansms", 34)




def loop():

	global screen ## Need to make screen a global variable

	gameexit=False

	gameover=False



	lead_x=100 
	lead_y=100

	velocity_x=0
	velocity_y=0

	while not gameexit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameexit=True

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					velocity_x=-10
					velocity_y=0
				if event.key==pygame.K_RIGHT:
					velocity_x=10
					velocity_y=0

				if event.key==pygame.K_UP:
					velocity_y=-10
					velocity_x=0
				if event.key==pygame.K_DOWN:
					velocity_y=10
					velocity_x=0


		lead_x+=velocity_x
		lead_y+=velocity_y

		if lead_x>=770:
			gameover=True
		if lead_x<=0:
			gameover=True
		if lead_y>=570:
			gameover=True
		if lead_y<=0:
			gameover=True

		while gameover:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					gameover=False
					gameexit=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_p:
						gameover=False
						lead_x=100
						lead_y=100
						velocity_x=0
						velocity_y=0

			output=font.render('You lose,press P to play again',True,red)
			screen.blit(output,(100,100))
			pygame.display.update()
			




		screen.fill(black)
		pygame.draw.rect(screen,white,[lead_x,lead_y,30,30])
		pygame.display.update()

if __name__ == '__main__':
	loop()