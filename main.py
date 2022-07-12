import pygame


screen = pygame.display.set_mode((640, 640))
srect = screen.get_rect()

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    pygame.display.flip()
