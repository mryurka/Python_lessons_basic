
__author__ = 'Айвазовский Юрий Валентинович'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
origin_list = [1, 2, 4, 0, -8, 16, -32, 64]
result_list = [element**2 for element in origin_list]
print("Исходный спсиок -->", origin_list)
print("Новый спсиок -->", result_list)
print('-' * 50)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
siberian_fruit = ["potato", "beet", "apple", "cucumber", "carrot", "tomato", "radish", "cabbage"]
belorussian_fruit = ["octopus", "squid", "tomato", "shrimp", "potato", "mussels", "oysters", "apple"]
proc = [fruit for fruit in siberian_fruit + belorussian_fruit if fruit in siberian_fruit and fruit in belorussian_fruit]
fruit_megamix = list(set(proc))
print('First fruit list "siberian_fruit"-->', siberian_fruit)
print('Second fruit list "belorussian_fruit"-->', belorussian_fruit)
print('Result fruit list "fruit_megamix"-->', fruit_megamix)
print('-' * 50)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
origin_list = [81, 2, 4, -12, 0, 3, -8, 16, 9, -32, 18, 64, 400, -27, 48]
result_list = [elem for elem in origin_list if not elem % 3 and elem % 4 and elem > 0]
print("Исходный спсиок -->", origin_list)
print("Новый спсиок -->", result_list)

