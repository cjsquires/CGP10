import pygame, sys, time, random
from pygame.locals import *
#setup pygame
pygame.init()
mainClock = pygame.time.Clock()
#setup window
WINDOWHEIGHT = 900
WINDOWWIDTH = 900
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('the experiment')
class Daedalus:
    hp = 200
    asgard = 50
    railgun = 10
    shield = 100

red = Daedalus()

green = Daedalus()

blue = Daedalus()

yellow = Daedalus()

pink = Daedalus()

black = Daedalus()

click = False

MOVESPEED = 5

MousePos=pygame.mouse.get_pos()

#colors
RED = (255, 0, 0)
TURQUOISE = (0, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
#text
font = pygame.font.SysFont(None, 48)
basicFont = pygame.font.SysFont(None, 48)
def drawText(text, font, surface,x,y):
    textobj = font.render(text, 1, textColour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

sprite1 = pygame.image.load('daedalus red.png')
sprite2 = pygame.image.load('daedalus green.png')
sprite3 = pygame.image.load('daedalus blue.png')
sprite4 = pygame.image.load('daedalus yellow.png')
sprite5 = pygame.image.load('daedalus pink.png')
sprite6 = pygame.image.load('daedalus black.png')

red = pygame.Rect(800,5,97,53)
redImage = sprite1
redStretchedImage = pygame.transform.scale(redImage,(97, 53))

green = pygame.Rect(800,63,97,53)
greenImage = sprite2
greenStretchedImage = pygame.transform.scale(greenImage,(97, 53))

blue = pygame.Rect(800,121,97,53)
blueImage = sprite3
blueStretchedImage = pygame.transform.scale(blueImage,(97, 53))

yellow = pygame.Rect(800,179,97,53)
yellowImage = sprite4
yellowStretchedImage = pygame.transform.scale(yellowImage,(97, 53))

pink = pygame.Rect(800,237,97,53)
pinkImage = sprite5
pinkStretchedImage = pygame.transform.scale(pinkImage,(97, 53))

black = pygame.Rect(800,295,97,53)
blackImage = sprite6
blackStretchedImage = pygame.transform.scale(blackImage,(97, 53))

RED = [red]

SHIPS = [red, green, blue, yellow, pink, black]
currentShip = 0 #red = 0, green = 1, blue = 2, yellow = 3, pink = 4, black = 5
materials = []
gameplay=True
background = pygame.Rect(0, 0, 900, 900)
backgroundImage = pygame.image.load('space n stuff.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(900, 900))
    
def Gameplay():
    global red, green, blue, yellow, pink, black, click, MousePos, currentShip
    while gameplay==True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == ord('a'):
                    findx = red.x
                    findy = red.y
                    print ( str(findy), str(findx))
                if event.key == ord('q'):
                    currentShip = 2
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                    
            if event.type == MOUSEBUTTONDOWN:
                click = True
            if event.type == MOUSEBUTTONUP:
                click = False
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
        MousePos=pygame.mouse.get_pos()
        for red in RED:
            if click == True and SHIPS[currentShip].left > MousePos[0]:
                SHIPS[currentShip].left -= MOVESPEED
            if click == True and SHIPS[currentShip].right < MousePos[0]:
                SHIPS[currentShip].right += MOVESPEED
            if click == True and SHIPS[currentShip].top > MousePos[1]:
                SHIPS[currentShip].top -= MOVESPEED
            if click == True and SHIPS[currentShip].bottom < MousePos[1]:
                SHIPS[currentShip].bottom += MOVESPEED

        

        windowSurface.fill(GRAY)
        windowSurface.blit(backgroundStretchedImage, background)

        if True:
            windowSurface.blit(redStretchedImage, red)

        if True:
            windowSurface.blit(greenStretchedImage, green)

        if True:
            windowSurface.blit(blueStretchedImage, blue)

        if True:
            windowSurface.blit(yellowStretchedImage, yellow)

        if True:
            windowSurface.blit(pinkStretchedImage, pink)

        if True:
            windowSurface.blit(blackStretchedImage, black)

        pygame.display.update()
        mainCl
        

