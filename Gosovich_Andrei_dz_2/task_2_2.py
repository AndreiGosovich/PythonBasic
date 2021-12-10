
__author__ = 'Госович Андрей Михайлович'

# 2.	Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
output_string = ""

# print(original_list, id(original_list))

for value_of_list in original_list:
    if value_of_list.isdigit():
        new_list.append('"')
        new_list.append(f"{int(value_of_list):02d}")
        new_list.append('"')
    elif value_of_list[0] in ("+", "-") and value_of_list[1:].isdigit():
        new_list.append('"')
        new_list.append(f"{value_of_list[0]}{int(value_of_list[1:]):02d}")
        new_list.append('"')
    else:
        new_list.append(value_of_list)

# print(new_list, id(new_list))
# склеить значения, учитывая, что после открывающихся и перед закрывающимися пробел не ставится.
is_space = True
for value_of_list in new_list:
    output_string += value_of_list
    if is_space and value_of_list != '"':
        output_string += " "
    elif is_space and value_of_list == '"':
        is_space = False
    elif not is_space and value_of_list == '"':
        output_string += " "
        is_space = True

print(output_string.capitalize())
