import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1024,1024))
pygame.display.set_caption('PacMan')
clock = pygame.time.Clock()

close = False
pacman = pygame.image.load('2000px-Pacman.svg.png')
pacman = pygame.transform.scale(pacman, (30, 30))
background = pygame.image.load('background.png')
gameDisplay.blit(background,(0,0))
posX = 480
posY = 545
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
matrix.append([-2,1,1,1,1,-2,1,-2,-2,-2,-2,1,-2,1,1,1,1,1,1,-2,1,-2,-2,-2,-2,-2,-2,1,1,1,1,-2])
matrix.append([-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2,1,-2,1,1,1,1,1,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2])
matrix.append([1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,-2,-2,1,1,1,1,1,1,1,1,1,1,1,1])
matrix.append([-2,-2,-2,-2,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,-2])
matrix.append([-2,1,1,1,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,-2,-2,1,-2,1,1,1,1,-2])
matrix.append(matrix[3])
matrix.append(matrix[4])
matrix.append(matrix[5])
matrix.append(matrix[6])
matrix.append(matrix[7])
matrix.append(matrix[8])
matrix.append([-2,1,1,1,-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,-2,-2,-2,1,-2,-2,-2,1,-2,-2,-2,-2,-2,-2,1,-2])
matrix.append([-2,-2,-2,1,-2,1,1,1,-2,1,1,1,1,1,1,1,1,-2,-2,1,1,-2,-2,1,-2,-2,1,1,1,-2,1,-2])
matrix.append(matrix[11])
matrix.append([-2,1,-2,1,-2,1,-2,1,1,1,1,1,1,-2,1,1,1,1,1,1,1,-2,-2,-2,-2,-2,-2,-2,1,-2,1,-2])
matrix.append([-2,1,-2,1,-2,1,-2,1,-2,-2,-2,-2,1,-2,1,-2,-2,-2,1,-2,1,-2,1,1,1,1,1,-2,1,-2,1,-2])
matrix.append([-2,1,1,1,1,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,1,1,-2,-2,-2,1,1,1,1,1,-2])
for i in range(31):
    matrix[0].append(-2)
matrix.append([])
for i in range(31):
    matrix[31].append(-2)

def drawPacMan(x, y):
    gameDisplay.blit(background,(0,0))
    gameDisplay.blit(pacman,(x,y))

drawPacMan(posX, posY)

while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 4
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_UP:
                direction = 1
            if event.key == pygame.K_DOWN:
                direction = 3
    
    if direction == 1:
        posY -= 1
    if direction == 2:
        posX += 1
    if direction == 3:
        posY += 1
    if direction == 4:
        posX -= 1
    drawPacMan(posX, posY)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
