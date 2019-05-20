#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    def __init__(self):
        line_1, line_2, line_3 = [], [], []
        self.card = (line_1, line_2, line_3)
        self.rest = 15
        for line in self.card:  # запихаем для начала по девять чисел в ряд
            while len(line) != 9:
                num = random.randint(1, 90)
                if num in self.card[0] or num in self.card[1] or num in self.card[2]:
                    continue
                else:
                    line.append(num)
        for line in self.card:
            line.sort()
            mem = None
            while line.count(" ") != 4:  # заполняем пробелами лишние 4 числа т.к. их нужно 5, а не 9
                hole = random.randint(0, 8)
                if hole != mem:
                    line[hole] = ' '
                else:
                    continue
                mem = hole

    def __str__(self):
        border = "-" * 26 + "\n"
        output, str_ln = border, ""
        for line in self.card:
            for item in line:
                if len(str(item)) < 2:
                    str_ln += f" {str(item)} "
                else:
                    str_ln += f"{str(item)} "
            output += (str_ln + "\n")
            str_ln = ""
        return output + border.rstrip('\n')

    def cross_out(self, barrel):
        res = False
        for line in self.card:
            try:
                elem = line.index(barrel)
                line[elem] = '--'
                res = True
                self.rest -= 1
            except ValueError:
                continue
        return res

    @property
    def is_empty(self):
        if self.rest <= 0:
            return True
        else:
            return False


class Pouch:
    def __init__(self):
        self.pouch = []
        self.position = -1
        while len(self.pouch) < 90:
            barrel = random.randint(1, 90)
            if barrel not in self.pouch:
                self.pouch.append(barrel)
            else:
                continue

    def __iter__(self):
        return self

    def __next__(self):
        stop = len(self.pouch) - 1
        if self.position < stop:
            self.position += 1
            return self.pouch[self.position]
        else:
            raise StopIteration


if __name__ == "__main__":
    print('Добро пожаловать в игру "Лото лайт, Бендер против Хьюмэнети"')
    npt = input("Нажмитие любую клавишу чтобы начать или 'A' - авто режим, 'Q' - для выхода, затем 'Enter': ").lower()
    user_card = Card()
    pc_card = Card()
    P = Pouch()
    stage = 1
    while npt != 'q':
        P_itr = iter(P)
        current_barrel = P_itr.__next__()
        print(f"====================== Ход номер {stage} ======================")
        print(f"Бендеру осталось вычеркнуть {pc_card.rest} цифр(ы)")
        print("+++ Карточка Бендера +++:")
        print(pc_card)
        print(f"Вам осталось вычеркнуть {user_card.rest} цифр(ы)")
        print("****** Ваша карточка ******:")
        print(user_card)
        print(f"Новый бочонок: {current_barrel} (осталось {90 - stage} бочонков)")
        # ------------------ Играет комп -------------------------
        crossed_out = pc_card.cross_out(current_barrel)
        if pc_card.is_empty:
            print("Увы! Вы проиграли. Bender вычеркнул все цифры своей карточки.")
            print("+++ Карточка Бендера +++:")
            print(pc_card)
            print("****** Ваша карточка ******:")
            print(user_card)
            break
        # ------------------ Играет юзер -------------------------------------------
        if npt == 'a':
            crossed_out = user_card.cross_out(current_barrel)
            if user_card.is_empty:
                print("Поздравляем! Вы выйграли! Все цифры Вашей карточки вычеркнуты.")
                print("+++ Карточка Бендера +++:")
                print(pc_card)
                print("****** Ваша карточка ******:")
                print(user_card)
                break
        else:
            npt = input("Зачеркнуть цифру? (y/n) или 'q' для выхода: ").lower()
            if npt == 'y':
                crossed_out = user_card.cross_out(current_barrel)
                if not crossed_out:
                    print(f"Цифры {current_barrel} не было на Вашей карточке,  Вы проиграли!")
                    npt = "q"
            elif npt == 'n':
                crossed_out = user_card.cross_out(current_barrel)
                if crossed_out:
                    print(f"Цифра {current_barrel} была на Вашей карточке,  Вы проиграли!")
                    npt = "q"
            elif npt == 'q':
                npt = "q"
            else:
                print("Ошибка ввода, неизвестная команда.")
                npt = "q"
            if user_card.is_empty:
                print("Поздравляем! Вы выйграли! Все цифры Вашей карточки вычеркнуты.")
                print("+++ Карточка Бендера +++:")
                print(pc_card)
                print("****** Ваша карточка ******:")
                print(user_card)
                break
        stage += 1

    print("Программа завершена.")

