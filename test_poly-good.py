import unittest
from unittest import TestCase
from poly import Polynomial

#tests
class TestPoly(TestCase):

    def test_addition(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(3, 2, 1)
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, (4, 4, 4))


    def test_subtraction(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(3, 2, 1)
        p3 = p1 - p2
        self.assertEqual(p3.coeffs, (-2, 0, 2))


    def test_multiplication(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(3, 2, 1)
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, (3, 8, 14, 8, 3))


    def test_evaluation(self):
        p = Polynomial(1, 2, 1)
        self.assertEqual(p(2), 9)


if __name__ == '__main__':
    unittest.main()
