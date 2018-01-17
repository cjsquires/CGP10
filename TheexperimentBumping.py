import pygame, sys, time, random
from pygame.locals import *
#setup pygame
pygame.init()
mainClock = pygame.time.Clock()
#setup window
WINDOWHEIGHT = 500
WINDOWWIDTH = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('the experiment')

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

sprite1 = pygame.image.load('wheatly.png')

red = pygame.Rect(300,300,100,100)
redImage = sprite1
redStretchedImage = pygame.transform.scale(redImage,(100, 100))

notred = pygame.Rect(300,300,100,100)
notredImage = sprite1
notredStretchedImage = pygame.transform.scale(notredImage,(100, 100))

A = [0, 1, 2, 3, 4]

B = [0, 1, 2, 3, 4]

C = [0, 1, 2, 3, 4]

D = [0, 1, 2, 3, 4]

E = [0, 1, 2, 3, 4]

A[0] = (0,0)

A[1] = (100,0)

A[2] = (200,0)

A[3] = (300,0)

A[4] = (400,0)


B[0] = (0,100)

B[1] = (100,100)

B[2] = (200,100)

B[3] = (300,100)

B[4] = (400,100)


C[0] = (0,200)

C[1] = (100,200)

C[2] = (200,200)

C[3] = (300,200)

C[4] = (400,200)


D[0] = (0,300)

D[1] = (100,300)

D[2] = (200,300)

D[3] = (300,300)

D[4] = (400,300)


E[0] = (0,400)

E[1] = (100,400)
                                                                                                                                                        
E[2] = (200,400)

E[3] = (300,400)

E[4] = (400,400)

MATRIX = [A, B, C, D, E]

SELECTING = []

MOVESPEED = 100

placement = B[4]

previous = D[1]

selected = 1

RED = [red]

area = D[1]

D1occupied = False

boop = True

materials = []
gameplay=True
background = pygame.Rect(0, 0, 500, 500)
backgroundImage = pygame.image.load('PURPLE.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(500, 500))

def confirm():
    global D1occupied
    if D1occupied == True:
        print ('holycrapitworked')
    if D1occupied == False:
        print ('crrraaaaaappppp')

def Gameplay():
    global red, D1occupied, placement, area, SELECTING, notred, boop, selected, previous
    while gameplay==True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == ord('p'):
                    confirm()
                if event.key == ord('a'):
                    SELECTING.append(A)
                if event.key == ord('b'):
                    SELECTING.append(B)
                if event.key == ord('c'):
                    SELECTING.append(C)
                if event.key == ord('d'):
                    SELECTING.append(D)
                if event.key == ord('e'):
                    SELECTING.append(E)
                if event.key == ord('1'):
                    placement = SELECTING[0][0]
                    if selected == 1:
                        if placement[0] == notred[0] and placement[1] == notred[1]:
                            placement = SELECTING[0][1]
                    if selected == 2:
                        if placement[0] == red[0] and placement[1] == red[1]:
                            placement = SELECTING[0][1]
                            
                if event.key == ord('2'):
                    placement = SELECTING[0][1]
                    if selected == 1:
                        if placement[0] == notred[0] and placement[1] == notred[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][0]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][2]
                    if selected == 2:
                        if placement[0] == red[0] and placement[1] == red[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][0]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][2]
                            
                if event.key == ord('3'):
                    placement = SELECTING[0][2]
                    if selected == 1:
                        if placement[0] == notred[0] and placement[1] == notred[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][1]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][3]
                    if selected == 2:
                        if placement[0] == red[0] and placement[1] == red[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][1]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][3]]
                                
                if event.key == ord('4'):
                    placement = SELECTING[0][3]
                    if selected == 1:
                        if placement[0] == notred[0] and placement[1] == notred[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][2]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][4]
                    if selected == 2:
                        if placement[0] == red[0] and placement[1] == red[1]:
                            if red[0] < notred[0]:
                                placement = SELECTING[0][2]
                            if red[0] > notred[0]:
                                placement = SELECTING[0][4]
                            
                if event.key == ord('5'):
                    placement = SELECTING[0][4]
                    if selected == 1:
                        if placement[0] == notred[0] and placement[1] == notred[1]:
                            placement = SELECTING[0][3]
                    if selected == 2:
                        if placement[0] == red[0] and placement[1] == red[1]:
                            placement = SELECTING[0][3]
                            
                if event.key == ord('r'):
                    selected = 1
                    placement = red
                if event.key == ord('n'):
                    selected = 2
                    placement = notred
                if event.key == ord(' '):
                    if RED[0] == red:
                        print ('gsdvhifsivleuvogi')
                    if RED[0] != red:
                        print ('fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == KEYUP:
                if event.key == ord('a'):
                    SELECTING.remove(A)
                if event.key == ord('b'):
                    SELECTING.remove(B)
                if event.key == ord('c'):
                    SELECTING.remove(C)
                if event.key == ord('d'):
                    SELECTING.remove(D)
                if event.key == ord('e'):
                    SELECTING.remove(E)
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
        
        if selected == 1:
            red = pygame.Rect(placement[0], placement[1],100,100)
            
        if selected == 2:
            notred = pygame.Rect(placement[0], placement[1],100,100)
        
        if MOVESPEED == 47328564562134120:
            
            MousePos=pygame.mouse.get_pos()
            for red in RED:
                if 0 > placement[0]:
                    red.left -= MOVESPEED
                if 0 < placement[0]:
                    red.right += MOVESPEED
                if 0 > placement[1]:
                    red.top -= MOVESPEED
                if 0 < placement[1]:
                    red.bottom += MOVESPEED
 
            for notred in RED:
                if 0 > placement[0]:
                    notred.left -= MOVESPEED
                if 0 < placement[0]:
                    notred.right += MOVESPEED
                if 0 > placement[1]:
                    notred.top -= MOVESPEED
                if 0 < placement[1]:
                    notred.bottom += MOVESPEED
        

        windowSurface.fill(GRAY)
        windowSurface.blit(backgroundStretchedImage, background)

        if True:
            windowSurface.blit(redStretchedImage, red)

        if True:
            windowSurface.blit(notredStretchedImage, notred)

        if red.left == area[0] and red.top == area[1]:
            D1occupied = True

        if red.left != area[0] and red.top != area[1]:
            D1occupied = False

        pygame.display.update()
        mainClock.tick(50)
Gameplay()
