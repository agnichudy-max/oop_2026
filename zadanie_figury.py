
# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()

# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie

from math import pi

class FiguraGeometryczna: #tu wpisujemy co mamy zrobic ale bez szczegolowych obliczen np: policz pole

    def policz_pole(self):
        pass

    def policz_obwod(self):
        pass


class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_obwod(self):
        return self.a *2 + self.b * 2

    def policz_pole(self):
        return self.a * self.b


class Kwadrat(FiguraGeometryczna):
    def __init__(self, c):
        self.c = c

    def policz_obwod(self):
        return self.c *4

    def policz_pole(self):
        return self.c * self.c

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r

    def policz_pole(self): # pi * r **2
        return pi * self.r **2

    def policz_obwod(self): #2 * pi * r
        return 2 * pi * self.r


class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c, h):
        self.c = c
        self.h = h
        self.a = a
        self.b = b

    def policz_pole(self):  # opcja pierwsza a * h/2
        return self.a * self.h/2

    def policz_obwod(self):  # a+b+c
        return self.a + self.b + self.c


##inna metoda obliczanaia pola trojkata
# def policz_pole(self):
    # p = (self.a + self.b +self.c)/2
    # return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5




