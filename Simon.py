# Simon
import pygame, sys, random, time
from pygame.locals import *

#Sets Pygame window and main function
pygame.init()
DISPLAY = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Simon')
fpsClock = pygame.time.Clock()
game_time = fpsClock.tick(60)


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

#Different sized fonts
font1 = pygame.font.Font('freesansbold.ttf', 50)
font2 = pygame.font.Font('freesansbold.ttf', 20)
font3 = pygame.font.Font('freesansbold.ttf', 34)

#Title of the game displayed
titleText = font1.render('Simon', True, black, white)
titleRect = titleText.get_rect()
titleRect.center = (350, 230)

#Start game button
startText = font3.render(' Start ', True, white, black) 
startRect = startText.get_rect()
startRect.center = (100, 70)

#Exit game button
exitText = font3.render(' Exit ', True, white, black) 
exitRect = exitText.get_rect()
exitRect.center = (600, 70)

#How to play game directions
directionsText = font2.render(' Use the arrow keys to repeat the pattern on the screen. ', True, black, white) 
directionsRect  = directionsText.get_rect()
directionsRect.center = (350, 330)

#Button to click to begin playing and first pattern
playText = font2.render(' Begin Playing ', True, black, white) 
playRect = playText.get_rect()
playRect.center = (350, 400)

#Shows when player repeats pattern correctly
correctText = font2.render('Correct!', True, white, black) 
correctRect = correctText.get_rect()
correctRect.center = (150, 100)

#Shows when the player's pattern is incorrect
incorrectText = font2.render('Incorrect.', True, white, black) 
incorrectRect = incorrectText.get_rect()
incorrectRect.center = (350, 450)

#Click to go to next "level" when previous was completed
levelText = font3.render(' Next Level ', True, blue, white) 
levelRect = levelText.get_rect()
levelRect.center = (350, 420)

#Play Again Button at end of game
playagainText = font3.render(' Play Again ', True, black, white) 
playagainRect = playagainText.get_rect()
playagainRect.center = (120,70)

#Exit Button at end of game
exit2Text = font3.render(' Exit ', True, black, white) 
exit2Rect = exit2Text.get_rect()
exit2Rect.center = (600, 70)

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

def simon_beginning():
	game_quit()
	DISPLAY.fill(white)

	DISPLAY.blit(titleText, titleRect)
	DISPLAY.blit(startText, startRect) #startRect == rect(52, 53, 97, 35)
	DISPLAY.blit(exitText, exitRect)  #exitRect == rect(558, 53, 85, 35)
	DISPLAY.blit(directionsText, directionsRect)
	pygame.display.update()

	#Will check to see if one of the buttons(or red x) has been clicked to move on
	x = True 
	while x == True:
		game_quit()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousey = pygame.mouse.get_pos()
				#If the startRect is clicked
				if 52 + 97 > mousey[0] > 52 and 53 + 35 > mousey[1] > 53:
					button_format() 
					x = False

					#If the exit button is clicked
				elif 558 + 85 > mousey[0] > 558 and 53 + 35 > mousey[1] > 53: 
					pygame.quit()
					sys.exit()

#Draws the original 4 buttons
def button_format():
	game_quit()
	DISPLAY.fill(screen_color)

	#All the rectangles start off white to make flash very visible
	yellow_rect = pygame.draw.rect(DISPLAY, white, top_mid)
	blue_rect  = pygame.draw.rect(DISPLAY, white, bottom_mid)
	red_rect = pygame.draw.rect(DISPLAY, white, bottom_right)
	green_rect  = pygame.draw.rect(DISPLAY, white, bottom_left)
	pygame.display.update()

#Checks to see if the "Begin Playing" button is clicked to continue. Makes sure player is ready.
def simon_play():
	#game_quit()
	DISPLAY.blit(playText, playRect) #playRect == rect(277, 390, 147, 21)
	pygame.display.update()
	#game_quit()

	p = True
	while p == True:
		game_quit()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousey = pygame.mouse.get_pos()
				#If playRect is clicked
				if 277 + 147 > mousey[0] > 277 and 390 + 21 > mousey[1] > 390: 
					pygame.draw.rect(DISPLAY, black, playRect)
					pygame.display.update()
		
					p = False



#Lights button with delay when computer is generating patttern
def light_buttons(color): 
		#yellow
		if color == 'y':

			last = pygame.time.get_ticks()
			#Makes light flash longer & visible
			while (pygame.time.get_ticks() - last < 800): 
				yellow_rect = pygame.draw.rect(DISPLAY, yellow_light, top_mid)
				pygame.display.update(yellow_rect)

				pygame.time.delay(500)
				pygame.event.pump()
	
			yellow_rect = pygame.draw.rect(DISPLAY, white, top_mid)
			pygame.display.update(yellow_rect)
			game_quit()
				

		#blue
		elif color == 'b':

			last = pygame.time.get_ticks()
 			# ms need to be greater than pygame.time.delay() ms
			while (pygame.time.get_ticks() - last < 800): 
				blue_rect  = pygame.draw.rect(DISPLAY, blue_light, bottom_mid)
				pygame.display.update(blue_rect)

				pygame.time.delay(500)
				pygame.event.pump()
	
			blue_rect  = pygame.draw.rect(DISPLAY, white, bottom_mid)
			pygame.display.update(blue_rect)
			game_quit()
			
		#red
		elif color == 'r':
			
			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 800):
				red_rect = pygame.draw.rect(DISPLAY, red_light, bottom_right)
				pygame.display.update(red_rect)
			
				pygame.time.delay(500)
				pygame.event.pump()
			
			red_rect = pygame.draw.rect(DISPLAY, white, bottom_right)
			pygame.display.update(red_rect)
			game_quit()
		
		#green
		elif color == 'g':

			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 800):
				green_rect  = pygame.draw.rect(DISPLAY, green_light, bottom_left)
				pygame.display.update(green_rect)
				
				pygame.time.delay(500)
				pygame.event.pump()

			green_rect  = pygame.draw.rect(DISPLAY, white, bottom_left)
			pygame.display.update(green_rect)
			game_quit()



#Lights buttons when player clicks or presses keys with NO DELAY
def player_buttons(button): 
		#yellow
		if button == 'y':

			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 400):
				yellow_rect = pygame.draw.rect(DISPLAY, yellow_light, top_mid)
				pygame.display.update(yellow_rect)
			
				pygame.event.pump()

			yellow_rect = pygame.draw.rect(DISPLAY, white, top_mid)
			pygame.display.update(yellow_rect)
			game_quit()
			

		#blue
		elif button == 'b':

			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 400):
				blue_rect  = pygame.draw.rect(DISPLAY, blue_light, bottom_mid)
				pygame.display.update(blue_rect)

				pygame.event.pump()

			blue_rect  = pygame.draw.rect(DISPLAY, white, bottom_mid)
			pygame.display.update(blue_rect)
			game_quit()
			

		#red
		elif button == 'r':
		
			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 400):
				red_rect = pygame.draw.rect(DISPLAY, red_light, bottom_right)
				pygame.display.update(red_rect)

				pygame.event.pump()
		
			red_rect = pygame.draw.rect(DISPLAY, white, bottom_right)
			pygame.display.update(red_rect)
			game_quit()
		

		#green
		elif button == 'g':
			
			last = pygame.time.get_ticks()

			while (pygame.time.get_ticks() - last < 400):
				green_rect  = pygame.draw.rect(DISPLAY, green_light, bottom_left)
				pygame.display.update(green_rect)
				
				pygame.event.pump()

			green_rect  = pygame.draw.rect(DISPLAY, white, bottom_left)
			pygame.display.update(green_rect)
			game_quit()



#End screen for the game
def simon_end():
	game_quit()

	DISPLAY.fill(black) #Provides new slate/blank screen
	DISPLAY.blit(incorrectText, incorrectRect)
	DISPLAY.blit(exit2Text, exit2Rect)
	DISPLAY.blit(playagainText, playagainRect)

	endscoreText = font3.render('Your score is ' + str(score) + '.', True, white, black)
	endscoreRect = endscoreText.get_rect()
	endscoreRect.center = (350, 200)
	DISPLAY.blit(endscoreText, endscoreRect)

	pygame.display.update()
	game_quit()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousey = pygame.mouse.get_pos()
			#If the playagainRect is clicked
			if 22 + 196 > mousey[0] > 22 and 52 + 36 > mousey[1] > 52: 
				button_format() 
				simon_main()
			#If the exit button is clicked
			elif 558 + 85 > mousey[0] > 558 and 53 + 35 > mousey[1] > 53:
				pygame.quit()
				sys.exit()


#Checks to see if red x (to close the window) is clicked. Will exterminate program if it was clicked.
def game_quit():
	for event in pygame.event.get(QUIT): 
		pygame.quit()
		sys.exit()


#Puts all the 'mini' functions in here to make whole game
def simon_main():

	simon_beginning()
	simon_play()
	game_quit()

	

	#Storing

	pattern = [] # color pattern
	player_pattern = [] # player's pattern 

	global score
	score = 0    # player's score

	wait_for_input = False # true when player has to repeat pattern
	color_choices = ['y','b','r','g'] # different colors
	

	#main game loop
	while True:
		game_quit()

		button = None

		scoreText = font2.render('Score: ' + str(score), True, white, black)
		scoreRect = scoreText.get_rect()
		scoreRect.center = (550, 30)
		DISPLAY.blit(scoreText, scoreRect)

		#Computer pattern (if player is not repeating)
		if wait_for_input == False:

			player_pattern.clear()
			pattern.append(random.choice(color_choices))
			for color in pattern:
				light_buttons(color)
				wait_for_input = True
				

		#Player's turn to repeat pattern
		else:
			#loop for if player is still not done repeating pattern
			while len(player_pattern) != len(pattern):
				game_quit()

				
				for event in pygame.event.get():
					#checks for keyboard arrow key presses
					if event.type == KEYDOWN:
						if event.key == K_UP:
							button = 'y'					#yellow						
							player_pattern.append('y')
							player_buttons(button)							
						elif event.key == K_DOWN:
							button = 'b'					#blue					
							player_pattern.append('b')
							player_buttons(button)							
						elif event.key == K_LEFT:
							button = 'g'					#green				
							player_pattern.append('g')
							player_buttons(button)							
						elif event.key == K_RIGHT:
							button = 'r'					#red						
							player_pattern.append('r')
							player_buttons(button)


					#checks for mouse or mousepad clicks on buttons
					elif event.type == pygame.MOUSEBUTTONDOWN:
						mousey = pygame.mouse.get_pos()
						#yellow
						if  300 + 100 > mousey[0] > 300 and 100 + 100 > mousey[1] > 100:
							button = 'y'							
							player_pattern.append('y')
							player_buttons(button)	

						#blue
						elif 300 + 100 > mousey[0] > 300 and 250 + 100 > mousey[1] > 250:
							button = 'b'							
							player_pattern.append('b')
							player_buttons(button)	

						#green
						elif 450 + 100 > mousey[0] > 450 and 250 + 100 > mousey[1] > 250:
							button = 'r'							
							player_pattern.append('r')
							player_buttons(button)	

						#red
						elif 150 + 100 > mousey[0] > 150 and 250 + 100 > mousey[1] > 250:
							button = 'g'							
							player_pattern.append('g')
							player_buttons(button)	
			
			#if the player repeated the pattern correctly
			if player_pattern == pattern:
				DISPLAY.blit(correctText, correctRect)
				#rect(111, 90, 79, 21)
				DISPLAY.blit(levelText, levelRect)
				#score += 1
				#pygame.display.update()
				game_quit()

				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						mousey = pygame.mouse.get_pos()
						#if the "Next Level" button is clicked
						if 255 + 190 > mousey[0] > 255 and 403 + 35 > mousey[1] > 403:
							score += 1
							pygame.draw.rect(DISPLAY, black, (255, 403, 190, 35))
							pygame.draw.rect(DISPLAY, black, (111, 90, 79, 21)) #Covers the "Correct!" once move on to next level

							wait_for_input = False

			#if the player repeated the pattern incorrectly
			elif player_pattern != pattern:
				simon_end()
			pygame.display.update()

	pygame.display.update()




simon_main()

