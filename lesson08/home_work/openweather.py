
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import urllib.request
import urllib.error
import os
import gzip
import json
import sqlite3
import datetime


def downloader(url="http://bulk.openweathermap.org/sample/city.list.json.gz"):
    try:
        print(f"Receiving file from url")
        response = urllib.request.urlretrieve(url, "city.list.json.gz")
    except urllib.error.HTTPError:
        return False
    else:
        return response[1]


def unpacker(full_path=(os.getcwd() + os.sep + "city.list.json.gz")):
    try:
        f_name = full_path[:-3]
        with open(f_name, "wb") as output:
            with gzip.GzipFile(full_path, "rb") as arc:
                output.write(arc.read())
    except:
        return False
    else:
        return True


def get_country_list(disp=False):
    with open("city.list.json", "r", encoding='utf-8') as js_file:
        country_list = [item['country'] for item in json.load(js_file) if item['country']]
        unique_country_list = list(set(country_list))  # прогон через множество для удаления дублей
        enumerate_country_list = list(enumerate(sorted(unique_country_list), 1))  # сортровка и нумерация
        enumerate_country_dict = {item[0]: item[1] for item in enumerate_country_list}  # со словариком удобнее
        if disp:
            for item in enumerate_country_list:
                print(f"Код страны {item[1]}, номер: {item[0]}")
        return enumerate_country_dict


def get_city_id(country_code="ru"):
    cc = country_code.upper()  # код страны
    with open("city.list.json", "r", encoding='utf-8') as js_file:
        lst = [item for item in json.load(js_file) if item['country'] == cc]
        return lst


def requester(city_code):
    app_id = r'6b26813e256d78f04d5913b5c1fe938d'
    head = r"https://api.openweathermap.org/data/2.5/group?"
    param = f"id={city_code}&units=metric&appid={app_id}"
    try:
        url = head + param
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        ret = False
    else:
        lst = json.loads(response.read())
        ret = lst['list']
    return ret


def db(c_id, c_name, t, w_id):
    d_today = datetime.date.today().strftime('%Y-%m-%d')
    if not os.path.exists('my_weather.db'):
        try:
            db_con = sqlite3.connect("my_weather.db")
            cursor = db_con.cursor()
            cursor.execute("""CREATE TABLE weather
                              (id INTEGER, city_id INTEGER, city VARCHAR (255), date DATE,
                               temperature INTEGER, weather_id INTEGER, PRIMARY KEY (id, city_id))
                           """)
        except sqlite3.Error:
            return False
    try:
        db_con = sqlite3.connect("my_weather.db")
        cursor = db_con.cursor()
        cursor.execute(f"""INSERT INTO weather
                       VALUES ((SELECT IFNULL(MAX(id), 0) + 1 FROM weather), {c_id}, '{c_name}', '{d_today}', {t}, {w_id})""")
        db_con.commit()
    except sqlite3.Error:
        ret = False
    else:
        ret = True
    return ret


if __name__ == "__main__":
    if not os.path.exists('city.list.json'):
        download = downloader()
        if download:
            unpack = unpacker()
            if not unpack:
                print('Ощибка распаковки файла со списском городов')
                print("Программа завершена.")
                exit()
        else:
            print('Ощибка скачивания файла со списском городов')
            print("Программа завершена.")
            exit()

    city_list_dic = get_country_list(disp=True)
    c_code_input = input('Введите номер страны для запроса погоды или "0" для выхода: ')
    items = []
    try:
        c_code_num = int(c_code_input)
        if c_code_num == 0:
            print('Всего доброго!')
            exit()
    except ValueError:
        print("Ошибка ввода, номер страны введён некоректно")
        print("Программа завершена.")
        exit()
    else:
        try:
            items = get_city_id(city_list_dic[c_code_num])
        except KeyError:
            print("Ошибка ввода, страны с таким номером не существует")
            print("Программа завершена.")
            exit()
        else:
            small_items = [(item['name'], item['id']) for item in items]
            sorted_items = sorted(small_items)
            printed, pause = 0, 35
            for item in sorted_items:
                print(f"Город: {item[0]}, номер: {item[1]}")
                printed += 1
                if printed == pause:
                    pause += 35
                    i = input('"Enter" следующая страница "S" прекратить вывод городов: ')
                    if i.upper() == 'S':
                        break

    id_code_input = input('Введите код города для запроса погоды или "0" для выхода: ')
    try:
        id_code_num = int(id_code_input)
        if id_code_num == 0:
            print('Всего доброго!')
            exit()
    except ValueError:
        print("Ошибка ввода, код корода введён некоректно")
        print("Программа завершена.")
        exit()
    else:
        test_list = [item["id"] for item in items]
        if id_code_num in test_list:
            print(f"ОК, код города найден в списке горов!")
            request = requester(id_code_num)
            if not request:
                print(f"Sorry, Код города НЕ найден! Скорее всего он введён не корректно, попробуйте Ctrl+c -> Ctrl+v")
                print("Программа завершена.")
                exit()
            print("Запрос к сервису выполнен")
            city_id = request[0]['id']
            city = request[0]['name']
            temp = request[0]['main']['temp']
            weather_id = request[0]['weather'][0]['id']
            # weather_id = request[0]['sys']['id']
            print(f"id Города: {city_id}, Город: {city}, Температура: {temp}")
            db_result = db(city_id, city, temp, weather_id)
            if db_result:
                print("Погода сохранена в БД.")
                print("Программа завершена.")
        else:
            print("Sorry, Код города НЕ найден! Скорее всего он введён не корректно, попробуйте Ctrl+c -> Ctrl+v")
            print("Программа завершена.")

