import pygame

WIDTH, HEIGHT = 600, 600

ROWS, COLS = 6, 6 

SQUARE_SIZE = WIDTH//COLS

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/Crown.jpeg'), (45,25))