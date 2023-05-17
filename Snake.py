import pygame
import random
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.direction = 'middle'
        self.length = 1
        self.posX = width / 2
        self.posY = height / 2
        self.head = [self.posX, self.posY]
        self.allCubes = [self.head]
        self.speed = 10
        self.diffX = 0
        self.diffY = 0
        self.rect = pygame.draw.rect(display,blue,[self.posX ,self.posY,10,10])

    def update(self, event):
        if event.key == K_UP:
            if self.direction != 'Down':
                self.direction = 'Up'
                self.diffX = 0
                self.diffY = -self.speed
        elif event.key == K_DOWN:
            if self.direction != 'Up':
                self.direction = 'Down'
                self.diffX = 0
                self.diffY = self.speed
        elif event.key == K_LEFT:
            if self.direction != 'Right':
                self.direction = 'Left'
                self.diffX = -self.speed
                self.diffY = 0
        elif event.key == K_RIGHT:
            if self.direction != 'Left':
                self.direction = 'Right'
                self.diffX = self.speed
                self.diffY = 0

    def increasePrint(self):
        self.allCubes.append(self.head)
        if len(self.allCubes) > self.length:
            del self.allCubes[0]
        for i in self.allCubes:
            pygame.draw.rect(display,blue,[i[0],i[1],10,10])

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.posX = round(random.randrange(0, width - 10)/10.0)*10.0
        self.posY = round(random.randrange(0, height - 10)/10.0)*10.0
        self.pos = [self.posX, self.posY]
        self.rect = pygame.draw.rect(display,black,[self.posX,self.posY,10,10])


def message(msg,color):
    font_style = pygame.font.SysFont(None, 50)
    msg = font_style.render(msg, True, color)
    display.blit(msg, [(width-msg.get_width())/2, (height-msg.get_height()-50)/2])
       
def main():
    global display, blue, white, black, green, width, height
    pygame.init()

    width = 300
    height = 300
    black = (0,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    white = (255,255,255)

    display = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()
    
    display.fill(white)
    snake = Snake()
    fruit = Fruit() # Creates first fruit
    allSprites = pygame.sprite.Group()
    allSprites.add(snake)
    allSprites.add(fruit)
    
    pygame.display.update()
    
    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == QUIT:
                gameOver = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameOver = True
                else:
                    snake.update(event)
        snake.posX += snake.diffX
        snake.posY += snake.diffY
        snake.head = [snake.posX, snake.posY]
        if snake.posX<0 or snake.posX>=width or snake.posY<0 or snake.posY>=width:
            gameOver = True
        
        if snake.posX == fruit.posX and snake.posY == fruit.posY:
            fruit.kill()
            snake.length += 1
            validFruit = 0
            while validFruit == 0:
                fruit = Fruit()
                if fruit.pos in snake.allCubes:
                    print('AHHHHHHH')
                    continue
                else:
                    validFruit = 1
            allSprites.add(fruit)

        display.fill(white)
        snake.increasePrint()
        pygame.draw.rect(display,black,[fruit.posX,fruit.posY,10,10])
        
        for i in snake.allCubes[:-1]:
            if i == snake.head:
                gameOver = True
        pygame.display.update()
        
        clock.tick(10)
        
    display.fill(white)
    message("You Lost",black)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


main()
