import pygame, sys
from mycomplex import Complex

width = 640
height = (width / 3) * 2
xmin = -2
xmax = 1
ymin = -1
ymax = 1
linecolor = (0, 0, 0)
background = (255, 255, 255)
maxi = 255


def main():
    pygame.init()
    pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mandelbrot Set')
    screen = pygame.display.get_surface()
    for i in xrange(0, width - 1):
        for j in xrange(0, height - 1):
            x = xmin + (float(i) * (xmax - xmin) / width)
            y = ymax - (float(j) * (ymax - ymin) / height)
            c = Complex(x, y)
            z = Complex(0.0, 0.0)
            k = 0
            while z.abs2() < 4 and k < maxi:
                z = z * z + c
                k += 1
            if k == maxi:
                r, g, b = 0, 0, 0
            else:
                r = (40 * k % 256)
                g = (26 * k % 256)
                b = (15 * k % 256)
            col = pygame.Color(r, g, b)
            screen.set_at((i, j), col)
        pygame.display.flip()

    while True:
        events = [pygame.event.wait()]
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        pass

if __name__=='__main__':
    main()
