from abc import ABCMeta, abstractmethod
from math import *
import matplotlib.pyplot as plt

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
    def enter(self):
        pass

    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def graphicalOutput(self):
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
    name = ''

    def __init__(self, v1, v2, v3, tri_name):
        super().__init__()
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.name = tri_name
        self.edge1 = Side(self.vertex1, self.vertex2)
        self.edge2 = Side(self.vertex2, self.vertex3)
        self.edge3 = Side(self.vertex3, self.vertex1)
        self.points = [[self.vertex1.x, self.vertex1.y], [self.vertex2.x, self.vertex2.y],
                       [self.vertex3.x, self.vertex3.y]]

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

    def enter(self):
        pass

    def output(self):
        print("Треугольник {6} с координатами вершин: ({0};{1}),({2};{3}),({4};{5})".format(self.vertex1.x,
                                                                                            self.vertex1.y,
                                                                                            self.vertex2.x,
                                                                                            self.vertex2.y,
                                                                                            self.vertex3.x,
                                                                                            self.vertex3.y, self.name))
        print("Стороны треугольника:{0},{1},{2}".format(self.edge1.length, self.edge2.length, self.edge3.length))
        print("Периметр треугольника:", self.perimeter())
        print("Площадь треугольника:", self.area())

    def graphicalOutput(self):
        polygon = plt.Polygon(self.points, fill=False, ec='#ff0000')
        plt.gca().add_patch(polygon)


class Rectangle(Figure):
    name = ''
    edge1 = Side(Point(0, 0), Point(0, 0))
    edge2 = Side(Point(0, 0), Point(0, 0))

    def __init__(self, v1, v2, v3, v4, quad_name):
        super().__init__()
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.vertex4 = v4
        self.name = quad_name
        self.edge1 = Side(self.vertex1, self.vertex2)
        self.edge2 = Side(self.vertex2, self.vertex3)
        self.edge3 = Side(self.vertex3, self.vertex4)
        self.edge4 = Side(self.vertex4, self.vertex1)
        self.diagonal1 = Side(self.vertex1, self.vertex3)
        self.diagonal2 = Side(self.vertex2, self.vertex4)
        self.points = [[self.vertex1.x, self.vertex1.y], [self.vertex2.x, self.vertex2.y],
                       [self.vertex3.x, self.vertex3.y], [self.vertex4.x, self.vertex4.y]]

    def perimeter(self):
        if (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length) and not (
                self.edge2.length == self.edge3.length):
            perimeter = 2 * (self.edge1.length + self.edge2.length)
        elif (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length):
            perimeter = 4 * self.edge1.length
        else:
            perimeter = self.edge1.length + self.edge3.length + self.edge2.length + self.edge4.length
        Figures_perimeters.append(perimeter)
        return perimeter

    def area(self):
        if (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length) and not (
                self.edge2.length == self.edge3.length):
            area = self.edge1.length * self.edge2.length
        elif (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length):
            area = self.edge1.length ** 2
        else:
            half_perimeter = self.perimeter() / 2
            area = sqrt(half_perimeter * (half_perimeter - self.edge1.length) * (half_perimeter - self.edge2.length) * (
                    half_perimeter - self.edge3.length) * (half_perimeter - self.edge4.length))
        Figures_areas.append(area)
        return area

    def enter(self):
        pass

    def output(self):
        if (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length) and not (
                self.edge2.length == self.edge3.length):
            print("Прямоугольник {6} с координатами вершин, описывающие стороны ({0};{1}),({2};{3}),({4};{5})".format(
                self.vertex1.x, self.vertex1.y, self.vertex2.x, self.vertex2.y, self.vertex3.x, self.vertex3.y,
                self.name))
        elif (self.edge1.length == self.edge3.length) and (self.edge2.length == self.edge4.length):
            print("Квадрат {0} со стороной {1}".format(self.name, self.edge1.length))
        else:
            print("Четырёхугольник {8} с координатами:({0};{1}),({2};{3}),({4};{5}),({6},{7})".format(
                self.vertex1.x, self.vertex1.y, self.vertex2.x, self.vertex2.y, self.vertex3.x, self.vertex3.y,
                self.vertex4.x, self.vertex4.y, self.name))
        print("Периметр: ", self.perimeter())
        print("Площадь: ", self.area())

    def graphicalOutput(self):
        polygon = plt.Polygon(self.points, fill=False, ec='#00ff00')
        plt.gca().add_patch(polygon)


class Circle(Figure):
    name = ''

    def __init__(self, a1, b1, circleName):
        super().__init__()
        self.name = circleName
        self.center = a1
        self.not_center = b1
        self.radius = Side(self.center, self.not_center)

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
            "Круг {3} с центром в точке ({0},{1}) и радиусом {2}".format(self.center.x, self.center.y,
                                                                         self.radius.length, self.name))
        print("Длина окружности: {0}".format(self.perimeter()))
        print("Площадь круга: {0}".format(self.area()))

    def enter(self):
        pass

    def graphicalOutput(self):
        circle = plt.Circle((self.center.x, self.center.y), radius=self.radius.length, fill=False, ec='#0000ff')
        plt.gca().add_patch(circle)


def figureChoice(figureType):
    if figureType.lower() == "треугольник":
        print("Введите координаты точек через пробел: ")
        a_x, a_y = map(float, input("Точка 1: ").split())
        a = Point(a_x, a_y)
        b_x, b_y = map(float, input("Точка 2: ").split())
        b = Point(b_x, b_y)
        c_x, c_y = map(float, input("Точка 3: ").split())
        c = Point(c_x, c_y)
        abc_name = input("Название фигуры: ")
        abc = Triangle(a, b, c, abc_name)
        return abc
    elif figureType.lower() == "четырёхугольник" or figureType.lower() == "квадрат" or figureType.lower() == "прямоугольник":
        print("Введите координаты точек через пробел против часовой стрелки: ")
        a_x, a_y = map(float, input("Точка 1: ").split())
        a = Point(a_x, a_y)
        b_x, b_y = map(float, input("Точка 2: ").split())
        b = Point(b_x, b_y)
        c_x, c_y = map(float, input("Точка 3: ").split())
        c = Point(c_x, c_y)
        d_x, d_y = map(float, input("Точка 3: ").split())
        d = Point(d_x, d_y)
        abcd_name = input("Название фигуры: ")
        abcd = Rectangle(a, b, c, d, abcd_name)
        return abcd
    elif figureType.lower() == "круг" or figureType.lower() == "окружность":
        print("Введите координаты точек через пробел: ")
        a_x, a_y = map(float, input("Точка 1: ").split())
        a = Point(a_x, a_y)
        b_x, b_y = map(float, input("Точка 2: ").split())
        b = Point(b_x, b_y)
        ab_name = input("Название фигуры: ")
        ab = Circle(a, b, ab_name)
        return ab


f_type = str()
n = int(input("Сколько фигур вы хотите ввести?: "))
while len(Figures)!=n:
    f_type = input("Какую фигуру вы хотите ввести?")
    figureChoice(f_type)
    print()

for figure in Figures:
    figure.output()
    print()

print("Сортировка фигур по возрастанию площадей: ")
for figure in sorted(Figures, key=lambda x: x.area()):
    print("{0} = {1}".format(figure.name, figure.area()))

print("Сортировка фигур по возрастанию периметров(длин окружностей): ")
for figure in sorted(Figures, key=lambda x: x.perimeter()):
    print("{0} = {1}".format(figure.name, figure.perimeter()))

show_figs = input("Показать фигуры на плоскости? Да/Нет")
if show_figs.lower() == "да":
    for figure in Figures:
        figure.graphicalOutput()
    plt.axis('scaled')
    plt.show()