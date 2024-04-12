import pygame
from random import randint

pygame.init()

WHITE = (255, 255, 255)
GRAY = (0, 70, 70)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RANDOM_COLOR = (125, 125, 125)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CELL = 30

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

COLORS = [WHITE, BLACK, BLUE, RANDOM_COLOR]

FPS = 5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate():
        return Point(randint(0, SCREEN_WIDTH // CELL - 1) * CELL, randint(0, SCREEN_HEIGHT // CELL - 1) * CELL)

class Food:
    def __init__(self, weight):
        self.pos = Point.generate()
        self.weight = weight
        self.timer = FPS * 10  #Disappear after 10 seconds

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()
        self.timer = FPS * 10  #Reset timer

class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL
        if head.x == SCREEN_WIDTH:
            head.x = 0
        if head.x < 0:
            head.x = (SCREEN_WIDTH // CELL - 1) * CELL
        if head.y == SCREEN_HEIGHT:
            head.y = 0
        if head.y < 0:
            head.y = (SCREEN_HEIGHT // CELL - 1) * CELL

    def check_collision(self, food_list):
        head = self.body[0]
        for food in food_list:
            if head.x == food.pos.x and head.y == food.pos.y:
                self.body.append(Point(head.x , head.y))
                print("Food! New length is: ", len(self.body))
                food.regenerate()  #Regenerate the food
                return True
        return False

    def draw(self, screen):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, GREEN, (segment.x, segment.y, CELL, CELL))

clock = pygame.time.Clock()
snake = Snake()
food_list = [Food(weight=1), Food(weight=2), Food(weight=3)]  #Foods with different weights

running = True
counter = 0
background_color_index = 0

font = pygame.font.SysFont("Verdana", 25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT:
                snake.dx = 1 
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1 
                snake.dy = 0

    screen.fill(COLORS[background_color_index])

    snake.move()
    if snake.check_collision(food_list):
        counter += 1

    for food in food_list:
        food.timer -= 1
        if food.timer <= 0:
            food_list.remove(food)

    if counter >= 4 and counter < 8:
        background_color_index = 1
    elif counter >= 8 and counter < 12:
        background_color_index = 2
    elif counter >= 12:
        background_color_index = 3

    coins_counter = font.render(str(counter), True, GRAY)
    screen.blit(coins_counter, (SCREEN_WIDTH - 50, 10))
    coins_counter_fon = font.render(str(background_color_index), True, GRAY)
    screen.blit(coins_counter_fon, (SCREEN_WIDTH - 50, CELL))

    for food in food_list:
        food.draw(screen)

    snake.draw(screen)

    pygame.display.flip()
    clock.tick(FPS + background_color_index * 5)  #since game is accelerating