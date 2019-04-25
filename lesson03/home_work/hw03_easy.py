
__author__ = 'Айвазовский Юрий Валентинович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    lst = str(number).split(".")
    if ndigits >= len(lst[1]):
        return "Ошибка! Количество знаков для округление должно быть меньше чем в исходном числе, иначе какой смысл?"
    if int(lst[1][ndigits]) < 5:
        res = float(lst[0] + '.' + lst[1][:ndigits])
    else:
        res = float('0.' + lst[1][:ndigits])
        head = int(lst[0])
        zeros = "0" * (ndigits - 1)
        res = res + float(f'{head}.{zeros}1')

    return res


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 4))
print(my_round(2.9999967, 5))
print(my_round(2.1253457, 7))  # Ошибка
print(my_round(2.1234543, 5))
print(my_round(2.1234312, 4))
print("-"*50)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if type(ticket_number) == int and len(ticket_number_str) == 6:
        sum_1 = 0
        sum_2 = 0
        for item in ticket_number_str[:4]:
            sum_1 += int(item)
        for item in ticket_number_str[3:]:
            sum_2 += int(item)
        if sum_1 == sum_2:
            return "Ваш билет счастливый, поздравляю! Нужно загадать желание и скушать его..."
        else:
            return "Вам не повезло, этот билет не похож на счастливый. Зато не придётся его есть!"
    else:
        return "Неверный номер билета, номер должен быть шестизначиным и содержать только цифры."


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
