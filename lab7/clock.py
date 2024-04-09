import pygame
import os
from datetime import datetime

pygame.init()


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")


current_dir = os.path.dirname(__file__)
clock_image_path = os.path.join(current_dir, "mainclock.png")
minute_hand_image_path = os.path.join(current_dir, "rightarm.png")
second_hand_image_path = os.path.join(current_dir, "leftarm.png")

clock_image = pygame.image.load(clock_image_path)
clock_rect = clock_image.get_rect(center=(screen_width // 2, screen_height // 2))
minute_hand_image = pygame.image.load(minute_hand_image_path)
second_hand_image = pygame.image.load(second_hand_image_path)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(clock_image, clock_rect)

    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second

    minute_angle = 360 / 60 * minute
    second_angle = 360 / 60 * second

    rotated_minute_hand = pygame.transform.rotate(minute_hand_image, -minute_angle - 60)
    minute_hand_rect = rotated_minute_hand.get_rect(center=clock_rect.center)
    screen.blit(rotated_minute_hand, minute_hand_rect)

    rotated_second_hand = pygame.transform.rotate(second_hand_image, -second_angle - 55)  # nemnogo skorektirovat nado
    second_hand_rect = rotated_second_hand.get_rect(center=clock_rect.center)
    screen.blit(rotated_second_hand, second_hand_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()