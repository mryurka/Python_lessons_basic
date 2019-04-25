
__author__ = 'Айвазовский Юрий Валентинович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m, check=False):
    # Xn+2=Xn+Xn+1 - уравнение
    result = None
    if m >= n:
        row = [1, 1]  # Первые элементами ряда
        x = 0
        while x < m:
            res = row[x] + row[x+1]
            x += 1
            row.append(res)
            result = row[n:m + 1]
            if check:
                check = list(enumerate(row))
    else:
        result = 'Ошибка! Начало ряда не должно быть раньше конца, попробуйте шщё разок!'
    if check and result:
        return result, check
    return result


n = 5
m = 8
print(f"Фибонача c {n} по {m} элемент:", fibonacci(5, 18))
print('-' * 50)

# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    from math import inf
    copy_list = origin_list.copy()
    result = []
    while copy_list:
        x = inf
        for item in copy_list:
            if item > x:
                continue
            x = item
        result.append(x)
        copy_list.remove(x)
    return result


original_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sorted_list = sort_to_max(original_list)
print("Оригиналный спсиок ------>:", original_list)
print("Список после сортировки ->:", sorted_list)
print('-' * 50)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, sequence):
    print(func)
    print(sequence)


my_filter("Here it is", (1, 2, 3))
print('-' * 50)
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogram(**kwargs):
    from math import sqrt
    (x1, y1) = kwargs["A"]
    (x2, y2) = kwargs["B"]
    (x3, y3) = kwargs["C"]
    (x4, y4) = kwargs["D"]
    # Найдём стороны
    AB = round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
    DC = round(sqrt((x4 - x3)**2 + (y4 - y3)**2), 2)
    AD = round(sqrt((x4 - x1)**2 + (y4 - y1)**2), 2)
    BC = round(sqrt((x3 - x2)**2 + (y3 - y2)**2), 2)
    # проверим
    if AB == DC and AD == BC:
        return f"""Судя по определению, которое говорит нам, что у параллелограмма стороны попарно равны, 
        данные точки являются вершинами параллелограмма т.к. AB({AB}) = DC({DC}) и AD({AD}) = BC({BC})"""
    else:
        return f"""Данные точки НЕ являются вершинами параллелограмма"""

        print("AB =", AB)
        print("DC =", DC)
        print("AD =", AD)
        print("BC =", BC)


points = {"A": (1, 3), "B": (4, 7), "C": (2, 8), "D": (-1, 4)}  # Словарик координат точек для проверки
print("Точки", points)
print(parallelogram(**points), "\n")  # Вызов функции и вывод результата
print("И ещё разок с другими точками:")
print("Точки", points)
points = {"A": (4, 3), "B": (4, 6), "C": (1, -8), "D": (-1, 4)}  # Словарик координат точек для проверки
print(parallelogram(**points))  # Вызов функции и вывод результата
print('----- EOF -----')
