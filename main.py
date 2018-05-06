import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((900,700))
pygame.display.set_caption('PacMan')
clock = pygame.time.Clock()

close = False
pacman = pygame.image.load('2000px-Pacman.svg.png')
pacman = pygame.transform.scale(pacman, (30, 30))
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1080, 720))
gameDisplay.blit(background,(0,0))
posX = 523
posY = 395

def drawPacMan(x, y):
    gameDisplay.blit(pacman,(x,y))

drawPacMan(posX, posY)

while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        move_ticker = 0
        keys=pygame.key.get_pressed()
        print(keys)
        #
        drawPacMan(posX, posY)
        pygame.display.update()
        clock.tick(30)

pygame.quit()
quit()
