import random
import pygame
import time
from pygame.locals import *
import sys
pygame.init()

#colors
BLUE  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
my_color = (230, 230, 250)

# display variables
display_width = 840
display_height = 650

# the size and color of background screen
display = pygame.display.set_mode((840, 650))
display.fill(white)

# settings
FPS = 60
clock = pygame.time.Clock()
own_Speed = 6
enemy_speed = 5
num_cars = 0

# loading the images of the cars
# car_enemy = pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/greencar.png')
# car_Own = pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/redcar.png')
bg = pygame.image.load("/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/AnimatedStreet.png")

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# size of coin
def size_coin():
    a = random.choice([1, 2]) * 20
    return a

# создаем классы
class coin_generation(pygame.sprite.Sprite):
    # first coin settings
    def __init__(self):
        super().__init__()
        global first
        first = size_coin()
        self.img = pygame.transform.scale(pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/coin.png'), (first, first))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(150, display_width-150), random.randint(60, display_height-60))
        global coi     
        coi = first        # first coin weight

    def check(self):
        pass
    
    def nextCoin(self):  # next coin
        global cnt
        global coi
        cnt = coi
        coi = size_coin()       # задаем другой размер coin
        self.img = pygame.transform.scale(pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/coin.png'), (coi, coi))
        self.rect.center = (random.randint(150, display_width-200), random.randint(60, display_height-60))
    def render(self, surface):
        surface.blit(self.img, self.rect)

class ownMovement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()     # own car settings
        self.car = pygame.transform.scale(pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/redcar.png'), (40, 90))
        self.rect = self.car.get_rect()
        self.rect.center = (600, 600)

    def check(self):
        pass

    def move(self):
        key = pygame.key.get_pressed()
        if(self.rect.bottom < display_height):
            if key[K_DOWN]:
                self.rect.move_ip(0, own_Speed)
        if(self.rect.top > 0):
            if key[K_UP]:
                self.rect.move_ip(0, -own_Speed)
        if (self.rect.right < display_width-138):
            if key[K_RIGHT]:
                self.rect.move_ip(own_Speed, 0)
        if (self.rect.left > 138):
            if key[K_LEFT]:
                self.rect.move_ip(-own_Speed, 0)

    def render(self,surface):
        surface.blit(self.car, self.rect)

class enemyMovement(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()    # enemy car settings
            self.car = pygame.transform.scale(pygame.image.load('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/greencar.png'), (45, 90))
            self.rect = self.car.get_rect()
            self.rect.center = (random.randint(138, display_width-138),0)
        def check(self):
            pass
        def move(self):
            self.rect.move_ip(0, enemy_speed)    # enemy car move
            if(self.rect.bottom > display_width):
                global num_cars
                num_cars += 1    # число машин
                self.rect.top = 0
                self.rect.center = (random.randint(138, display_width-138),0)
        def render(self, surface):
            surface.blit(self.car, self.rect)

current_Own = ownMovement()
current_Enemy = enemyMovement()
current_Coin = coin_generation()  

sprite_Coin = pygame.sprite.Group()
sprite_Coin.add(current_Coin)
sprite_Enemy = pygame.sprite.Group()
sprite_Enemy.add(current_Enemy)
sprite_All = pygame.sprite.Group()
sprite_All.add(current_Enemy)
sprite_All.add(current_Own)

global collected
coins = 0

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while 1:
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
    display.blit(bg, (0, 0))
    # Moves and Re-draws all Sprites
    for entity in sprite_All:
        display.blit(entity.car, entity.rect)
        entity.move()
    for i in sprite_Coin:
        i.check()
        i.render(display)


    scoreeee = f'collected coins - {int(coins)}'      # вывод на экран
    collectttt = font_small.render(str(scoreeee), True, black)
    display.blit(collectttt, (display_width - collectttt.get_width() - 5, 2))

    nummm = f'number of cars - {num_cars}'       # вывод на экран
    nunnuuumm = font_small.render(str(nummm), True, black)
    display.blit(nunnuuumm, (5, 2))


    if pygame.sprite.spritecollideany(current_Own, sprite_Coin):
        current_Coin.nextCoin()
        if coins == 0:
            coins += first/20
        else:
            coins += cnt/20
        if coins % 4:
            enemy_speed += 1   # каждый 4 монеты, скорость увеличивается
            own_Speed += 1
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(current_Own, sprite_Enemy):
        pygame.display.update()
        pygame.mixer.Sound('/Users/alikhankudaibergen/Documents/pp2/tsis9/машинка/crash.mp3').play()
        

        display.fill(red)
        display.blit(game_over, ((display_width - game_over.get_width())/2, (display_height - game_over.get_height())/2))
        # вывод на экран наши резы
        pygame.display.update()
        time.sleep(0.7) 

        for entity in sprite_All:
            entity.kill()  # очистка
        time.sleep(1)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(FPS)