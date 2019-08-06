# Simon
import pygame, sys, random, time
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Simon')
fpsClock = pygame.time.Clock()
fpsClock.tick(60)

#Colors
white        = (255, 255, 255)
black        = (0, 0, 0)

yellow       = (155, 155, 0)
yellow_light = (255, 255, 0,)
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
font3 = pygame.font.Font('freesansbold.ttf', 22)

titleText = font1.render('Simon', True, black, white)
titleRect = titleText.get_rect()
titleRect.center = (350, 100)

introText = font2.render('Press ENTER to begin.', True, white, black)
introRect = introText.get_rect()
introRect.center = (350, 350)

directionsText = font2.render('Use the arrow keys to repeat the pattern on the screen.', True, white, black)
directionsRect  = directionsText.get_rect()
directionsRect.center = (350, 310)

correctText = font2.render('Correct!', True, white, black)
correctRect = correctText.get_rect()
correctRect.center = (350, 420)

incorrectText = font2.render('Incorrect.', True, white, black)
incorrectRect = incorrectText.get_rect()
incorrectRect.center = (350, 420)

averageText = font2.render('Your average is ' + str() + '.', True, white, black)
averageRect = averageText.get_rect()
averageRect.center = (350, 250)


endText1 = font3.render('Do you want to play again?', True, white, black)
endRect1 = endText1.get_rect()
endRect1.center = (350, 400)

endText2 = font2.render('If you do, press "y", otherwise close this window or press "esc" to exit the game.',True, white, black)
endRect2 = endText2.get_rect()
endRect2.center = (350,435)



#scoreText = font2.render('Score:', True, white, black)
#scoreRect = scoreText.get_rect()
#scoreRect.center = (550, 30)

#intro_pic = 'Users/s.miles1313/Desktop/images.png'

#Buttons
top_mid    = pygame.Rect(300, 100, 100, 100)
#yellow_rect = pygame.draw.rect(DISPLAY, yellow, top_mid)

bottom_mid = pygame.Rect(300, 250, 100, 100)
#blue_rect  = pygame.draw.rect(DISPLAY, blue, bottom_mid)

bottom_right = pygame.Rect(450, 250, 100, 100)
#red_rect = pygame.draw.rect(DISPLAY, red, bottom_right)

bottom_left  = pygame.Rect(150, 250, 100, 100)
#green_rect  = pygame.draw.rect(DISPLAY, green, bottom_left)

patternspeed = 450 #milliseconds
patterndelay = 200

#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow

def main():

	format()

	#Storing
	pattern = [] # color pattern
	player_pattern = [] # player's pattern 
	score = 0    # player's score
	wait_for_input = False # true when player has to repeat pattern
	color_choices = ['y','b','r','g'] # different colors

	average = [] # Will need to hold previous scores then find the mean #average.append(score)

	while True:
		#quit()

		button = None

		scoreText = font2.render('Score: ' + str(score), True, white, black)
		scoreRect = scoreText.get_rect()
		scoreRect.center = (550, 30)
		DISPLAY.blit(scoreText, scoreRect)

		quit()

		if wait_for_input == False:
			player_pattern.clear()
			pattern.append(random.choice(color_choices))
			for color in pattern:
				light_buttons(color)
				wait_for_input = True

		else:
			while len(player_pattern) != len(pattern):

				for event in pygame.event.get():
					if event.type == KEYDOWN:
						if event.key == K_UP:
							button = 'y'							
							player_pattern.append('y')
							light_buttons(button)							
						elif event.key == K_DOWN:
							button = 'b'							
							player_pattern.append('b')
							light_buttons(button)							
						elif event.key == K_LEFT:
							button = 'g'							
							player_pattern.append('g')
							light_buttons(button)							
						elif event.key == K_RIGHT:
							button = 'r'							
							player_pattern.append('r')
							light_buttons(button)

			if player_pattern == pattern:
				DISPLAY.blit(correctText, correctRect)
				score += 1
				wait_for_input = False

			elif player_pattern != pattern:
				DISPLAY.blit(incorrectText, incorrectRect)
				end()
				pygame.display.update()
				pygame.quit()
				sys.exit()
			pygame.display.update()

	pygame.display.update()

def quit():
	for event in pygame.event.get(QUIT): 
		pygame.quit()
		sys.exit()
	#while True:
	#	for event in pygame.event.get():
	#		if event.type == QUIT:
	#			pygame.quit()
	#			sys.exit()
	#		else:
	#			break
	#	pygame.display.update()


def beginning():

		#DISPLAY.fill(black)
		DISPLAY.blit(titleText, titleRect)
		DISPLAY.blit(introText, introRect)
		DISPLAY.blit(directionsText, directionsRect)
		while True:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_RETURN:
						main()
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
	
	yellow_rect = pygame.draw.rect(DISPLAY, yellow, top_mid)
	blue_rect  = pygame.draw.rect(DISPLAY, blue, bottom_mid)
	red_rect = pygame.draw.rect(DISPLAY, red, bottom_right)
	green_rect  = pygame.draw.rect(DISPLAY, green, bottom_left)


def light_buttons(color):
	#while True:
		if color == 'y':
			yellow_rect = pygame.draw.rect(DISPLAY, yellow_light, top_mid)
			pygame.display.update()
			#pygame.time.delay(500)
			yellow_rect = pygame.draw.rect(DISPLAY, yellow, top_mid)
			#pygame.time.delay(500)
			pygame.display.update()

		elif color == 'b':
			blue_rect  = pygame.draw.rect(DISPLAY, blue_light, bottom_mid)
			pygame.display.update()
			pygame.time.delay(500)
			blue_rect  = pygame.draw.rect(DISPLAY, blue, bottom_mid)
			pygame.time.delay(500)
			pygame.display.update()

		elif color == 'r':
			red_rect = pygame.draw.rect(DISPLAY, red_light, bottom_right)
			pygame.display.update()
			pygame.time.delay(500)
			red_rect = pygame.draw.rect(DISPLAY, red, bottom_right)
			pygame.time.delay(500)
			pygame.display.update()

		elif color == 'g':
			green_rect  = pygame.draw.rect(DISPLAY, green_light, bottom_left)
			pygame.display.update()
			pygame.time.delay(500)
			green_rect  = pygame.draw.rect(DISPLAY, green, bottom_left)
			pygame.time.delay(500)
			pygame.display.update()






		 #pygame.display.update()


def end():
	#pygame.time.delay(300)
	DISPLAY.fill(screen_color)

	#DISPLAY.blit(scoreText,(325, 225))

	#DISPLAY.blit(averageText, averageRect)
	DISPLAY.blit(endText1, endRect1)
	DISPLAY.blit(endText2, endRect2)
	quit()
	pygame.display.update()




beginning()
#main()
#end()

#/////////////////////////////////////////////////////////
#last = pygame.time.get_ticks()

#yellow_rect = pygame.draw.rect(DISPLAY, yellow, top_mid)
#blue_rect  = pygame.draw.rect(DISPLAY, blue, bottom_mid)
#red_rect = pygame.draw.rect(DISPLAY, red, bottom_right)
#green_rect  = pygame.draw.rect(DISPLAY, green, bottom_left)
#pygame.display.update()
#pygame.time.delay(1000)

#print (last)

#///////////////////
#yellow_rect = pygame.draw.rect(DISPLAY, yellow_light, top_mid)
#pygame.display.update()


