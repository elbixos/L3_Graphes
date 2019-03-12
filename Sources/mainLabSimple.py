import pygame
import numpy as np


def getMatrixPos(event,squareSize):

    j = int(event[0] /squareSize)
    i = int(event[1]/squareSize)

    #print (nLines, nCols)
    return i,j

def getSizes(fenetre,squareSize):

    w,h = fenetre.get_size()
    nLines = int(h /squareSize)
    nCols = int(w/squareSize)

    #print (nLines, nCols)
    return nLines,nCols

def drawGrid(fenetre,size):
    color = (255,255,255)

    w,h = fenetre.get_size()
    nLines, nCols = getSizes(fenetre,squareSize)

    ## Horizontal lines
    for i in range(nLines) :
        start_pos = (0,i*size)
        end_pos =(w,i*size)
        pygame.draw.line(fenetre, color, start_pos, end_pos, 1)

    ## Vertical lines
    for j in range(nCols) :
        start_pos = (j*size,0)
        end_pos =(j*size,h)
        pygame.draw.line(fenetre, color, start_pos, end_pos, 1)

def drawStart(pos,fenetre,size):
    color = (0,128,0)

    rect = pygame.Rect(pos[1]*size,pos[0]*size,size,size)
    pygame.draw.rect(fenetre, color, rect, 0)

def drawEnd(pos,fenetre,size):
    color = (128,0,0)

    rect = pygame.Rect(pos[1]*size,pos[0]*size,size,size)
    pygame.draw.rect(fenetre, color, rect, 0)


def drawMatrix(matrix,fenetre,size):
    color = (128,128,128)

    nLines, nCols = getSizes(fenetre,squareSize)

    ## Horizontal lines
    for i in range(nLines) :
        for j in range(nCols) :
            if matrix[i,j] == 1 :
                rect = pygame.Rect(j*size,i*size,size,size)
                pygame.draw.rect(fenetre, color, rect, 0)



## Initialisation de la fenetre et création
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

quitGame = False

squareSize = 20

nLines, nCols = getSizes(fenetre,squareSize)

matrix = np.zeros((nLines,nCols),dtype=int)

start = (-1,-1)
end = (-1,-1)

startDefine = False
endDefine = False

# Boucle des tours de jeu
horloge = pygame.time.Clock()

while quitGame == False:
    # on fixe la cadence
    horloge.tick(20)

    # on r�cup�re la pile d'evenements pour plus tard.
    allEvents = pygame.event.get()

    # on r�cup�re aussi l'�tat des touches pour plus tard.
    touches = pygame.key.get_pressed();

    if touches[pygame.K_s]:
        print("depart")
        startDefine = True
        endDefine = False

    if touches[pygame.K_e]:
        endDefine = True
        startDefine = False

    ## In case of a click : let's do stuff
    for event in allEvents:   # parcours de la liste des evenements recus
        if event.type == pygame.MOUSEBUTTONUP:
            i,j = getMatrixPos(event.pos,squareSize)

            if startDefine :
                start = (i,j)
                matrix[i,j]=0
                startDefine = False
            elif endDefine :
                end =(i,j)
                matrix[i,j]=0
                endDefine = False
            else :
                matrix[i,j]=1

    drawGrid(fenetre,squareSize)
    drawMatrix(matrix,fenetre,squareSize)

    print (start)

    if not start[0] == -1:
        drawStart(start,fenetre, squareSize)

    if not end[0] == -1:
        drawEnd(end,fenetre, squareSize)


    pygame.display.flip()


    # et on v�rifie si on a voulu quitter
    for event in allEvents:   # parcours de la liste des evenements recus
            if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
                quitGame = True

pygame.quit()
