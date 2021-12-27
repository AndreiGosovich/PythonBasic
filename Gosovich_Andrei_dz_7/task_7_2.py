
__author__ = "Госович Андрей Михайлович"

# 2.	*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
# Примечание: структуру файла config.yaml придумайте сами,
# его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import task_7_1  # парсер строки с именами файлов и папок из задания 7_1

# чтение файла с конфигурацией
with open("config.yaml", "r", encoding="utf-8") as config_file:
    folders = task_7_1.get_folders_from_string(config_file.read())

# print(folders)
# создание папок и файлов
for elem in folders:
    if os.path.splitext(elem)[1]:  # проверка ниличия расширения для файла
        if not os.path.exists(elem):
            f = open(elem, "x", encoding="utf-8")
            f.close()
    else:
        if not os.path.exists(elem):
            os.makedirs(elem)
