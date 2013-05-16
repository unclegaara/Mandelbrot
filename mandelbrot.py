import pygame, sys

class State(object):
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def zoom(self, x, y):
        w = (self.xmax - self.xmin) / scale
        h = (self.ymax - self.ymin) / scale
        xmin = x - w / 2
        ymax = y + h / 2
        xmax = x + w / 2
        ymin = y - h / 2
        return State(xmin, xmax, ymin, ymax)

    def getpos(self, i, j):
        x = self.xmin + (float(i) * (self.xmax - self.xmin) / width)
        y = self.ymax - (float(j) * (self.ymax - self.ymin) / height)
        return x, y


width = 640
height = (width / 3) * 2
linecolor = (0, 0, 0)
background = (255, 255, 255)
maxi = 255
scale = 4.0
steplist = [State(xmin=-2.0, xmax=1.0, ymin=-1.0, ymax=1.0)]


def draw(screen, state):
    for i in xrange(0, width - 1):
        for j in xrange(0, height - 1):
            x, y = state.getpos(i, j)
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
    draw(screen, steplist[-1])
    while True:
        events = [pygame.event.wait()]
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    i, j = event.pos
                    x, y = steplist[-1].getpos(i, j)
                    steplist.append(steplist[-1].zoom(x, y))
                    draw(screen, steplist[-1])
                elif event.button == 3:
                    if len(steplist) > 1:
                        steplist.pop()
                        draw(screen, steplist[-1])


if __name__=='__main__':
    main()
