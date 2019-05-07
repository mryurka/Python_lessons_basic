import os
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
FOLDER = os.getcwd()

dir_name = "dir_"
print("Текущая папка -->", FOLDER)
for index in range(1, 10):
    try:
        os.mkdir(dir_name + str(index))
    except FileExistsError:
        print(f"Ошибка создания! Папка {dir_name + str(index)} уже существует...")
    else:
        print("Создана папка -->", os.path.abspath(dir_name + str(index)))
print("-" * 50)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
dir_lst = os.listdir(FOLDER)
print("Содержимое папки -->", FOLDER)
mark = 1
for item in dir_lst:
    if os.path.isdir(os.path.join(FOLDER, item)):
        print(f"{mark})folder ../", item)
    else:
        print(f"{mark})file ---->", item)
    mark += 1
print("-" * 50)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print("Текущая папка -->", FOLDER)
file = sys.argv[0]
file_name = os.path.split(file)[1]
print("Копируется файл -->", file_name)
shutil.copy(file, f"copy_{file_name}")
print(f"Файл скопирован, имя копии --> copy_{file_name}")


