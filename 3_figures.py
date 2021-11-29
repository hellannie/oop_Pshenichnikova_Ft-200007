from abc import ABCMeta, abstractmethod
from math import *

Figures = []
Figures_perimeters = []
Figures_areas = []


class Figure(object, metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def output(self):
        pass

    def __init__(self):
        Figures.append(self)


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def output(self):
        print("Точка с координатами:({0};{1})".format(self.x, self.y))


class Side:
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1
        self.length = sqrt(pow((self.b.x - self.a.x), 2) + pow((self.b.y - self.a.y), 2))

    def output(self):
        print("Отрезок с координатами: ({0};{1}), ({2},{3}); длина равна {4}".format(self.a.x, self.a.y, self.b.x,
                                                                                     self.b.y, self.length))


class Triangle(Figure):
    @property
    def name(self):
        return "Треугольник"

    def __init__(self, v1, v2, v3):
        super().__init__()
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.edge1 = Side(self.vertex1, self.vertex2)
        self.edge2 = Side(self.vertex2, self.vertex3)
        self.edge3 = Side(self.vertex3, self.vertex1)

    def perimeter(self):
        perimeter = self.edge1.length + self.edge2.length + self.edge3.length
        Figures_perimeters.append(perimeter)
        return perimeter

    def area(self):
        half_perimeter = self.perimeter() / 2
        area = sqrt(half_perimeter * (half_perimeter - self.edge1.length) * (half_perimeter - self.edge2.length) * (
                half_perimeter - self.edge3.length))
        Figures_areas.append(area)
        return area

    def output(self):
        print("Треугольник с координатами вершин: ({0};{1}),({2};{3}),({4};{5})".format(self.vertex1.x, self.vertex1.y,
                                                                                        self.vertex2.x, self.vertex2.y,
                                                                                        self.vertex3.x, self.vertex3.y))
        print("Стороны треугольника:{0},{1},{2}".format(self.edge1.length, self.edge2.length, self.edge3.length))
        print("Периметр треугольника:", self.perimeter())
        print("Площадь треугольника:", self.area())


class Rectangle(Figure):
    @property
    def name(self):
        if self.edge1.length == self.edge2.length:
            return "Квадрат"
        else:
            return "Прямоугольник"

    edge1 = Side(Point(0, 0), Point(0, 0))
    edge2 = Side(Point(0, 0), Point(0, 0))

    def __init__(self, v1, v2, v3):
        super().__init__()
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.edge1 = Side(self.vertex1, self.vertex2)
        self.edge2 = Side(self.vertex1, self.vertex3)

    def perimeter(self):
        perimeter = 2 * (self.edge1.length + self.edge2.length)
        Figures_perimeters.append(perimeter)
        return perimeter

    def area(self):
        area = self.edge1.length * self.edge2.length
        Figures_areas.append(area)
        return area

    def output(self):
        if self.edge1.length != self.edge2.length:
            print("Прямоугольник с координатами вершин, описывающие стороны ({0};{1}),({2};{3}),({4};{5})".format(
                self.vertex1.x, self.vertex1.y, self.vertex2.x, self.vertex2.y, self.vertex3.x, self.vertex3.y))
        else:
            print("Квадрат со стороной:", self.edge1.length)
        print("Периметр: ", self.perimeter())
        print("Площадь: ", self.area())


class Circle(Figure):
    def __init__(self, a1, b1):
        super().__init__()
        self.center = a1
        self.not_center = b1
        self.radius = Side(self.center, self.not_center)
    @property
    def name(self):
        return "Круг"

    def perimeter(self):
        perimeter = 2 * pi * self.radius.length
        Figures_perimeters.append(perimeter)
        return perimeter

    def area(self):
        area = pi * (self.radius.length) ** 2
        Figures_areas.append(area)
        return area

    def output(self):
        print(
            "Круг с центром в точке ({0},{1}) и радиусом {2}".format(self.center.x, self.center.y, self.radius.length))
        print("Длина окружности: {0}".format(self.perimeter()))
        print("Площадь круга: {0}".format(self.area()))


abc = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
abcd = Rectangle(Point(0, 0), Point(6, 0), Point(0, 4))
a = Rectangle(Point(0, 0), Point(4, 0), Point(0, 4))
oo1 = Circle(Point(0, 0), Point(7, 0))
for figure in Figures:
    figure.output()
    print()
