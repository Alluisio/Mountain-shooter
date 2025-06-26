import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mountain Shooter")

while True:
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()