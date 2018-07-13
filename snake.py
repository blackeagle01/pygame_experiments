import pygame
import random

pygame.init()


#colors
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)


screen=pygame.display.set_mode((800,600))





class Snake(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.body=[[x,y]]

		self.block_size=10
		self.velocity_x=0
		self.velocity_y=0
		self.length=1

	def set_speed_x(self,speed):
		self.velocity_x=speed
		self.velocity_y=0
		
	def set_speed_y(self,speed):
		self.velocity_y=speed
		self.velocity_x=0		
		
	def move(self):
		global gameexit
		self.x+=self.velocity_x
		self.y+=self.velocity_y

		if self.x>=800 or self.x<=0 or self.y>=600 or self.y<=0:
			gameover=True

		'''for [self.x,self.y] in self.body:
			gameexit=True'''


		self.body.append([self.x,self.y])

		if len(self.body)>self.length:
			del self.body[0]


	def draw(self):
		global screen
		for pos in self.body:
			pygame.draw.rect(screen,white,[pos[0],pos[1],self.block_size,self.block_size])

	def collide(self,apple):
		if abs(self.x-apple.x)<9 and abs(self.y-apple.y)<9:
			return True
		else:
			return False
			






class Apple(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.block_size=10

	def draw(self):
		global screen
		pygame.draw.rect(screen,red,[self.x,self.y,self.block_size,self.block_size])





gameexit=False

snake=Snake(100,100)
apple=Apple(random.randrange(0,700),random.randrange(0,500))

clock=pygame.time.Clock()
fps=30


while not gameexit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameexit=True

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				snake.set_speed_x(-10)
			if event.key==pygame.K_RIGHT:
				snake.set_speed_x(10)
			if event.key==pygame.K_UP:
				snake.set_speed_y(-10)
			if event.key==pygame.K_DOWN:
				snake.set_speed_y(10)

	snake.move()

	if snake.collide(apple):
		apple.x=random.randrange(0,700)
		apple.y=random.randrange(0,500)
		snake.length+=1

	screen.fill(black)
	snake.draw() 
	apple.draw()
	pygame.display.update()
	clock.tick(fps)




