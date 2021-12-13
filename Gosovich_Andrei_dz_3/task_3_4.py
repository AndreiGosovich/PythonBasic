
__author__ = "Госович Андрей Михайлович"

# 4.	*(вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий
# , а значения — словари, реализованные по схеме предыдущего задания и содержащие записи
# , в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    """
    Группировка Имени Фамили сначала по первой букве Фимили, затем по первой букве имени

    :param: *args: tuple of names
    :return: dict
    """
    dict_of_persons = dict()
    persons_list = []
    for person in args:
        persons_list.clear()
        persons_list.append(person)
        if dict_of_persons.get(person.split(" ")[1][0]):
            if dict_of_persons.get(person.split(" ")[1][0]).get(person[0]):
                dict_of_persons.get(person.split(" ")[1][0]).get(person[0]).append(person)
            else:
                dict_of_persons.get(person.split(" ")[1][0]).setdefault(person[0], persons_list[:])
        else:
            dict_of_persons.setdefault(person.split(" ")[1][0], {person[0]: persons_list[:]})
    return dict_of_persons


def print_like_example_adv(input_dict):
    """ Вывод словаря как в примере """
    for i, key1 in enumerate(input_dict):
        if i == 0:
            print("{")

        print(f'{"":<4}"{key1}": {{')

        for j, key2 in enumerate(input_dict[key1]):
            print(f'{"":<8}"{key2}": [', end='')
            for person in input_dict[key1][key2]:
                print(person, end="")
                print(", ", end="") if person != input_dict[key1][key2][-1] else print("", end="")
            print("],") if j < len(input_dict[key1]) - 1 else print("]")

        print(f'{"":<4}}}, ')

        if i == len(input_dict) - 1:
            print("}")


def sort_dict_adv(input_dict, reverse=False):
    """
    Сортировка словаря

    :param input_dict: dict which is need to sort
    :param reverse: True, if need to revers. Default False
    :return: sorted dict
    """
    new_dic = {}
    sub_dic = {}
    for key in sorted(input_dict.keys(), reverse=reverse):
        sub_dic.clear()
        for sub_key in sorted(input_dict[key].keys(), reverse=reverse):
            sub_dic.setdefault(sub_key, input_dict.get(key).get(sub_key))
        new_dic[key] = sub_dic.copy()
    return new_dic


dictionary = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(dictionary)
print_like_example_adv(dictionary)
dictionary = sort_dict_adv(dictionary)
print_like_example_adv(dictionary)
