import pygame, mycomplex

width = 640
height = 480
xmin = -2
xmax = 1
ymin = -1
ymax = 1
pygame.init()
pygame.display.set_mode((width, height))
pygame.display.set_caption('Mmandelbrot Set')
screen = pygame.display.get_surface()
