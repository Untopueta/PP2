import pygame
import math

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
START_X = 0
START_Y = 0

SPEED = 5

class Player:
    def __init__(self):
        self.width = 60
        self.aspect_ratio = 0.5
        self.height = self.width / self.aspect_ratio
        self.image = pygame.image.load("car_green.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (set.SCREEN_WIDTH // 2, set.SCREEN_HEIGHT - 100)
        self.MOVEMENT_SPEED = set.SPEED * 4

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-self.MOVEMENT_SPEED, 0)
        if pressed[pygame.K_RIGHT]:
            if self.rect.right < set.SCREEN_WIDTH:
                self.rect.move_ip(self.MOVEMENT_SPEED, 0)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Coin:
    def __init__(self):
        self.width = 20
        self.acpect_ratio = 1
        self.height = self.width / self.acpect_ratio
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = self.randomize_position()
        self.speed = set.SPEED

    def randomize_position(self):
        y = int(-self.height)
        x = math.random.randint(
            10 + self.rect.width, set.SCREEN_WIDTH - 10 - self.rect.width
        )
        return x, y

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > set.SCREEN_HEIGHT:
            self.__init__()

    def ChangeSpeed(self, speed):
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

screen = pygame.display.set_mode((set.SCREEN_WIDTH, set.SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)

FPS = 60
clock = pygame.time.Clock()
running = True

player = Player()
coin = Coin()

coins = 0
scroll = 0
speed = set.SPEED

font = pygame.font.Font("font1", 40) #font

b = pygame.image.load("background.png")
B_WIDTH = set.SCREEN_WIDTH
B_ASPECT_RATIO = b.get_width() / b.get_height()
B_HEIGHT = math.ceil(set.SCREEN_HEIGHT / B_ASPECT_RATIO)
background = pygame.transform.scale(b, (B_WIDTH, B_HEIGHT))
COPIES = math.ceil(set.SCREEN_HEIGHT / b.get_height()) + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(set.WHITE)
    scroll = (scroll + speed // 1.5) % b.get_height()
    for i in range(COPIES):
        screen.blit(b, (0, scroll + (i - 1) * (b.get_height() - 1)))

    coins_counter = font.render(str(coins), True, set.BLACK)
    screen.blit(coins_counter, (set.SCREEN_WIDTH - 50, 10))

    player.draw(screen)
    coin.draw(screen)
    coin.ChangeSpeed(speed)
    player.move()
    coin.move()

    if player.rect.colliderect(coin.rect):
        coin.__init__()
        coins += 1
    
    pygame.display.flip()
    clock.tick(FPS)