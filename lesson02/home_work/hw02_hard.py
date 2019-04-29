__author__ = 'Айвазовский Юрий Валентинович'
import math
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
print("Дано уравнениие:", equation)
print("Определить координату y точки с заданной координатой x")
x = 2.5
print("х =", x)
equation = 'y = -12x + 11111140.2121'.replace("x", ' * {}'.format(x))
equation = eval(equation[4:])

print("Коорднаты точки равны:", equation)
print("-" * 50)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date1 = '01.22.1001'
date2 = '1.12.1001'
date3 = '-2.10.3001'
date4 = '45.13.81855'

date_list_str = date4.split('.')

month = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30,
         "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}

date_list_int = []
for item in date_list_str:
    num = int(item)  # сделали числом
    date_list_int.append(int(math.fabs(num)))  # очистили знак
# ------------------------------------month---------------------------------------------------------
if date_list_int[1] <= 12:
    if date_list_int[1] > 9:
        ready_month = str(date_list_int[1])
    else:  # добавим 0 в к началу для красоты
        ready_month = "0" + str(date_list_int[1])
else:
    ready_month = 'err'
    print('Не верно введён месяц, он должен быть целвм числом от 1 до 12 в формате даты: дд.мм.гггг')
# ------------------------------------day---------------------------------------------------------
if ready_month != 'err':
    if date_list_int[0] <= month[ready_month]:
        if date_list_int[0] > 9:
            ready_day = str(date_list_int[0])
        else:  # добавим 0 в к началу для красоты
            ready_day = "0" + str(date_list_int[0])
    else:
        ready_day = 'err'
        print('Не верно введён день, он должен быть целвым числом от 1 до 30(31) в формате даты: дд.мм.гггг')
else:
    ready_day = '!-->'
# -------------------------------------year-------------------------------------------------------
if date_list_int[2] > 1 < 9999:
    ready_year = str(date_list_int[2])
    if len(ready_year) != 4:
        ready_year = 'err'
        print('Не верно введён день, он должен быть целым числом от 1 до 30(31) в формате даты: дд.мм.гггг')
else:
    ready_year = 'err'
    print('Не верно введён день, он должен быть целым числом от 1 до 30(31) в формате даты: дд.мм.гггг')


print(f"Дата правильного вида: {ready_day}.{ready_month}.{ready_year}")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


room = 0
level = 1
floor = 0

target = int(input("Введите, пожалуйста, номер искомой комнаты 1 ≤ N ≤ 2 000 000 000:"))

if target <= 1 >= 2000000000:
    print('Неверный номер квартиры, попробуйте ещё раз')
else:
    stop = False
    while not stop:
        # print("Level", level)
        for _ in range(level):
            if not stop:
                floor += 1
                # print("floor", floor)
                doors_left = 0
                for _ in range(level):
                    doors_left += 1
                    room += 1
                    # print("Room", room)
                    if room == target:
                        print(f"Этаж: {floor}, Комната {doors_left}-я слева")
                        stop = True
                        break
            else:
                break
        level += 1

