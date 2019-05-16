__author__ = 'Айвазовский Юрий Валентинович'
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import shelve
import os


class Person:
    def __init__(self, name):
        self.name = name  # ФИО

    def __str__(self):  # Вызывается при попытке вывода на экран объекта экземпляра класса
        return self.name

    @property
    def surname(self):
        return self.name.split()[0]

    @property
    def first_name(self):
        return self.name.split()[1]

    @property
    def patronymic_name(self):
        try:
            patronymic_name = self.name.split()[2]
        except IndexError:
            patronymic_name = "Данные отсутствуют"
        return patronymic_name

    @property
    def f_name(self):
        try:
            full_name = self.name.split()
            f_name = f"{full_name[0]} {full_name[1][0]}. {full_name[2][0]}."
        except IndexError:
            f_name = "Данные отсутствуют"
        return f_name


class Teacher(Person):
    def __init__(self, name, subject, classes_list):
        Person.__init__(self, name)
        self.subject = subject
        self.classes = classes_list


class Pupil(Person):
    def __init__(self, name, grade, father, mother):
        Person.__init__(self, name)
        self.grade = grade
        self.father = Person(father)
        self.mother = Person(mother)

    @property
    def parents(self):
        if self.father:
            parents = {"Отец": self.father.f_name}
        else:
            parents = {"Отец": "Данные отсутствуют"}
        if self.mother:
            parents["Мать"] = self.mother.f_name
        else:
            parents["Мать"] = "Данные отсутствуют"
        return parents


if __name__ == "__main__":
    # Заполняем базу данными
    just = "do not do it"
    if os.path.exists("school_db.dat"):
        npt = input("База данных уже существует, всё равно добавить записи? введите y or n и нажмите 'Enter'")
        if npt == "y" or npt == "Y":
            just = "do it"
    elif not os.path.exists("school_db.dat") or just == "do it":
        db = shelve.open("school_db")
        db['pupil_1'] = Pupil("Белоусов Евгений Иванович", "4А", "Белоусов Иван Степанович", "Белоусова Дарья Батьковна")
        db['pupil_2'] = Pupil("Шатунова Степанида Сергеевна", "4А", "Шатунов Сергей Филипович", "Шатунова Анна Павловна")
        db['pupil_3'] = Pupil("Князев Николай Игоревич", "4А", "Князев Игорь Дмитриевич", "Князева Екатерина Викторовна")
        db['pupil_4'] = Pupil("Гринёв Василий Петрович", "4Б", "Гринёв Пётр Витальевич", "Гринёва Василина Сергеевна")
        db['pupil_5'] = Pupil("Простоволосая Виктория Семёновна", "4Б", "", "Простоволосая Ева Григорьевна")
        db['pupil_6'] = Pupil("Бурая Ольга Ивановна", "5А", "Бурый Иван Алексеевич", "Бурая Владлена Даниловна")

        db['teacher_1'] = Teacher("Брежнев Сергей Петрович", "Математика", ["4А", "4Б", "5А"])
        db['teacher_2'] = Teacher("Хрущёва Любовь Ивановна", "Природоведение", ["4А", "4Б"])
        db['teacher_3'] = Teacher("Черненко Анатолий Фёдорович", "Французский", ["4Б", "5А"])
        db['teacher_4'] = Teacher("Горбачёв Василий Алибабаевич", "Литература", ["5A"])
        db.close()

    db = shelve.open("school_db")
    classes_lst = []
    for item in db:
        try:
            classes_lst.append(db[item].grade)
        except AttributeError:
            continue
    classes_set = set(classes_lst)
    print("1) Список всех классов школы -->", classes_set)
    # ---------------------------------------------------
    target_class = '4Б'
    pup_list = []
    for item in db:
        try:
            if db[item].grade == target_class:
                pup_list.append(db[item].f_name)
            else:
                continue
        except AttributeError:
            continue
    #    pup_list = [db[item].f_name for item in db if db[item].grade == target_class]
    print("2) Список учеников класса 4Б -->", pup_list)
    # ---------------------------------------------------
    target_pupil = "Простоволосая Виктория Семёновна"  # ученик информацию которого будем искать
    her_class = ""  # Сначала найдём класс ученика в базе, пропуская все объекты прочих классов т.к. в базе все в куче
    for item in db:
        try:
            if db[item].name == target_pupil:
                her_class = db[item].grade
            else:
                continue
        except AttributeError:
            continue
    pupil_subjects = []  # потом в куче находим всех учетелей этого класса и запоминаем их предметы
    for item in db:
        try:
            if her_class in db[item].classes:
                pupil_subjects.append(db[item].subject)
            else:
                continue
        except AttributeError:
            continue
    print(f"3) Список всех предметов ученика {target_pupil}  -->", pupil_subjects)
    # ------------------------------------------------------------------------------------
    her_parents = ""
    for item in db:
        try:
            if db[item].name == target_pupil:
                her_parents = db[item].parents
            else:
                continue
        except AttributeError:
            continue
    print(f"4) Родители ученика {target_pupil} --> {her_parents}")
    # ------------------------------------------------------------------------------------
    teachers = []  # можно проверять по названию объекта т.е. без try / except
    for item in db:
        if "teacher" in item and target_class in db[item].classes:
            teachers.append(db[item].f_name)
        else:
            continue
    print(f"5) Учителя преподающие в классе {target_class} --> {teachers}")

print("--- EOF ---")





