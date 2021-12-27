
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

# 5.	*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json

FOLDER = r"C:\Users\Andrei\Downloads"
stat_dict = {}
try:
    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            border = 10 ** len(str(file_size))  # расчёт границы.
            if stat_dict.get(border):
                _ = set(stat_dict[border][1])  # взять текущий список расширений и преобразовать в множество
                _.add(os.path.splitext(file)[1])  # добавить в множество новое значение, автматическая проверка на повтор.
                stat_dict[border] = (stat_dict[border][0] + 1, list(_))  # +1 в количество и сохранение новых значений в словать.
            else:
                stat_dict[border] = (1, [str(os.path.splitext(file)[1])])  # если значения для границы ещё нет в словаре - добавить.

    stat_dict = {key: stat_dict[key] for key in sorted(stat_dict)}  # сортировка полученного словаря

    with open(f"{os.path.split(FOLDER)[1]}_summary.json", "w", encoding="utf-8") as f:  # сохранение в файл json
        json.dump(stat_dict, f, indent=4, ensure_ascii=True)
    print(stat_dict)

except FileNotFoundError as e:
    print(f"Не найден файл или папка: {FOLDER}")
    exit(1)
