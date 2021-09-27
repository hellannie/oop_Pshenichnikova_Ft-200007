from math import *
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def output(self):
        print("Точка с координатами:({0};{1})".format(self.x, self.y))

class Triangle:
    vertex1 = Point(0,0)
    vertex2 = Point(0,0)
    vertex3 = Point(0,0)
    side1 = 0
    side2 = 0
    side3 = 0
    def __init__(self,a,b,c):
        self.vertex1 = a
        self.vertex2 = b
        self.vertex3 = c
        self.side1 = sqrt(pow((self.vertex2.x-self.vertex1.x),2)+pow((self.vertex2.y-self.vertex1.y),2))
        self.side2 = sqrt(pow((self.vertex3.x-self.vertex2.x),2)+pow((self.vertex3.y-self.vertex2.y),2))
        self.side3 = sqrt(pow((self.vertex1.x-self.vertex3.x),2)+pow((self.vertex1.y-self.vertex3.y),2))
    def output(self):
        print("Треугольник с координатами вершин: ({0};{1}),({2};{3}),({4};{5})".format(self.vertex1.x,self.vertex1.y,self.vertex2.x,self.vertex2.y,self.vertex3.x,self.vertex3.y))
        print("Стороны треугольника:{0},{1},{2}".format(self.side1,self.side2,self.side3))
        print("Периметр треугольника:",self.perimeter())
        print("Площадь треугольника:",self.square())
    def perimeter(self):
        return self.side1+self.side2+self.side3
    def square(self):
        half_perimeter = self.perimeter()/2
        return sqrt(half_perimeter*(half_perimeter-self.side1)*(half_perimeter-self.side2)*(half_perimeter-self.side3))


class Circle:
    center = Point(0,0)
    radius = 0
    def __init__(self, x, y,n):
        self.x = x
        self.y = y
        self.radius = n

a_x, a_y = map(float,input().split())
a = Point(a_x, a_y)
b_x, b_y = map(float,input().split())
b = Point(b_x, b_y)
c_x, c_y = map(float,input().split())
c = Point(c_x, c_y)
abc = Triangle(a,b,c)
abc.output()
