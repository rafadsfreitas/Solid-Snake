import pygame
from random import randrange
pygame.init()

WHITE =(255,255,255)
BLACK =(0, 0, 0)
RED =(255, 0, 0)
GREEN =(0, 160, 0)
DGREEN =(0, 140, 0)
MGREEN =(0, 180, 0)
BLUE =(0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
DYELLOW = (240, 240, 0)
MAGENTA = (255, 0, 255)
PURPLE =  (230, 0, 255)
GRAY = (50, 50, 50)

width = 800
height = 600
size = 40

clock = pygame.time.Clock()
bg = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cobrinha Moderada")
#apple sprite
appl = pygame.image.load("macaColor.png")

def grid():
    for i in range(0, width, size*2):
        for j in range(0, height, size*2):
            pygame.draw.rect(bg, DGREEN, [i, j, size, size])
    for k in range(size, width, size*2):
        for l in range(size, height, size*2):
            pygame.draw.rect(bg, DGREEN, [k, l, size, size])
    
    '''for i in range(size, width, size):
        pygame.draw.line(bg, CYAN, [i, 0], [i, 600], True)
    for j in range(size, height, size):
        pygame.draw.line(bg, CYAN, [0, j], [800, j], True)'''

def text(msg, color, textsize, x, y):
    font = pygame.font.SysFont('Arial', textsize, bold=True)
    text1 = font.render(msg, True, color)
    bg.blit(text1, [x, y])

def snake(snakexy):
    for xy in snakexy:
        pygame.draw.rect(bg, YELLOW, [xy[0], xy[1], size, size])
        #pygame.draw.rect(bg, YELLOW, [xy[0]+1, xy[1]+1, size-1, size-1])

def apple(apple_x, apple_y): #appleSpawn
        bg.blit(appl, [apple_x, apple_y])

def game():
    score = 0
    running = True
    gameover = False
    pos_x = randrange(0, width-size, size)
    pos_y = randrange(0, height-size, size)
    apple_x = randrange(0, width-size, size)
    apple_y = randrange(size, height-size, size)
    speed_x = size
    speed_y = 0
    snakexy = []
    snakeComp = 2
    gamespeed = 10
    paused = False
    while running:
        #pauseGame
        while paused:
            gamespeed = 0
            #pygame.draw.rect(bg, GRAY, [0, 240, width, 241])
            text("GAME PAUSED", WHITE, 100, 30, 255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameover = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gamespeed = 10
                        paused = False
                    if event.key == pygame.K_SPACE:
                        gamespeed = 10
                        paused = False
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        gameover = False
            pygame.display.update()
        #gameOver
        while gameover:
            gamespeed = 0
            pygame.draw.rect(bg, GREEN, [0, size, width, height])
            pygame.draw.rect(bg, GRAY, [0, 160, width, 330])
            text("GAME OVER ", RED, 120, 30, 200)
            text('TRY AGAIN? Y/N', WHITE, 70, 100, 360)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameover = False                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        score = 0
                        running = True
                        gameover = False
                        pos_x = randrange(0, width-size, size)
                        pos_y = randrange(0, height-size, size)
                        apple_x = randrange(0, width-size, size)
                        apple_y = randrange(size, height-size, size)
                        speed_x = size
                        speed_y = 0
                        snakexy = []
                        snakeComp = 2
                        gamespeed = 8
                    if event.key == pygame.K_n:
                        running = False
                        gameover = False
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        gameover = False
        #keyboardEvents
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameover = True
                if event.key == pygame.K_LEFT and speed_x != size:
                    speed_y = 0
                    speed_x = -size
                if event.key == pygame.K_RIGHT and speed_x != -size:
                    speed_y = 0
                    speed_x = size
                if event.key == pygame.K_UP and speed_y != size:
                    speed_x = 0
                    speed_y = -size
                if event.key == pygame.K_DOWN and speed_y != -size:
                    speed_x = 0
                    speed_y = size
                if event.key == pygame.K_a and speed_x != size:
                    speed_y = 0
                    speed_x = -size
                if event.key == pygame.K_d and speed_x != -size:
                    speed_y = 0
                    speed_x = size
                if event.key == pygame.K_w and speed_y != size:
                    speed_x = 0
                    speed_y = -size
                if event.key == pygame.K_s and speed_y != -size:
                    speed_x = 0
                    speed_y = size
                if event.key == pygame.K_p:
                    paused = True
                if event.key == pygame.K_SPACE:
                    paused = True
        if running:
            bg.fill(MGREEN)
            pos_x += speed_x
            pos_y += speed_y

            if pos_x == apple_x and pos_y == apple_y:
                apple_x = randrange(0, width-size, size)
                apple_y = randrange(size, height-size, size)
                snakeComp += 1
                score += 10
              #movement
            if pos_x + size > width:
                pos_x = 0
            if pos_x < 0:
                pos_x = width-size
            if pos_y + size > height:
                pos_y = size
            if pos_y < size:
                pos_y= height-size

            snakeHead = []
            snakeHead.append(pos_x)
            snakeHead.append(pos_y)
            snakexy.append(snakeHead)
            if len(snakexy) > snakeComp:
                del snakexy[0]
            
            if any(block == snakeHead for block in snakexy[:-1]):
                gameover = True

            grid()
            pygame.draw.rect(bg, BLACK, [0, 0, width, size])
            text("SCORE: {}".format(score), WHITE, 30, 13, 4)
            snake(snakexy)        
            apple(apple_x, apple_y)
            pygame.display.update()
            clock.tick(gamespeed)
    
game()
pygame.quit()
