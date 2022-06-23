import unittest
from fractions import Fraction


class TestFraction(unittest.TestCase):
    def setUp(self) -> None:
        self.x = Fraction(1, 2)
        self.y = Fraction(1, 4)

    def test_greatest_common_divisor(self):
        self.assertEqual(Fraction.greatest_common_divisor(2, 4), 2)
        self.assertEqual(Fraction.greatest_common_divisor(10, 10), 10)
        self.assertEqual(Fraction.greatest_common_divisor(12, 16), 4)
        self.assertEqual(Fraction.greatest_common_divisor(5, 7), 1)

    def test_lowest_common_denominator(self):
        self.assertEqual(Fraction.lowest_common_denominator(4, 10), 20)
        self.assertEqual(Fraction.lowest_common_denominator(3, 5), 15)
        self.assertEqual(Fraction.lowest_common_denominator(7, 7), 7)
        self.assertEqual(Fraction.lowest_common_denominator(8, 15), 120)

    def test_clean_fraction(self):
        self.assertEqual(Fraction.clean_fraction(8, 10), Fraction(4, 5))
        self.assertEqual(Fraction.clean_fraction(1, 10), Fraction(1, 10))
        self.assertEqual(Fraction.clean_fraction(6, 36), Fraction(1, 6))
        self.assertEqual(Fraction.clean_fraction(10, 10), Fraction(1, 1))

    def test_add(self):
        res = self.x + self.y
        self.assertEqual(res, Fraction(3, 4))

    def test_sub(self):
        res = self.x - self.y
        self.assertEqual(res, Fraction(1, 4))

    def test_mul(self):
        res = self.x * self.y
        self.assertEqual(res, Fraction(1, 8))

    def test_div(self):
        res = self.x / self.y
        self.assertEqual(res, Fraction(2, 1))
