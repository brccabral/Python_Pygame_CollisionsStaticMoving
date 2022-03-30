import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

moving_rect = pygame.Rect(350, 350, 100, 100)
x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

while True:
    for event in pygame.event.get([pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, "white", moving_rect)
    pygame.draw.rect(screen, "red", other_rect)
    pygame.display.flip()
    clock.tick(60)
