class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)

class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMa(magnitude, self.angle + other.angle)

from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

ri = ComplexRI(5, 12)
# print(ri.real)
# print(ri.magnitude)
ri.real = 9
# print(ri.real)
# print(ri.magnitude)
# print(ComplexRI(1,2) + ComplexMA(2, pi/2))
# print(ComplexRI(0,1) + ComplexMA(0, 1))

from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMa({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)

# ma = ComplexMA(2, pi/2)
# print(ma.imag)
# ma.angle = pi
# print(ma.real)

#from fractions import gcd
from math import gcd
class Rational(Number):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)
    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

# print(Rational(2, 5) + Rational(1, 10))
# print(Rational(1, 4) * Rational(2, 3))

c = ComplexRI(1, 1)
# print(isinstance(c, ComplexRI))
# print(isinstance(c, Complex))
# print(isinstance(c, ComplexMA))

def is_real(c):
    """Return whether c is a real number with no imaginary part."""
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0

# print(is_real(ComplexRI(1, 1)))
# print(is_real(ComplexMA(2, pi)))


Rational.type_tag = 'rat'
Complex.type_tag = 'com'


def add_complex_and_rational(c, r):
    """
    We rely on the fact that a Rational can be converted approximately to a float value that is a real number.
    The result can be combined with a complex number.
    """
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

