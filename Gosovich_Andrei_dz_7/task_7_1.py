
__author__ = "Госович Андрей Михайлович"

# 1.	Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации,
# когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно
# было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

FILE_STRUCTURE = """my_project_1
>settings
>mainapp
>>eyt_path
>adminapp
>authapp
"""


def get_folders_from_string(string_files=FILE_STRUCTURE):
    """
    Парсинг строки определённого формата и возврат списка папок.
    :param string_files: строка в формате:
                                        папка первого уровня
                                        >второй уровень
                                        >>третий
    :return: список строк в формате ['папка первого уровня', 'папка первого уровня/второй уровень', 'папка первого уровня/второй уровень/третий'']
    """
    folders = []
    cur_f = []
    for folder in string_files.splitlines():
        cur_f.clear()
        if folder.count(">") == 0:
            cur_f.append(folder)
        else:
            # cur_f = "/".join(["/".join(folders[-1].split("/")[0:folder.count(">")]), folder.replace(">", "")])  # не кросплатформенно...
            cur_f = [folders[-1][i] for i in range(folder.count(">"))]
            cur_f.append(folder.replace(">", ""))
        folders.append(cur_f[:])
    return [os.path.join(*folder) for folder in folders]


if __name__ == "__main__":
    folder_list = get_folders_from_string(FILE_STRUCTURE)
    print(folder_list)
    for f in folder_list:
        print(f)
        os.makedirs(f, exist_ok=True)
