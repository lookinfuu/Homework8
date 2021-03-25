import math
from math import pi
from math import sqrt


class Figure:

    def __init__(self, *args):
        self.fig_class = args[0]
        self.a = args[1]
        if len(args) == 4:
            self.b = args[2]
        if len(args) == 5:
            self.b = args[2]
            self.c = args[3]
        self.oper = args[-1]
    
    def circle(self):
        p = 2 * pi * self.a
        s = pi * (self.a ** 2)
        print(f'Периметр: {p:.2f}')
        print(f'Площадь: {s:.2f}')

    def square(self):
        p = self.a * 4
        s = self.a ** 2
        print(f'Периметр: {p:.2f}')
        print(f'Площадь: {s:.2f}')

    def rectangle(self):
        p = self.a * 2 + self.b * 2
        s = self.a * self.b
        print(f'Периметр: {p:.2f}')
        print(f'Площадь: {s:.2f}')

    def triangle(self):
        if self.oper == 1:
            p = self.a + self.b + self.c
            print(f'Периметр: {p:.2f}')
        elif self.oper == 2:
            s = 0.5 * self.a * self.b
            print(f'Площадь: {s:.2f}')

    def ball(self):
        s = 4 * pi * (self.a ** 2)
        v = (4 / 3) * pi * (self.a ** 3)
        print(f'Площадь: {s:.2f}')
        print(f'Объем: {v:.2f}')

    def sphere(self):
        s = 4 * pi * (self.a ** 2)
        print(f'Площадь: {s:.2f}')

    def cube(self):
        s = 6 * (self.a ** 2)
        v = self.a ** 3
        print(f'Площадь: {s:.2f}')
        print(f'Объем: {v:.2f}')

    def cuboid(self):
        ab = self.a * self.b
        ac = self.a * self.c
        bc = self.b * self.c
        s = (ab + bc + ac) * 2
        v = self.a * self.b * self.c
        print(f'Площадь: {s:.2f}')
        print(f'Объем: {v:.2f}')

    def triangular_pyramid(self):
        a = self.a
        b = self.b
        s = (a / 4) * (a * sqrt(3) + 6 * b)
        v = ((a ** 2) * b) / (4 * sqrt(3))
        print(f'Площадь: {s:.2f}')
        print(f'Объем: {v:.2f}')

    def quadrangular_pyramid(self):
        a = self.a
        b = self.b
        s = a * (a + 2 * b)
        v = (1 / 3) * (a ** 2) * b
        print(f'Площадь: {s:.2f}')
        print(f'Объем: {v:.2f}')
