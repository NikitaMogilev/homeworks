class triangle:

    def __init__(self, a, b, c):
        self._check_triagle_exist(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def _check_triagle_exist(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        raise ValueError('This triangle impossiable')

    def get_sides(self):
        return f'Trangle {self.a}, {self.b}, {self.c}'

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        import math
        p = (self.a + self.b + self.c) / 2
        hight_a = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a
        squre = self.a * hight_a * 0.5
        return squre

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        elif self.a**2 + self.c**2 == self.b**2:
            return True
        elif self.b**2 + self.c**2 == self.c**2:
            return True
        else:
            return False

    def __eq__(self, other):
        perimetr1 = self.perimetr()
        perimetr2 = other.perimetr()
        return perimetr1 == perimetr2


tr1 = triangle(8, 4, 6)
tr2 = triangle(7, 4, 6)
print(tr1.is_right_angled())
print(tr1 != tr2)
