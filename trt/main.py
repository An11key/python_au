import math
import sys

f = open('1.txt', 'r')





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

    def __init__(self, file):
        self.file = file

    def check(self):
        for item in self.file:
            if len(item.split(' ')) == 6:
                self.mass.append(self.file.readlines(1)[0][:-1].split(' '))
        for item in self.mass:
            A, B, C = dot(float(item[0]), float(item[1])), dot(float(item[2]), float(item[3])), dot(float(item[4]),
                                                                                                    float(item[5]))

            AB, BC, CA = leng(A, B), leng(B, C), leng(C, A)
            if AB + BC + CA - 2 * max(AB, BC, CA) > 0 and (AB == BC or BC == CA or AB == CA):
                self.mass_t.append(triangle(AB, BC, CA))


s = start(f)
s.check()
S_max = 0.0
for item in s.mass_t:
    print(item.AB)
    if item.area() > S_max:
        S_max = item.area()
print(S_max)
