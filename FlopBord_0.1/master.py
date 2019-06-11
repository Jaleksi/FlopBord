import pygame
from collision import collision, outOfBounds

pygame.init()
leveys = 600
korkeus = 600
display = pygame.display.set_mode((korkeus, leveys))
pygame.display.set_caption("FlopBord")
clock = pygame.time.Clock()


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumping = False
        self.jumpHeight = 10

    def drawBird(self):
        pygame.draw.circle(display, (0), [self.x, self.y], 20, 0)

    def gravity(self):
        if(not outOfBounds(self.x, self.y, 10)):
            print("ouou")
        if(self.jumping):
            if(int(self.jumpHeight) >= 1):
                self.y -= int(self.jumpHeight)
                self.jumpHeight *= 0.9
            else:
                self.jumping = False
                self.jumpHeight = 10
        else:
            self.y += 3

    def jump(self):
        self.jumping = True




def gameLogic(entity):
    entity.drawBird()
    entity.gravity()


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
    while(True):
        inputt(bird)
        display.fill(pygame.Color("white"))
        gameLogic(bird)
        pygame.display.update()
        clock.tick(60)


if(__name__ == "__main__"):
    game()
