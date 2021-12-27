
__author__ = "Госович Андрей Михайлович"

# 4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

FOLDER = r"C:\Users\Andrei\Downloads"
stat_dict = {}
try:
    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            border = 10 ** len(str(file_size))  # расчёт границы.
            if stat_dict.get(border):
                stat_dict[border] += 1
            else:
                stat_dict[border] = 1

    stat_dict = {key: stat_dict[key] for key in sorted(stat_dict)}  # сортировка полученного словаря
    print(stat_dict)

except FileNotFoundError as e:
    print(f"Не найден файл или папка: {FOLDER}")
    exit(1)
