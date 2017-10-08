import pygame, sys, time, random
from pygame.locals import *
#setup pygame
pygame.init()
mainClock = pygame.time.Clock()
#setup window
WINDOWHEIGHT = 500
WINDOWWIDTH = 900
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('ill name it later')
#movement
moveLeft = False
moveRight = False
boost = False
pewpew = False
MOVESPEED = 7
BULLETSPEED = 3.5
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
#variables
sprite1 = pygame.image.load('space ship idle.png')

sprite2 = pygame.image.load('space ship idle right bank.png')
sprite3 = pygame.image.load('space ship idle left bank.png')

sprite4 = pygame.image.load('space ship boosting.png')

sprite5 = pygame.image.load('space ship boosting right bank.png')
sprite6 = pygame.image.load('space ship boosting left bank.png')

sprite7 = pygame.image.load('bullet.png')

basicFont = pygame.font.SysFont(None, 28)

b = 50

player = pygame.Rect(150,350,b,125)
playerImage = sprite1
playerStretchedImage = pygame.transform.scale(playerImage,(90, 100))

playerbr = pygame.Rect(150,350,50,125)
playerImagebr = sprite2
playerStretchedImagebr = pygame.transform.scale(playerImagebr,(90, 100))

playerbl = pygame.Rect(150,350,50,125)
playerImagebl = sprite3
playerStretchedImagebl = pygame.transform.scale(playerImagebl,(90, 100))

playerb = pygame.Rect(150,350,50,125)
playerImageb = sprite4
playerStretchedImageb = pygame.transform.scale(playerImageb,(90, 100))

playerbbr = pygame.Rect(150,350,50,125)
playerImagebbr = sprite5
playerStretchedImagebbr = pygame.transform.scale(playerImagebbr,(90, 100))

playerbbl = pygame.Rect(150,350,50,125)
playerImagebbl = sprite6
playerStretchedImagebbl = pygame.transform.scale(playerImagebbl,(90, 100))

bulletp = pygame.Rect(b,350,10,20)
bulletImagep = sprite7
bulletStretchedImagep = pygame.transform.scale(bulletImagep,(10, 20))

PLAYER = [player, playerbr, playerbl, playerb, playerbbr, playerbbl]

materials = []
gameplay=True
background = pygame.Rect(0, 0, 900, 500)
backgroundImage = pygame.image.load('space n stuff.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(900, 500))

def Gameplay():
    global playerd, playerh, pewpew, playerImage, moveRight, moveLeft, boost, MOVESPEED, player, PLAYER, bulletp, bullet, BULLETSPEED
    while gameplay==True:
        for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == ord('d'):
                    moveRight = True
                    moveLeft = False
                if event.key == ord(' '):
                    pewpew = True
                if event.key == ord('w'):
                    boost = True
            if event.type == KEYUP:
                if event.key == ord('a'):
                    moveLeft = False
                if event.key == ord('d'):
                    moveRight = False
                if event.key == ord(' '):
                    pewpew = False
                if event.key == ord('w'):
                    boost = False
        for player in PLAYER:
            if moveLeft and player.left > 0:
                player.left -= MOVESPEED
            if moveRight and player.right < WINDOWWIDTH:
                player.right += MOVESPEED

            if moveLeft and bulletp.left > 0:
                bulletp.left -= BULLETSPEED
            if moveRight and bulletp.right < WINDOWWIDTH:
                bulletp.right += BULLETSPEED


        windowSurface.fill(GRAY)
        windowSurface.blit(backgroundStretchedImage, background)

        if moveLeft==False and moveRight==False and boost==False:
            windowSurface.blit(playerImage, player)
        
        if moveLeft==True and boost==False:
            windowSurface.blit(playerImagebl, playerbl)
                
        if moveRight==True and boost==False:
            windowSurface.blit(playerImagebr, playerbr)

        if boost==True and moveLeft==False and moveRight==False:
            windowSurface.blit(playerImageb, playerb)

        if boost==True and moveRight==True:
            windowSurface.blit(playerImagebbr, playerbbr)

        if boost==True and moveLeft==True:
            windowSurface.blit(playerImagebbl, playerbbl)

        if pewpew==True:
            windowSurface.blit(bulletImagep, bulletp)
            
            
        pygame.display.update()
        mainClock.tick(50)
Gameplay()
