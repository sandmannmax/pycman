import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1920,1024))
pygame.display.set_caption('Pycman')
icon = pygame.image.load('icon.png')
icon = pygame.transform.scale(icon, (32,32))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

close = False
pacman = pygame.image.load('pacman.png')
pacman = pygame.transform.scale(pacman, (32, 32))
pacman = pygame.transform.rotate(pacman,180)
point = pygame.image.load('punkt.png')
background = pygame.image.load('background.png')
gameDisplay.blit(background,(0,0))
posX = 15
posY = 17
posXpx = posX*32
posYpx = posY*32
praedirection = 4
direction = 4
matrix = [[]] 
matrix.append([-2,1,1,1,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,1,1,1,-2])
matrix.append([-2,1,-2,-2,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,1,-2,1,-2,-2,1,-2])
matrix.append([-2,1,-2,-2,1,-2,1,-2,1,-2,1,-2,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,-2,-2,1,-2])
matrix.append([-2,1,1,1,1,1,1,-2,1,1,1,-2,1,1,1,-2,-2,-2,-2,1,-2,-2,-2,1,-2,1,1,1,-2,-2,1,-2])
matrix.append([-2,1,-2,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,1,-2,1,1,1,1,1,1,-2,1,-2,-2,-2,1,1,1,1,-2])
matrix.append([-2,1,-2,1,1,1,1,1,1,1,1,1,1,-2,1,-2,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,1,-2,1,1,1,1,1,1,-2,1,-2,1,1,1,1,1,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,1,1,1,-2,1,1,1,1,1,1,-2,-2,1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2])
matrix.append([-2,1,1,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,-2,1,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,1,-2])
matrix.append([-2,-2,-2,1,-2,1,1,1,-2,1,1,1,1,1,1,1,1,-2,-2,1,1,1,1,-2,-2,-2,1,1,1,-2,1,-2])
matrix.append([-2,1,1,1,-2,1,-2,1,-2,-2,1,-2,-2,-2,-2,-2,1,-2,-2,1,-2,-2,1,1,1,1,1,-2,1,-2,1,-2])
matrix.append([-2,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2,-2,1,1,1,-2])
matrix.append([-2,1,-2,-2,1,-2,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,-2,1,-2,1,1,1,1,-2,-2,-2,-2,1,-2])
matrix.append([-2,1,1,1,1,-2,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,1,1,1,1,-2])
matrix.append([-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2])
matrix.append([-2,-2,-2,-2,1,1,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,-2,1,1,1,1,1,1,1,1,-2,-2,-2,-2])
matrix.append([-2,-2,-2,-2,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2])
matrix.append([-2,1,1,1,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,1,-2,1,1,1,1,-2])
matrix.append([-2,1,-2,-2,1,-2,1,-2,1,-2,1,-2,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,-2,-2,1,-2])
matrix.append([-2,1,1,1,1,1,1,-2,1,1,1,-2,1,1,1,-2,-2,-2,-2,1,-2,-2,-2,1,-2,1,1,1,-2,-2,1,-2])
matrix.append([-2,1,-2,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,1,-2,1,1,1,1,1,1,-2,1,-2,-2,-2,1,1,1,1,-2])
matrix.append([-2,1,-2,1,1,1,1,1,1,1,1,1,1,-2,1,-2,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,1,-2,1,1,1,1,1,1,-2,1,-2,1,1,1,1,1,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,1,1,1,-2,1,1,1,1,1,1,-2,-2,1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2])
matrix.append([-2,1,1,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,1,-2])
matrix.append([-2,-2,-2,1,-2,1,1,1,-2,1,1,1,1,1,1,1,1,-2,-2,1,-2,-2,-2,1,-2,-2,1,1,1,-2,1,-2])
matrix.append([-2,1,1,1,-2,1,-2,1,-2,-2,1,-2,-2,-2,-2,-2,1,-2,-2,1,-2,-2,-2,1,1,1,1,-2,1,-2,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,1,1,1,1,1,1,-2,1,1,1,1,1,1,1,-2,-2,-2,-2,-2,-2,-2,1,-2,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,1,-2,1,-2,1,1,1,1,1,-2,1,-2,1,-2])
matrix.append([-2,1,1,1,1,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,1,1,-2,-2,-2,1,1,1,1,1,-2])
for i in range(31):
    matrix[0].append(-2)
matrix.append([])
for i in range(31):
    matrix[31].append(-2)

def pointTest():
    points = {}
    pointnumber = 0
    count1 = 0
    count2 = 0
    for row in matrix:
        for x in row:
            if x == 1:
                points[pointnumber] = (count2*32, count1*32)
                pointnumber += 1
            count2 += 1
        count1 += 1
        count2 = 0
    return points

points = pointTest()
            
def drawPacMan(x, y):
    points = pointTest()
    gameDisplay.blit(background,(0,0))
    for k, v in points.items():
       gameDisplay.blit(point,v)
    gameDisplay.blit(pacman,(x,y))

drawPacMan(posXpx, posYpx)
matrix[posY][posX] = 0


while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                praedirection = 4
            if event.key == pygame.K_RIGHT:
                praedirection = 2
            if event.key == pygame.K_UP:
                praedirection = 1
            if event.key == pygame.K_DOWN:
                praedirection = 3
    
    if direction == 1:
        if posYpx % 32 > 0:
            posYpx -= 2
        elif matrix[posY - 1][posX] != -2:
            if praedirection == direction:
                matrix[posY][posX] = -1
                posYpx -= 2
                matrix[posY - 1][posX] = 0
                posY -= 1
            else:
                if praedirection == 2:
                    if matrix[posY][posX + 1] != -2:
                        pacman = pygame.transform.rotate(pacman,270)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx -= 2
                        matrix[posY - 1][posX] = 0
                        posY -= 1
                elif praedirection == 3:
                    if matrix[posY + 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,180)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx -= 2
                        matrix[posY - 1][posX] = 0
                        posY -= 1
                elif praedirection == 4:
                    if matrix[posY][posX - 1] != -2:
                        pacman = pygame.transform.rotate(pacman,90)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx -= 2
                        matrix[posY - 1][posX] = 0
                        posY -= 1
        else:
            if praedirection == 2:
                if matrix[posY][posX + 1] != -2:
                    pacman = pygame.transform.rotate(pacman,270)
                    direction = praedirection
            elif praedirection == 3:
                if matrix[posY + 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,180)
                    direction = praedirection
            elif praedirection == 4:
                if matrix[posY][posX - 1] != -2:
                    pacman = pygame.transform.rotate(pacman,90)
                    direction = praedirection
    if direction == 2:
        if posXpx % 32 == 0 or posXpx / 32 < posX:
            posXpx += 2
        elif matrix[posY][posX + 1] != -2:
            if praedirection == direction:
                matrix[posY][posX] = -1
                posXpx += 2
                matrix[posY][posX + 1] = 0
                posX += 1
            else:
                if praedirection == 1:
                    if matrix[posY - 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,90)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx += 2
                        matrix[posY][posX + 1] = 0
                        posX += 1
                elif praedirection == 3:
                    if matrix[posY + 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,270)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx += 2
                        matrix[posY][posX + 1] = 0
                        posX += 1
                elif praedirection == 4:
                    if matrix[posY][posX - 1] != -2:
                        pacman = pygame.transform.rotate(pacman,180)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx += 2
                        matrix[posY][posX + 1] = 0
                        posX += 1
        else:
            if praedirection == 1:
                if matrix[posY - 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,90)
                    direction = praedirection
            elif praedirection == 3:
                if matrix[posY + 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,270)
                    direction = praedirection
            elif praedirection == 4:
                if matrix[posY][posX - 1] != -2:
                    pacman = pygame.transform.rotate(pacman,180)
                    direction = praedirection
    if direction == 3:
        if posYpx % 32 == 0 or posYpx / 32 < posY:
            posYpx += 2
        elif matrix[posY + 1][posX] != -2:
            if praedirection == direction:
                matrix[posY][posX] = -1
                posYpx += 2
                matrix[posY + 1][posX] = 0
                posY += 1
            else:
                if praedirection == 1:
                    if matrix[posY - 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,180)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx += 2
                        matrix[posY + 1][posX] = 0
                        posY += 1
                elif praedirection == 2:
                    if matrix[posY][posX + 1] != -2:
                        pacman = pygame.transform.rotate(pacman,90)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx += 2
                        matrix[posY + 1][posX] = 0
                        posY += 1
                elif praedirection == 4:
                    if matrix[posY][posX - 1] != -2:
                        pacman = pygame.transform.rotate(pacman,270)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posYpx += 2
                        matrix[posY + 1][posX] = 0
                        posY += 1
        else:
            if praedirection == 1:
                if matrix[posY - 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,180)
                    direction = praedirection
            elif praedirection == 2:
                if matrix[posY][posX + 1] != -2:
                    pacman = pygame.transform.rotate(pacman,90)
                    direction = praedirection
            elif praedirection == 4:
                if matrix[posY][posX - 1] != -2:
                    pacman = pygame.transform.rotate(pacman,270)
                    direction = praedirection
    if direction == 4:
        if posXpx % 32 > 0:
            posXpx -= 2
        elif matrix[posY][posX - 1] != -2:
            if praedirection == direction:
                matrix[posY][posX] = -1
                posXpx -= 2
                matrix[posY][posX - 1] = 0
                posX -= 1
            else:
                if praedirection == 1:
                    if matrix[posY - 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,270)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx -= 2
                        matrix[posY][posX - 1] = 0
                        posX -= 1
                elif praedirection == 2:
                    if matrix[posY][posX + 1] != -2:
                        pacman = pygame.transform.rotate(pacman,180)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx -= 2
                        matrix[posY][posX - 1] = 0
                        posX -= 1
                elif praedirection == 3:
                    if matrix[posY + 1][posX] != -2:
                        pacman = pygame.transform.rotate(pacman,90)
                        direction = praedirection
                    else:
                        matrix[posY][posX] = -1
                        posXpx -= 2
                        matrix[posY][posX - 1] = 0
                        posX -= 1
        else:
            if praedirection == 1:
                if matrix[posY - 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,270)
                    direction = praedirection
            elif praedirection == 2:
                if matrix[posY][posX + 1] != -2:
                    pacman = pygame.transform.rotate(pacman,180)
                    direction = praedirection
            elif praedirection == 3:
                if matrix[posY + 1][posX] != -2:
                    pacman = pygame.transform.rotate(pacman,90)
                    direction = praedirection

    drawPacMan(posXpx, posYpx)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
