import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

WHITE = (255, 255, 255)
GRAY = (70, 70, 70)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RANDOM_COLOR = (125, 125, 125)

COLORS = [WHITE, BLACK, BLUE, RANDOM_COLOR]

CELL = 60
FPS = 5

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def generate():
        return Point(randint(0, SCREEN_WIDTH // CELL - 1) * CELL, randint(0, SCREEN_HEIGHT // CELL - 1) * CELL)

class Food:
    def __init__(self):
        self.pos = Point.generate()

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()

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

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x , head.y))
            print("Got food! Lenght is:", len(self.body))
            return True

    def draw(self, screen):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x, segment.y, CELL, CELL))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
# our class
snake = Snake()
food_1 = Food()

def draw_grid():
    for i in range(0, SCREEN_HEIGHT, CELL):
        for j in range(0, set.SCREEN_WIDTH, CELL):
            pygame.draw.rect(screen, set.GRAY, (i, j, CELL, CELL), 1)

running = True
counter = 0
counter_fon = 0

font = pygame.font.Font("font", 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # move our snake
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
    screen.fill(COLORS[counter_fon])

    snake.move()
    for i in range(len(snake.body) - 1, 0, -1):
        if food_1.pos.x == snake.body[i].x and food_1.pos.y == snake.body[i].y:
            food_1.regenerate()
    if snake.check_collision(food_1):
        counter += 1
        food_1.regenerate()

    coins_counter = font.render(str(counter), True, GRAY)
    screen.blit(coins_counter, (SCREEN_WIDTH - 50, 10))
    coins_counter_fon = font.render(str(counter_fon), True, GRAY)
    screen.blit(coins_counter_fon, (SCREEN_WIDTH - 50, CELL))
    
    if counter >= 4 and counter <8:
        counter_fon = 1
    if counter >= 8 and counter <12:
        counter_fon = 2
    if counter >= 12:
        counter_fon = 3

    snake.draw(screen)
    food_1.draw(screen)
    draw_grid()

    pygame.display.flip()
    clock.tick(FPS + counter_fon * 5)