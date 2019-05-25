
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import os
import sys
import sqlite3


def db(city="", dictionary=False):
    city_name = city.capitalize()
    if not os.path.exists('my_weather.db'):
        return False
    else:
        try:
            db_con = sqlite3.connect("my_weather.db")
            if dictionary:
                db_con.row_factory = sqlite3.Row  # магия просто какая-то
            cursor = db_con.cursor()
            if city_name:
                query = cursor.execute(f"SELECT * FROM weather WHERE city = '{city_name}'")
            else:
                query = cursor.execute(f"SELECT * FROM weather")
            if dictionary:
                res = [dict(row) for row in query]  # Питон огонь! row_factory - рулит! :))
            else:
                res = query.fetchall()
            return res
        except sqlite3.Error:
            return False


def jSn(obj, json_file_name):
    if not json_file_name:
        json_file_name = 'exported.json'
    with open(json_file_name, 'w') as write_json:
        json.dump(obj, write_json, indent=2)


def cSv(obj, csv_file_name):
    if not csv_file_name:
        csv_file_name = 'exported.csv'
    with open(csv_file_name, 'w') as write_csv:
        writer = csv.writer(write_csv)
        for row in obj:
            writer.writerow(row)


if __name__ == "__main__":

    params = sys.argv
    len_p = len(params)
    if len_p == 1:
        print("Use: export_openweather.py --csv filename [<город>] ИЛИ export_openweather.py --json filename [<город>]")
        print('--csv или --json - обязательный параметр, задаёт формат экспорта')
        print('[filename] - не обязательный параметр, если он не введён имя файла будет "exported.json или *.csv"')
        print('[<город>] - не обязательный параметр, если он не введён экспорт затронет все города в БД')
    else:
        city = ""
        filename = ""
        if len_p > 2:
            filename = params[2]
            if len_p == 4:
                city = params[3]
        try:
            clear_p = params[1][2:]
            if clear_p.lower() == "csv":
                data_C = db(city, dictionary=False)
                if not data_C:
                    print("Ошибка, данных не существует")
                    exit()
                data_C[:0] = [('id', 'city_id', 'city', 'date', 'temperature', 'weather_id')]
                cSv(data_C, filename)
            elif clear_p.lower() == "json":
                data_J = db(city, dictionary=True)
                if not data_J:
                    print("Ошибка, данных не существует")
                    exit()
                jSn(data_J, filename)
            else:
                raise IndexError
        except IndexError:
            print("Ошибка в параметрах")
            exit()

print("Экспорт выполнен.")