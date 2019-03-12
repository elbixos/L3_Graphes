import pygame
import numpy as np

def getNeighbors(matrix, current) :
    l,c = matrix.shape

    neighbors = []
    (i,j) = current
    #print (i,j)

    if i-1 >= 0 :
        if matrix[i-1,j] == 0:
            neighbors.append((i-1,j))

    if i+1 < l :
        if matrix[i+1,j] == 0:
            neighbors.append((i+1,j))

    if j-1 >= 0 :
        if matrix[i,j-1] == 0:
            neighbors.append((i,j-1))

    if j+1 < c :
        if matrix[i,j+1] == 0:
            neighbors.append((i,j+1))


    #print(neighbors)
    return neighbors


def getPath(start, end,previous):
    #print (previous)
    path = []
    current = end
    while not current == start :
        #print (current)
        prev = previous[current]
        path.insert(0,prev)
        current = prev

    del path[0]
    return path


def run(start,end, matrix):
    toDo = [start]
    alreadyDone = []
    previous ={}

    while toDo :
        current=toDo[0]
        #print ("processing", str(current))

        for s in getNeighbors(matrix, current) :
            #print (s)
            if (not s in toDo) and (not s in alreadyDone):
                previous[s]=current
                toDo.append(s)

        toDo.remove(current)
        alreadyDone.append(current)

    #print (previous)
    path = getPath(start,end, previous)
    #print (path)
    return path

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


def drawPath(path, fenetre,size):
    color = (128,128,0)

    ## Horizontal lines
    for e in path :
        print (e)
        rect = pygame.Rect(e[1]*size+1,e[0]*size+1,size-1,size-1)
        pygame.draw.rect(fenetre, color, rect, 0)

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

    rect = pygame.Rect(pos[1]*size+1,pos[0]*size+1,size-1,size-1)
    pygame.draw.rect(fenetre, color, rect, 0)

def drawEnd(pos,fenetre,size):
    color = (128,0,0)

    rect = pygame.Rect(pos[1]*size+1,pos[0]*size+1,size-1,size-1)
    pygame.draw.rect(fenetre, color, rect, 0)


def drawMatrix(matrix,fenetre,size):
    color = (128,128,128)

    nLines, nCols = getSizes(fenetre,squareSize)

    ## Horizontal lines
    for i in range(nLines) :
        for j in range(nCols) :
            rect = pygame.Rect(j*size+1,i*size+1,size-1,size-1)
            if matrix[i,j] == 1 :
                pygame.draw.rect(fenetre, color, rect, 0)
            else:
                pygame.draw.rect(fenetre, (0,0,0), rect, 0)



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

path = []
# Boucle des tours de jeu
horloge = pygame.time.Clock()

while quitGame == False:
    # on fixe la cadence
    horloge.tick(20)

    # on r�cup�re la pile d'evenements pour plus tard.
    allEvents = pygame.event.get()

    # on r�cup�re aussi l'�tat des touches pour plus tard.
    touches = pygame.key.get_pressed();

    if touches[pygame.K_ESCAPE]:
        quitGame = True


    if touches[pygame.K_s]:
        startDefine = True
        endDefine = False

    if touches[pygame.K_e]:
        endDefine = True
        startDefine = False

    if touches[pygame.K_r]:
        if (not start == (-1,-1)) and (not end == (-1,-1)):
            path = run(start,end, matrix)
            print (path)

    ## In case of a click : let's do stuff
    for event in allEvents:   # parcours de la liste des evenements recus
        if event.type == pygame.MOUSEBUTTONUP:
            i,j = getMatrixPos(event.pos,squareSize)
            # the previously defined path is now pointless
            path = []
            if startDefine :
                # position of starting point
                start = (i,j)
                matrix[i,j]=0
                startDefine = False

            elif endDefine :
                # position of the ending point
                end =(i,j)
                matrix[i,j]=0
                endDefine = False
            else :
                # Position a wall
                if matrix [i,j] == 0:
                    matrix[i,j]=1
                else :
                    matrix[i,j]=0


    drawGrid(fenetre,squareSize)
    drawMatrix(matrix,fenetre,squareSize)



    if not start == (-1,-1):
        drawStart(start,fenetre, squareSize)

    if not end == (-1,-1):
        drawEnd(end,fenetre, squareSize)

    if path :
        drawPath(path,fenetre,squareSize)

    pygame.display.flip()


    # et on v�rifie si on a voulu quitter
    for event in allEvents:   # parcours de la liste des evenements recus
            if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
                quitGame = True

pygame.quit()
