import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 300))#, flags = pygame.NOFRAME)
running = True
pygame.display.set_caption("RACIST")

current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, "icon.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

FPS = pygame.time.Clock()
FPS.tick(60)


while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()
        
    pygame.display.update()