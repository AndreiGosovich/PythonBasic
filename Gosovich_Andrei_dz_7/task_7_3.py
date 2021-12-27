
__author__ = "Госович Андрей Михайлович"

# 3.	Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os
from sys import exit
import shutil


class FileExist(Exception):
    pass


root_folder = "my_project"  # корневая папка с проектом
templates_folder = os.path.join(root_folder, "templates")  # папка с шаблонами
try:
    os.mkdir(templates_folder) if not os.path.exists(templates_folder) else None  # создать папку с шаблонами, если её нет
    for root, dirs, files in os.walk(root_folder):
        if root.count(templates_folder) == 0 and root.count("templates") > 0 and os.path.split(root)[1] != "templates":  # оставим только нужные папки с файлами
            # print(root, dirs, files)

            dst_folder = os.path.join(templates_folder, os.path.split(root.split("templates")[-1])[-1])  # папка, в которую нужно перенести файлы
            if not os.path.exists(dst_folder):  # если нет нужной папки в шаблонах, то создать
                os.mkdir(dst_folder)

            for file in files:  # пройтись по всем файлам в папке
                src_file = os.path.join(root, file)  # фай, который нужно скопировать
                dst_file = os.path.join(dst_folder, file)  # фай, куда нужно скопировать
                try:
                    if not os.path.exists(dst_file):  # скопировать файл, если его нет в целевой папке
                        shutil.copy(src_file, dst_folder)
                    else:
                        raise FileExist
                except FileExist:
                    if input(f"Файл: {dst_file} существует. Перезаписать? (y/n) ") == "y":
                        shutil.copy(src_file, dst_folder)
except FileNotFoundError as e:
    print(f"Не найден файл или папка: {e.filename}")
    exit(1)
