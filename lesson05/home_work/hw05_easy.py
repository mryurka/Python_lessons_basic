import os
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mk_folder(folder=os.getcwd(), dir_name="new_dir"):
    full_name = os.path.join(folder, dir_name)
    try:
        os.mkdir(full_name)
    except FileExistsError:
        return f"Ошибка создания! Папка {dir_name} уже существует..."
    else:
        return "Создана папка -->", os.path.abspath(dir_name)


def rm_folder(del_dir_name, folder=os.getcwd()):
    full_name = os.path.join(folder, del_dir_name)
    try:
        shutil.rmtree(full_name)
    except FileNotFoundError:
        return "Ошибка удаления такого каталога не существует"
    else:
        return f"Папка {del_dir_name} - удалена"


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def disp_folder(folder=os.getcwd()):
    dir_lst = os.listdir(folder)
    print("Содержимое папки -->", folder)
    mark = 1
    for item in dir_lst:
        if os.path.isdir(os.path.join(folder, item)):
            print(f"{mark})folder ../", item)
        else:
            print(f"{mark})file ---->", item)
        mark += 1


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def simple_file_copy(folder=os.getcwd()):
    print("Текущая папка -->", folder)
    file = sys.argv[0]
    file_name = os.path.split(file)[1]
    print("Копируется файл -->", file_name)
    shutil.copy(file, f"copy_{file_name}")
    print(f"Файл скопирован, имя копии --> copy_{file_name}")


if __name__ == '__main__':
    print("--- Задача-1 ---")
    for index in range(1, 10):
        my_name = 'dir_' + str(index)
        print(mk_folder(dir_name=my_name))
    npt = input('\nУдалить ранее созданые папки? Y or N затем  "Enter"')
    if npt == 'Y' or npt == 'y':
        for index in range(1, 10):
            my_name = 'dir_' + str(index)
            print(rm_folder(del_dir_name=my_name))

    print("-" * 50)
    print("--- Задача-2 ---")
    disp_folder()
    print("-" * 50)
    print("--- Задача-3 ---")
    simple_file_copy()
    print("-" * 50)


