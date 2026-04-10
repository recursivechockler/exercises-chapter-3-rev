from numbers import Number

def derivative(poly):
    return poly.dx()

class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            negpoly = Polynomial(tuple(-c for c in other.coefficients))

            return self + negpoly
        
        if isinstance(other, Number):
            return self - Polynomial((other,))
        
        return NotImplemented
    
    def __rsub__(self, other):
        if isinstance(self, Polynomial):
            negpoly = Polynomial(tuple(-c for c in self.coefficients))

            return other + negpoly
        
        if isinstance(self, Number):
            return other - Polynomial((self,))
        
        return NotImplemented

    def __mul__(self, other):

        if isinstance(other, Number):
            return Polynomial(tuple(c * other for c in self.coefficients))
        
        if isinstance(other, Polynomial):
            total = Polynomial((0,))

            for pow, c in enumerate(self.coefficients):
                total += Polynomial(tuple(pow * (0,) + tuple(c * oc for oc in other.coefficients)))
            
            return total
        
        return NotImplemented

    def __rmul__(self,other):
        return self * other
    
    def __pow__(self, other):
        
        if other == 0:
            return Polynomial((1,))
        
        return self * (self ** (other-1))
    
    def __call__(self, value):
        return sum(c * (value ** pow) for pow, c in enumerate(self.coefficients))
    
    def dx(self):
        if len(self.coefficients) == 1:
            return Polynomial((0,))

        return Polynomial(tuple((pow) * c for pow, c in enumerate(self.coefficients))[1:])