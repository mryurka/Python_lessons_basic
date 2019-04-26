# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def my_calc(a, b):
    wrong_list = ('*', '+', '-', '!', '@', '#', '$', '%', '^',
                       ',', '.', '?', '~', '`')
    err = 'Неверные параметры! Формат ввода: "n x/y" ,где n - целая часть, x - числитель, у - знаменатель.'
    if (type(a) is str) and (type(b) is str):
        a_list, b_list = a.split(), b.split()
        n_dict = {'a_num': None, 'a_fraction': {'a_numerator': None, 'a_denominator': None},
                  'b_num': None, 'b_fraction': {'b_numerator': None, 'b_denominator': None}}
        # print(a_list, b_list)
        tag = 'a'
        for item in (a_list, b_list):
            if len(item) == 1:  # Если да, то у нас либо только целая часть либо дробь (1 элемент str в списке)
                # print("Один элемент а_лист", item)
                item = item[0].split('/')
                # print("Один элемент после разделения а_лист", item)
                if len(item) == 1:  # Если да значит разделить по '/' не получилось, следовательно там целая чсть
                    # print("Только целая часть", item)
                    if item[0] not in wrong_list:
                        n_dict[f'{tag}_num'] = int(item[0])
                        # print(n_dict)
                    else:
                        return err
                else:  # Разделилось по "/" значит это дробь без целого числа
                    # print("Дробь без целого числа", item)
                    if item[0] not in wrong_list and item[1] not in wrong_list:
                        n_dict[f'{tag}_fraction'][f'{tag}_numerator'] = int(item[0])
                        n_dict[f'{tag}_fraction'][f'{tag}_denominator'] = int(item[1])
                        # print(n_dict)
                    else:
                        return err
            else:
                # print("Список из двух элеменов, значит это полная дробь", item)
                item[1] = item[1].split('/')
                if len(item[1]) != 1 and item[0] not in wrong_list and item[1][0] not in wrong_list and item[1][1] not in wrong_list:
                    # print('split', item)
                    n_dict[f'{tag}_num'] = int(item[0])
                    n_dict[f'{tag}_fraction'][f'{tag}_numerator'] = int(item[1][0])
                    n_dict[f'{tag}_fraction'][f'{tag}_denominator'] = int(item[1][1])
                    # print(n_dict)
                else:
                    return err
            tag = 'b'
        # ---------------------- математика ------------------
        import math
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        a_num, b_num = n_dict['a_num'], n_dict['b_num']
        a_numerator, b_numerator = n_dict['a_fraction']['a_numerator'], n_dict['b_fraction']['b_numerator']
        a_denominator, b_denominator = n_dict['a_fraction']['a_denominator'], n_dict['b_fraction']['b_denominator']
        if a_num:
            a_numerator = (a_numerator + (a_num * a_denominator))
        if b_num:
            b_numerator = (b_numerator + (b_num * b_denominator))
        if a_denominator != b_denominator:
            denominator = a_denominator * b_denominator
            numerator = (a_numerator * b_denominator) + (b_numerator * a_denominator)
        else:
            denominator = a_denominator
            numerator = a_numerator + b_numerator
        if numerator > denominator:
            num = numerator // denominator
            numerator = numerator % denominator
            p_result = f'{num} {numerator}/{denominator}'
        else:
            p_result = f'{numerator}/{denominator}'
        # --------------------------------------------------------------------------------------------------
        a_num, b_num = n_dict['a_num'], n_dict['b_num']
        a_numerator, b_numerator = n_dict['a_fraction']['a_numerator'], n_dict['b_fraction']['b_numerator']
        a_denominator, b_denominator = n_dict['a_fraction']['a_denominator'], n_dict['b_fraction']['b_denominator']
        if a_num:
            a_numerator = (a_numerator + (a_num * a_denominator))
        if b_num:
            b_numerator = (b_numerator + (b_num * b_denominator))
        if a_denominator != b_denominator:
            denominator = a_denominator * b_denominator
            numerator = (a_numerator * b_denominator) - (b_numerator * a_denominator)
        else:
            denominator = a_denominator
            numerator = a_numerator - b_numerator
        if math.fabs(numerator) > denominator:
            num = numerator // denominator
            numerator = numerator % denominator
            m_result = f'{num} {numerator}/{denominator}'
        else:
            m_result = f'{numerator}/{denominator}'
        res = p_result, m_result
    else:
        res = err
    return res


x = '2 2/5'  # первая дробь к ней будем прибавлять из неё вычитать
y = '1/4'  # вторая её будем прибавлять и вычитать

print("Функция возвращает кореж из двух значений [0] --> сумма, [1] --> разность:")
print(my_calc(x, y))
# или можно вывести вот так:
res = my_calc(x, y)
if type(res) is not str:
    print(f"Сумма = {res[0]}, разность = {res[1]}")
else:
    print(res)
print("-" * 50)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
