import pygame
from collision import withinBounds, hittingWall
from random import randint

pygame.init()
leveys = 600
korkeus = 600
display = pygame.display.set_mode((korkeus, leveys))
pygame.display.set_caption("FlopBord")
clock = pygame.time.Clock()
birdUp = pygame.image.load("media/bird_up.png")
birdDown = pygame.image.load("media/bird_down.png")
topWall = pygame.image.load("media/ylaPutki.png")
downWall = pygame.image.load("media/alaPutki.png")


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumping = False
        self.jumpHeight = 10

    def drawBird(self):
        if(self.jumpHeight > 5):
            display.blit(birdUp, [self.x, self.y])
        else:
            display.blit(birdDown, [self.x, self.y])

    def gravity(self):
        self.hitBox = [self.x+20, self.y+20]
        if(not withinBounds(self.x, self.y, 10)):
            print("ouou")
        if(self.jumping):
            if(int(self.jumpHeight) >= 1):
                self.y -= int(self.jumpHeight)
                self.jumpHeight *= 0.9
            else:
                self.jumping = False
                self.jumpHeight = 10
        else:
            self.y += 7

    def jump(self):
        self.jumpHeight = 10
        self.jumping = True


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawWall(self):
        display.blit(topWall, [self.x, self.y-525])
        display.blit(downWall, [self.x, self.y+25])

    def moveWall(self):
        self.topHitBox = [self.x, self.y-525, 80, 440] # leveys, korkeus
        self.botHitBox = [self.x, self.y+25, 80, 440]
        if(self.x < -100):
            self.x = 600
            self.y = randint(150, 450)
        else:
            self.x -= 3


def gameLogic(entity, obstacle):
    entity.gravity()
    entity.drawBird()
    for wall in obstacle:
        wall.moveWall()
        wall.drawWall()
        if(hittingWall(entity.hitBox, wall.botHitBox) or
           hittingWall(entity.hitBox, wall.topHitBox)):
            print("wdf")


def inputt(entity):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                entity.jump()

def game():
    bird = Bird(300, 300)
    walls = [Wall(700, randint(100, 500)), Wall(1050, randint(100, 500))]
    while(True):
        inputt(bird)
        display.fill(pygame.Color("white"))
        gameLogic(bird, walls)
        pygame.display.update()
        clock.tick(60)


if(__name__ == "__main__"):
    game()
