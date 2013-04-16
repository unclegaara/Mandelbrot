import pygame, sys 
from mycomplex import Complex

width = 640
height = 480
xmin = -2
xmax = 1
ymin = -1
ymax = 1
linecolor = (0, 0, 0)
background = (255, 255, 255)
x0 = (width / 3) * 2
y0 = height / 2
dots = (1, 2, 3, 4, 5, 6, 7)
pygame.init()
pygame.display.set_mode((width, height))
pygame.display.set_caption('Mandelbrot Set')
screen = pygame.display.get_surface()
pygame.draw.rect(screen, (background), (0, 0, width, height), 0)
pygame.draw.aaline(screen, (linecolor), (x0, 0), (x0, height), 6)
pygame.draw.aaline(screen, (linecolor), (0, y0), (width, y0), 6)
pygame.draw.polygon(screen, (linecolor), (dots), 0)
pygame.display.flip()



while True:
    events = [pygame.event.wait()]
    for event in events:
        if event.type == pygame.QUIT:
           sys.exit()
    pass
