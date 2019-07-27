# Simon
import pygame, sys, random, time
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Simon')
fpsClock = pygame.time.Clock()
fpsClock.tick(60)

#Storing
pattern = [] #color pattern
score = 0    #

#Colors
white        = (255, 255, 255)
black        = (0, 0, 0)

yellow       = (155, 155, 0)
yellow_light = (255, 255, 0)
blue         = (0, 0, 155)
blue_light   = (0, 0, 255)
red          = (155, 0, 0)
red_light    = (255, 0, 0)
green        = (0, 128, 0)
green_light  = (0, 255, 0)
screen_color = black

#Text
font1 = pygame.font.Font('freesansbold.ttf', 46)
font2 = pygame.font.Font('freesansbold.ttf', 18)

titleText = font1.render('Simon', True, black, white)
titleRect = titleText.get_rect()
titleRect.center = (350, 100)

introText = font2.render('Press ENTER to begin.', True, white, black)
introRect = introText.get_rect()
introRect.center = (350, 350)

directionsText = font2.render('Use the arrow keys to repeat the pattern on the screen.', True, white, black)
directionsRect  = directionsText.get_rect()
directionsRect.center = (350, 310)

scoreText = font2.render('Score:', True, white, black)
scoreRect = scoreText.get_rect()
scoreRect.center = (550, 30)

intro_pic = 'Users/s.miles1313/Desktop/images.png'

#Buttons
yellow_rect = pygame.Rect(300, 100, 100, 100)
#pygame.draw.rect(DISPLAY, yellow, yellow_rect)

blue_rect   = pygame.Rect(300, 250, 100, 100)
#pygame.draw.rect(DISPLAY, blue, blue_rect)

red_rect    = pygame.Rect(450, 250, 100, 100)
#pygame.draw.rect(DISPLAY, red, red_rect)

green_rect  = pygame.Rect(150, 250, 100, 100)
#pygame.draw.rect(DISPLAY, green, green_rect)

patternspeed = 450 #milliseconds
patterndelay = 200

def quit():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

def beginning():

		#DISPLAY.fill(black)
		DISPLAY.blit(titleText, titleRect)
		DISPLAY.blit(introText, introRect)
		DISPLAY.blit(directionsText, directionsRect)
		while True:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_RETURN:
						format()
						break
				elif event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	#pygame.image.load(intro_pic)
	#DISPLAY.blit(intro_pic,(300, 200))
	#pygame.display.update()

def format():
	DISPLAY.fill(screen_color)

	pygame.draw.rect(DISPLAY, yellow, yellow_rect)
	pygame.draw.rect(DISPLAY, blue, blue_rect)
	pygame.draw.rect(DISPLAY, red, red_rect)
	pygame.draw.rect(DISPLAY, green, green_rect)

	DISPLAY.blit(scoreText, scoreRect)


#def light_buttons(color):
	#if color == yellow:



#def main():






beginning()
quit()




