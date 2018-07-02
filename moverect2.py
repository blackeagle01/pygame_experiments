import pygame
import random

pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)


gamecrash=False
display_dim=(800,600)
screen=pygame.display.set_mode(display_dim)
fps=30





class Snake:
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height



class Apple:
	def __init__(self,dim):
		self.x=dim[0]
		self.y=dim[1]

		self.width=7
		self.height=7




snake=Snake(300,300,20,20)
change_x=0
change_y=0



clock=pygame.time.Clock()

apple_x=random.randint(0,700)
apple_y=random.randint(0,500)


apple=Apple((apple_x,apple_y))

while not gamecrash:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gamecrash=True

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				change_x= -10
				change_y=0

			elif event.key==pygame.K_RIGHT:
				change_x= 10
				change_y=0

			elif event.key==pygame.K_UP:
				change_y=-10
				change_x=0

			elif event.key==pygame.K_DOWN:
				change_y=10
				change_x=0

	prev_x=snake.x
	prev_y=snake.y
	snake.x+=change_x
	snake.y+=change_y

	if snake.x>=800:

		snake.x=10

	if snake.x<=0:
		snake.x=800

	if snake.y>=600:
		snake.y=10

	if snake.y<=0:
		snake.y=600
	
	

	

	if abs(snake.x-apple.x)<=7 and abs(snake.y-apple.y)<=7:
		pygame.draw.rect(screen,black,[apple.x,apple.y,apple.width,apple.height])
		apple.x=random.randint(0,700)
		apple.y=random.randint(0,500)

	pygame.draw.rect(screen,red,[apple.x,apple.y,apple.width,apple.height])

	pygame.draw.rect(screen,black,[prev_x,prev_y,snake.width,snake.height])



	pygame.draw.rect(screen,white,[snake.x,snake.y,snake.width,snake.height])
	pygame.display.update()

	clock.tick(fps)
