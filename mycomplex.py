import math
z = []
class Complex(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, z):
        return Complex(self.re + z.re, self.im + z.im)

    def __sub__(self, z):
        return Complex(self.re - z.re, self.im - z.im)

    def __mul__(self, z):
        return Complex(self.re * z.re - self.im * z.im,
                       self.re * z.im + z.re * self.im)

    def __div__(self, z):
        reimsqrtsum = z.re * z.re + z.im * z.im
        return Complex((self.re * z.re + self.im * z.im) / reimsqrtsum,
                       (self.im * z.re - self.re * z.im) / reimsqrtsum)

    def abs(self):
        return math.sqrt(self.re * self.re + self.im * self.im)
