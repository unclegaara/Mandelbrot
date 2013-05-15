import pygame, sys

width = 640
height = (width / 3) * 2
xmin = -2.0
xmax = 1.0
ymin = -1.0
ymax = 1.0
linecolor = (0, 0, 0)
background = (255, 255, 255)
maxi = 255
scale = 4.0


def getpos(i, j):
    x = xmin + (float(i) * (xmax - xmin) / width)
    y = ymax - (float(j) * (ymax - ymin) / height)
    return x, y


def draw(screen):
    print xmax, ymax, xmin, ymin
    for i in xrange(0, width - 1):
        for j in xrange(0, height - 1):
            x, y = getpos(i, j)
            c = complex(x, y)
            z = complex(0.0, 0.0)
            k = 0
            while z.real * z.real + z.imag * z.imag < 4 and k < maxi:
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


def main():
    global xmax, xmin, ymax, ymin
    pygame.init()
    pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mandelbrot Set')
    screen = pygame.display.get_surface()
    draw(screen)
    while True:
        events = [pygame.event.wait()]
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                i, j = event.pos
                x, y = getpos(i, j)
                w = (xmax - xmin) / scale
                h = (ymax - ymin) / scale
                xmin = x - w / 2
                ymax = y + h / 2
                xmax = x + w / 2
                ymin = y - h / 2
                draw(screen)

if __name__=='__main__':
    main()
