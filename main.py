import pygame
import pygame.freetype

from pygame import Rect

pygame.init()

SIZE = (700, 480)
screen = pygame.display.set_mode(SIZE)

# all fonts
FONT_LARGE = pygame.freetype.Font("PulpenSnowman.ttf", 40)
FONT_MEDIUM = pygame.freetype.Font("PulpenSnowman.ttf", 25)
FONT_SMALL = pygame.freetype.Font("PulpenSnowman.ttf", 15)

# all colours
BLACK = (0, 0, 0)
DARK_BLUE = (50, 131, 168)
LIGHT_BLUE = (88, 139, 161)
LIGHT_GREY = (204, 198, 196)
GREEN = (119, 189, 159)
BLUE = (148, 210, 215)
ORANGE = (254, 95, 1)
PURPLE = (201, 67, 155)
YELLOW = (254, 225, 0)
RED = (254, 27, 6)
OFF_WHITE = (230, 230, 230)

# mouseX and mouseY
mx = 0
my = 0

# variables for guess board balls for collide
guess_area1 = Rect(422, 114, 32, 32)
guess_area2 = Rect(474, 114, 32, 32)
guess_area3 = Rect(526, 114, 32, 32)
guess_area4 = Rect(578, 114, 32, 32)

# variables for colours board balls for collide
colours_area1 = Rect(369, 410, 32, 32)
colours_area2 = Rect(422, 410, 32, 32)
colours_area3 = Rect(474, 410, 32, 32)
colours_area4 = Rect(526, 410, 32, 32)
colours_area5 = Rect(578, 410, 32, 32)
colours_area6 = Rect(629, 410, 32, 32)

# guess_counter keeps track of which guess slot is filled
guess_counter = 0

# assigns initial colours for guess board balls
guess_colour_change = LIGHT_GREY
guess_area1_colour = LIGHT_GREY
guess_area2_colour = LIGHT_GREY
guess_area3_colour = LIGHT_GREY
guess_area4_colour = LIGHT_GREY

# variable for indicator
indicator_x = 433

def drawBackground():
  # background
  pygame.draw.rect(screen, DARK_BLUE, (240, 0, 460, 480))
  pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 240, 480))

  # guess titles
  FONT_LARGE.render_to(screen, (460, 50), "Guess #1", BLACK)
  FONT_MEDIUM.render_to(screen, (295, 116), "Your Guess:", BLACK)
  FONT_MEDIUM.render_to(screen, (415, 245), "Make your next guess.", BLACK)

  # guess board
  pygame.draw.rect(screen, LIGHT_GREY, (412, 97, 207, 64))
  pygame.draw.rect(screen, BLACK, (412, 97, 207, 64), 1)
  pygame.draw.line(screen, BLACK, (462, 97), (462, 160))
  pygame.draw.line(screen, BLACK, (515, 97), (515, 160))
  pygame.draw.line(screen, BLACK, (568, 97), (568, 160))

  # colours title
  FONT_MEDIUM.render_to(screen, (273, 415), "Colours:", BLACK)

  # colours board
  pygame.draw.rect(screen, LIGHT_GREY, (359, 393, 312, 65))
  pygame.draw.rect(screen, BLACK, (359, 393, 312, 65), 1)
  pygame.draw.line(screen, BLACK, (410, 393), (410, 457))
  pygame.draw.line(screen, BLACK, (463, 393), (463, 457))
  pygame.draw.line(screen, BLACK, (515, 393), (515, 457))
  pygame.draw.line(screen, BLACK, (568, 393), (568, 457))
  pygame.draw.line(screen, BLACK, (619, 393), (619, 457))

  # colours board balls; outlines and colours
  pygame.draw.ellipse(screen, GREEN, (369, 410, 32, 32))
  pygame.draw.ellipse(screen, BLUE, (422, 410, 32, 32))
  pygame.draw.ellipse(screen, ORANGE, (474, 410, 32, 32))
  pygame.draw.ellipse(screen, PURPLE, (526, 410, 32, 32))
  pygame.draw.ellipse(screen, YELLOW, (578, 410, 32, 32))
  pygame.draw.ellipse(screen, RED, (629, 410, 32, 32))
  pygame.draw.ellipse(screen, BLACK, (369, 410, 32, 32), 1)
  pygame.draw.ellipse(screen, BLACK, (422, 410, 32, 32), 1)
  pygame.draw.ellipse(screen, BLACK, (474, 410, 32, 32), 1)
  pygame.draw.ellipse(screen, BLACK, (526, 410, 32, 32), 1)
  pygame.draw.ellipse(screen, BLACK, (578, 410, 32, 32), 1)
  pygame.draw.ellipse(screen, BLACK, (629, 410, 32, 32), 1)

  # past guesses titles
  FONT_MEDIUM.render_to(screen, (55, 25), "Past Guesses", BLACK)
  FONT_SMALL.render_to(screen, (168, 402), "C: 0  W: 0", BLACK)

  # past guesses board
  pygame.draw.rect(screen, LIGHT_GREY, (7, 383, 155, 48))
  pygame.draw.rect(screen, BLACK, (7, 383, 155, 48), 1)
  pygame.draw.line(screen, BLACK, (44, 383), (44, 430))
  pygame.draw.line(screen, BLACK, (83, 383), (83, 430))
  pygame.draw.line(screen, BLACK, (122, 383), (122, 430))

  # past guesses board balls; outlines
  pygame.draw.ellipse(screen, BLACK, (14, 396, 23, 23), 1)
  pygame.draw.ellipse(screen, BLACK, (53, 396, 23, 23), 1)
  pygame.draw.ellipse(screen, BLACK, (92, 396, 23, 23), 1)
  pygame.draw.ellipse(screen, BLACK, (131, 396, 23, 23), 1)

# draws guess balls if colours are selected
def ifMouseClicked():
  global colours_area1, colours_area2, colours_area3, colours_area4, colours_area5, colours_area6, guess_area1_colour, guess_area2_colour, guess_area3_colour, guess_area4_colour, guess_counter

  if button == 1:
    if colours_area1.collidepoint(mx, my) or colours_area2.collidepoint(mx, my) or colours_area3.collidepoint(mx, my) or colours_area4.collidepoint(mx, my) or colours_area5.collidepoint(mx, my) or colours_area6.collidepoint(mx, my):
      pygame.draw.ellipse(screen, guess_area1_colour, (422, 114, 32, 32))
      pygame.draw.ellipse(screen, guess_area2_colour, (474, 114, 32, 32))
      pygame.draw.ellipse(screen, guess_area3_colour, (526, 114, 32, 32))
      pygame.draw.ellipse(screen, guess_area4_colour, (578, 114, 32, 32))

def drawScene(screen, button, mx, my):
  global colours_area1, colours_area2, colours_area3, colours_area4, colours_area5, colours_area6, guess_counter, guess_colour_change, guess_area1_colour, guess_area2_colour, guess_area3_colour, guess_area4_colour, guess_area1, guess_area2, guess_area3, guess_area4, indicator_x, OFF_WHITE

  # changes colour of guess depending on colours ball clicked
  if button == 1:
    if colours_area1.collidepoint(mx, my):
      guess_colour_change = GREEN
      ifMouseClicked()
      guess_counter += 1
    elif colours_area2.collidepoint(mx, my):
      guess_colour_change = BLUE
      ifMouseClicked()
      guess_counter += 1
    elif colours_area3.collidepoint(mx, my):
      guess_colour_change = ORANGE
      ifMouseClicked()
      guess_counter += 1
    elif colours_area4.collidepoint(mx, my):
      guess_colour_change = PURPLE
      ifMouseClicked()
      guess_counter += 1
    elif colours_area5.collidepoint(mx, my):
      guess_colour_change = YELLOW
      ifMouseClicked()
      guess_counter += 1
    elif colours_area6.collidepoint(mx, my):
      guess_colour_change = RED
      ifMouseClicked()
      guess_counter += 1

  # guess_counter is reset if the guess areas are clicked on
  if button == 1:
    if guess_area1.collidepoint(mx, my):
      guess_counter = 1
    elif guess_area2.collidepoint(mx, my):
      guess_counter = 2
    elif guess_area3.collidepoint(mx, my):
      guess_counter = 3
    elif guess_area4.collidepoint(mx, my):
      guess_counter = 4
  
  # records guess by changing colour of each guess ball
  if guess_counter == 1:
     guess_area1_colour = guess_colour_change
     indicator_x = 433
  elif guess_counter == 2:
    guess_area2_colour = guess_colour_change
    indicator_x = 486
  elif guess_counter == 3:
    guess_area3_colour = guess_colour_change
    indicator_x = 538
  elif guess_counter == 4:
    guess_area4_colour = guess_colour_change
    indicator_x = 590

  # draws circle that indicates which guess slot is selected
  pygame.draw.rect(screen, DARK_BLUE, (422, 170, 578, 10))
  pygame.draw.ellipse(screen, OFF_WHITE, (indicator_x, 170, 9, 9))

  # draws outlines of guess slots
  pygame.draw.ellipse(screen, BLACK, (420, 114, 34, 34), 3)
  pygame.draw.ellipse(screen, BLACK, (474, 114, 34, 34), 3)
  pygame.draw.ellipse(screen, BLACK, (526, 114, 34, 34), 3)
  pygame.draw.ellipse(screen, BLACK, (578, 114, 34, 34), 3)

  if guess_counter > 4:
    guessSubmitted()

def guessSubmitted():
    pygame.draw.ellipse(screen, BLACK, (422, 114, 32, 32))
    pygame.draw.ellipse(screen, BLACK, (474, 114, 32, 32))
    pygame.draw.ellipse(screen, BLACK, (526, 114, 32, 32))
    pygame.draw.ellipse(screen, BLACK, (578, 114, 32, 32))
    
    pygame.draw.ellipse(screen, guess_area1_colour, (50, 400, 20, 20))
    pygame.draw.ellipse(screen, guess_area2_colour, (50, 40, 32, 32))
    pygame.draw.ellipse(screen, guess_area3_colour, (50, 70, 32, 32))
    pygame.draw.ellipse(screen, guess_area4_colour, (50, 100, 32, 32))

drawBackground()

# game Loop
running = True
while running:
  button = 0

  for e in pygame.event.get():

    if e.type == pygame.QUIT:
      running = False

    if e.type == pygame.MOUSEBUTTONDOWN:
      mx, my = e.pos          
      button = e.button

    elif e.type == pygame.MOUSEMOTION:
      mx, my = e.pos 
  
  drawScene(screen, button, mx, my)
  pygame.display.flip()