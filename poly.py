
class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial" + str(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __sub__(self, other):
        return Polynomial(*(x - y for x, y in zip(self.coeffs, other.coeffs)))

    def __mul__(self, other):
        coeffs = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i, x in enumerate(self.coeffs):
            for j, y in enumerate(other.coeffs):
                coeffs[i+j] += x * y
        return Polynomial(*coeffs)

    def __call__(self, x):
        res = 0
        for i, coeff in enumerate(self.coeffs):
            res += coeff * x**i
        return res