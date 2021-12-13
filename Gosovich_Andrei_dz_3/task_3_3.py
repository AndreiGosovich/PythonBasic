
__author__ = "Госович Андрей Михайлович"

# 3.	Написать функцию thesaurus(), принимающую в
# качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*args):
    """
    Группировка имён по первой букве

    :param: *args: tuple of names
    :return: dict
    """
    dict_of_names = dict()

    for name_local in args:
        names_local = []
        if dict_of_names.get(name_local[0]):
            names_local = dict_of_names.get(name_local[0])
            names_local.append(name_local)
            dict_of_names[name_local[0]] = names_local
        else:
            names_local.append(name_local)
            dict_of_names.setdefault(name_local[0], names_local)
    return dict_of_names


def print_like_example(input_dict):
    """ Вывод словаря как в примере """
    for i, key in enumerate(input_dict):
        if i == 0:
            print("{")
        names = ""
        for name in input_dict[key]:
            names += f'"{name}"'
            names += ", " if name != input_dict[key][-1] else ""
        print(f'{"":<4}"{key:}": [{names}],')

        if i == len(input_dict) - 1:
            print("}")


def sort_dict(input_dict, reverse=False):
    """
    Сортировка словаря

    :param input_dict: dict which is need to sort
    :param reverse: True, if need to revers. Default False
    :return: sorted dict
    """
    list_of_keys = sorted(input_dict.keys(), reverse=reverse)
    new_dic = {}
    for key in list_of_keys:
        new_dic.setdefault(key, input_dict[key])
    return new_dic


dictionary = thesaurus("Иван", "Андрей",  "Мария", "Петр", "Илья", "Артём")
print(dictionary)
print_like_example(dictionary)
dictionary = sort_dict(dictionary, True)
print_like_example(dictionary)
