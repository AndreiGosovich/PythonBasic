
__author__ = "Госович Андрей Михайлович"

# 4.	*(вместо 3) Решить задачу 3 для ситуации,
# когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл
# (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

import sys

with open("users.csv", "r", encoding="utf-8") as users, open("hobby.csv", "r", encoding="utf-8") as hobby,\
        open("users_hobby.txt", "w", encoding="utf-8") as f:
    for person in users:
        line = hobby.readline().splitlines()
        print(f'{person.splitlines()[0]}: {line[0] if line else None}', file=f)
    if hobby.readline():
        sys.exit(1)
