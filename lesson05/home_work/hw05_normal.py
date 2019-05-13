import os
import shutil

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from hw05_easy import disp_folder
from hw05_easy import mk_folder
from hw05_easy import rm_folder


def game_over():  # command 0
    return True


def goto():  # command 1
    destination = input('Введите полный путь для перехода и нажмите "Enter": ')
    try:
        os.chdir(destination)
    except FileNotFoundError:
        print("Ошибка такого каталога не существует, попробуйте ещё раз")
    else:
        print("Текущий каталог изменён на:", os.getcwd())


def disp():  # command 2
    disp_folder(os.getcwd())


def remove():  # command 3
    work_dir = os.getcwd()
    del_dir_name = input("Введите название папки для удаления: ")
    confirmation = input(f'Вы уверены что хотите удалить папку {del_dir_name} включая все вложенные папки и файлы? \
Выберите Y если ДА или N если нет и нажмите "Enter" :')
    if confirmation == 'Y' or confirmation == 'y':
        print(rm_folder(os.path.join(work_dir, del_dir_name)))
        #    print("Ошибка удаления такого каталога не существует, попробуйте ещё раз")
    else:
        print('Удаление не подтверждено, для подтверждения нужно выбрать "Y"')


def mkdir():  # command 4
    work_dir = os.getcwd()
    new_dir_name = input("Введите название новой папки: ")
    print(mk_folder(work_dir, new_dir_name))



commands = [game_over, goto, disp, remove, mkdir]  # список из функций для удобства вызова (порядок как в меню!)
enough = False
while not enough:
    # -------------------получаем и очищаем комманду пользователя----------------------------------
    txt = f"""\nВаш текущий рабочий каталог {os.getcwd()} 
    Пожалуйста выберете действие от 1 - 5 или 0 для выхода и нажмите "Enter": 
        0. Выйти из программы
        1. Перейти в папку
        2. Просмотреть содержимое текущей папки
        3. Удалить папку
        4. Создать папку
           Ваш выбор --> """
    input_command = input(txt)
    try:
        input_command = int(input_command)
        if input_command in range(0, 5):
            com_clear = input_command
        else:
            com_clear = ("Input error: value not in options range (from 0 to 4)", input_command)
    except ValueError:
        com_clear = ("Input error: Value is not correct", input_command)
    # -----------------Вызываем функции в зависимости от комманды---------------------------------
    if type(com_clear) is int and com_clear != 0:
        commands[com_clear]()
    elif type(com_clear) is int and com_clear == 0:
        enough = True
    else:
        print(com_clear)

