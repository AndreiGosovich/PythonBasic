
__author__ = "Госович Андрей Михайлович"

# 3.	Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом  — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

import sys
import json

with open("users.csv", "r", encoding="utf-8") as users, open("hobby.csv", "r", encoding="utf-8") as hobby, \
        open("users_hobby.json", "w", encoding="utf-8") as f:
    dict_persons = {}
    person_list = users.readlines()
    hobby_list = hobby.readlines()

    if len(person_list) < len(hobby_list):
        sys.exit(1)
    for i, el in enumerate(person_list):
        dict_persons[el.replace(",", " ").splitlines()[0]] = hobby_list[i].splitlines()[0] if i <= len(hobby_list) - 1 else None

    # print(dict_persons)
    json.dump(dict_persons, f, indent=4, ensure_ascii=False)

