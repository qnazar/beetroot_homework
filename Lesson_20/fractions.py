"""Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
with appropriate checking and error handling"""


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        if self.numerator == 0:
            return '0'
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    @staticmethod
    def greatest_common_divisor(a, b):
        if a % b == 0:
            return b
        else:
            return Fraction.greatest_common_divisor(b, a % b)

    @staticmethod
    def lowest_common_denominator(a, b):
        return a * b // Fraction.greatest_common_divisor(a, b)

    @staticmethod
    def clean_fraction(numerator, denominator):
        gcd = Fraction.greatest_common_divisor(numerator, denominator)
        numerator /= gcd
        denominator /= gcd
        return Fraction(int(numerator), int(denominator))

    def __add__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            denominator = self.denominator
        else:
            denominator = self.lowest_common_denominator(self.denominator, other.denominator)
            numerator = self.numerator * denominator/self.denominator + other.numerator * denominator/other.denominator
        return self.clean_fraction(numerator, denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            denominator = self.denominator
        else:
            denominator = self.lowest_common_denominator(self.denominator, other.denominator)
            numerator = self.numerator * denominator / self.denominator - other.numerator * denominator / other.denominator
        return self.clean_fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return self.clean_fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return self.clean_fraction(numerator, denominator)


x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
