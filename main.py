import pygame
pygame.init()

WIDTH = 600
HEIGHT = 200
pygame.draw.rect(600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly Junior")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    BACKGROUND = (220, 240, 220)
    BOARD = (245, 245, 220)
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 48)
    screen.fill((220,240,220))
    pygame.display.flip()

pygame.quit()
