import math
import sys


def leng(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)


class dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class triangle:
    def __init__(self, AB, BC, CA):
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def area(self):
        p = (self.AB + self.BC + self.CA) / 2
        return math.sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.CA))


class start:
    mass = []
    mass_t = []
    wrong_t = 0

    def __init__(self, file):
        self.file = file

    def check(self):
        for item in self.file:
            if len(item.split(' ')) == 6:
                self.mass.append(item.split(' '))
        for item in self.mass:
            A, B, C = dot(float(item[0]), float(item[1])), dot(float(item[2]), float(item[3])), dot(float(item[4]),
                                                                                                    float(item[5]))

            AB, BC, CA = leng(A, B), leng(B, C), leng(C, A)
            self.wrong_t += 1
            if AB + BC + CA - 2 * max(AB, BC, CA) > 0 and (AB == BC or BC == CA or AB == CA):
                self.mass_t.append(triangle(AB, BC, CA))
            else:
                if AB + BC + CA - 2 * max(AB, BC, CA) <= 0:
                    print('Треугольник ', self.wrong_t, ' - не подходит (он неправильный)')
                if AB != BC != CA and BC != CA:
                    print('Треугольник ', self.wrong_t, ' - не подходит (он не равнобедренный)')


f = open(sys.stdin.readline()[:-1], 'r')
s = start(f)
s.check()
S_max = 0.0
f.close()
for item in s.mass_t:

    if item.area() > S_max:
        S_max = item.area()
if s.mass_t:
    print('Максимальная площадь',S_max)
else:
    print('Все треугольники не подходят')
