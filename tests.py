import unittest
from mycomplex import Complex

class ComplexTest(unittest.TestCase):
    def test_basic_operations(self):
        a = Complex(1.0, 2.0)
        self.assertEquals(a.re, 1.0)
        self.assertEquals(a.im, 2.0)
        b = Complex(3.0, 4.0)
        c = a + b
        self.assertEquals(c.re, 4.0)
        self.assertEquals(c.im, 6.0)
        c = a - b
        self.assertEquals(c.re, -2.0)
        self.assertEquals(c.im, -2.0)
        c = a * b
        self.assertEquals(c.re, -5.0)
        self.assertEquals(c.im, 10.0)
        c = a / b
        self.assertEquals(c.re, 0.44)
        self.assertEquals(c.im, 0.08)
        c = b.abs()
        self.assertEquals(c, 5.0)

if __name__ == '__main__':
    unittest.main()
