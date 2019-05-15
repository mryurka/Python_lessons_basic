__author__ = 'Айвазовский Юрий Валентинович'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, vert=({"x": 1, "y": 1}, {"x": 5, "y": 10}, {"x": 10, "y": 1})):
        self.a = math.sqrt((vert[1]["x"] - vert[0]["x"])**2 + (vert[1]["y"] - vert[0]["y"])**2)
        self.b = math.sqrt((vert[2]["x"] - vert[1]["x"])**2 + (vert[2]["y"] - vert[1]["y"])**2)
        self.c = math.sqrt((vert[2]["x"] - vert[0]["x"])**2 + (vert[2]["y"] - vert[0]["y"])**2)

    def get_perimeter(self):
        p = self.a + self.b + self.c
        return round(p, 2)

    def get_area(self):
        try:
            p = self.get_perimeter() / 2
            s = (math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return round(s, 2)

    def get_height(self):
        try:
            s = self.get_area()
            h_ab = round((2 * s) / self.a, 2)
            h_bc = round((2 * s) / self.b, 2)
            h_ca = round((2 * s) / self.c, 2)
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return {"H ab": h_ab, "H bc": h_bc, "H ca": h_ca}


# ---------------тесты задачи 1--------------------------------------------------
print("--- Задача-1 ---")
vertices_1 = ({"x": 4, "y": 3}, {"x": 16, "y": -6}, {"x": 20, "y": 16})
vertices_2 = ({"x": -6, "y": 1}, {"x": 2, "y": 4}, {"x": 2, "y": -2})
vertices_3 = ({"x": 7, "y": 8}, {"x": -4, "y": 5}, {"x": -1, "y": -4})

triangle_1 = Triangle(vertices_1)
print("Треугольник №1, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_1.get_perimeter(), triangle_1.get_area(), triangle_1.get_height()))
triangle_2 = Triangle(vertices_2)
print("Треугольник №2, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_2.get_perimeter(), triangle_2.get_area(), triangle_2.get_height()))
triangle_3 = Triangle(vertices_3)
print("Треугольник №2, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_3.get_perimeter(), triangle_3.get_area(), triangle_3.get_height()))

print("-" * 16)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapeze:
    def __init__(self, vert=({"x": 0, "y": 5}, {"x": -2, "y": 4}, {"x": 4, "y": 2}, {"x": 3, "y": 4})):
        self.x1, self.x2, self.x3, self.x4 = vert[0]["x"], vert[1]["x"], vert[2]["x"], vert[3]["x"]
        self.y1, self.y2, self.y3, self.y4 = vert[0]["y"], vert[1]["y"], vert[2]["y"], vert[3]["y"]
        self.a = round(math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)), 2)
        self.b = round(math.sqrt(((self.x3 - self.x2)**2) + ((self.y3 - self.y2)**2)), 2)
        self.c = round(math.sqrt(((self.x4 - self.x3)**2) + ((self.y4 - self.y3)**2)), 2)
        self.d = round(math.sqrt(((self.x1 - self.x4)**2) + ((self.y1 - self.y4)**2)), 2)

    def isosceles(self):
        try:
            if (((self.a == self.c) and ((self.x4 - self.x1) / self.d == (self.x3 - self.x2) / self.b)) or
                ((self.b == self.d) and ((self.x3 - self.x4) / self.c == (self.x2 - self.x1) / self.a)) or
               ((self.a == self.c) and (self.b == self.d)) or ((self.b == self.d) and (self.c == self.a))):
                return True
            else:
                return False
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"

    def get_perimeter(self):
        p = self.a + self.b + self.c + self.d
        return round(p, 2)

    def get_area(self):
        try:
            h = math.sqrt(self.a**2 - ((((self.d - self.b)**2) + (self.a**2 - self.c**2)) / (2 * (self.d - self.b)))**2)
            s = ((self.b + self.d) / 2) * h
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return round(s, 2)


# ---------------тесты задачи 2--------------------------------------------------
print("--- Задача-2 ---")
trap_0 = Trapeze()
print("\nТрапеция 0")
print(f'{"Точки образуют равнобедренную трапецию" if trap_0.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_0.a}, b:{trap_0.b}, c:{trap_0.c}, d:{trap_0.d}')
print(f'Периметр --> {trap_0.get_perimeter()}')
print(f'Площадь --> {trap_0.get_area()}')

trap_ver_1 = ({"x": -2, "y": -2}, {"x": -3, "y": 1}, {"x": 7, "y": 7}, {"x": 3, "y": 1})
trap_1 = Trapeze(trap_ver_1)
print("\nТрапеция 1")
print(f'{"Точки образуют равнобедренную трапецию" if trap_1.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_1.a}, b:{trap_1.b}, c:{trap_1.c}, d:{trap_1.d}')
print(f'Периметр --> {trap_1.get_perimeter()}')
print(f'Площадь --> {trap_1.get_area()}')

trap_ver_2 = ({"x": -20, "y": -15}, {"x": -10, "y": 8}, {"x": 10, "y": 8}, {"x": 20, "y": -15})
trap_2 = Trapeze(trap_ver_2)
print("\nТрапеция 2")
print(f'{"Точки образуют равнобедренную трапецию" if trap_2.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_2.a}, b:{trap_2.b}, c:{trap_2.c}, d:{trap_2.d}')
print(f'Периметр --> {trap_2.get_perimeter()}')
print(f'Площадь --> {trap_2.get_area()}')
print("-" * 16)

