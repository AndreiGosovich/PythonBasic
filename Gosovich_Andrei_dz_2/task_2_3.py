
__author__ = 'Госович Андрей Михайлович'

# 3.	*(вместо задачи 2) Решить задачу 2 не создавая новый список
# (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.
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

# первый вариант
print("Первый вариант")
print("Оригинальная строка", chr(10), original_list, id(original_list))

for i, value_of_list in enumerate(original_list):
    if value_of_list.isdigit():
        original_list[i] = f'"{int(value_of_list):02d}"'
    elif value_of_list[0] in ("+", "-") and value_of_list[1:].isdigit():
        original_list[i] = f'"{value_of_list[0]}{int(value_of_list):02d}"'

print("Изменённая оригинальная строка", chr(10), original_list, id(original_list))
print("Результат", chr(10), " ".join(original_list).capitalize())

##################
# второй вариант #
##################
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
output_string = ""

# print(original_list, id(original_list))
i = 0
while i < len(original_list):
    if original_list[i].isdigit():
        original_list.insert(i, '"')
        i += 1
        original_list[i] = f"{int(original_list[i]):02d}"
        i += 1
        original_list.insert(i, '"')
    elif original_list[i][0] in ("+", "-") and original_list[i][1:].isdigit():
        original_list.insert(i, '"')
        i += 1
        original_list[i] = f"{original_list[i][0]}{int(original_list[i][1:]):02d}"
        i += 1
        original_list.insert(i, '"')
    i += 1

# склеить значения, учитывая, что после открывающихся и перед закрывающимися пробел не ставится.
is_space = True
for value_of_list in original_list:
    output_string += value_of_list
    if is_space and value_of_list != '"':
        output_string += " "
    elif is_space and value_of_list == '"':
        is_space = False
    elif not is_space and value_of_list == '"':
        output_string += " "
        is_space = True

print(chr(10), "Второй вариант", sep="")
print("Изменённая оригинальная строка", chr(10), original_list, id(original_list))
print("Результат", chr(10), output_string.capitalize())

# судя по id, решением является первый вариант.
