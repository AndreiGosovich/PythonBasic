
__author__ = 'Госович Андрей Михайлович'

# 5.	Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# A.	Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# B.	Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# C.	Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D.	Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [34.6, 48.05, 120, 543.9, 50.00, 234.56, 1239, 543.28, 384, 956.26, 764.20, 934, 472.6, 23947]
# A.
result_string = ""
for number in price_list:
    number = float(number)
    # result_string += f"{number:.0f} руб {str(number).split('.')[-1] if len(str(number).split('.')[-1]) == 2 else str(number).split('.')[-1] + '0':s} коп"
    result_string += f"{number:.0f} руб {int((number - int(number)).__round__(2) * 100):02d} коп"
    result_string += ", " if price_list[-1] != number else ""

print(f"A. {result_string}")

# B.
print("B.")
print(f"id оригинального списка: {id(price_list)}")
price_list.sort()
print(f"id сортированного списка: {id(price_list)}")
print(price_list)

# C.
print("C.")
print(f"id оригинального списка: {id(price_list)}")
sorted_list = sorted(price_list, reverse=True)
print(f"id сортированного списка: {id(sorted_list)}")
print(sorted_list)

# D.
print("D.")
print(sorted_list[:5])
price_list.sort(reverse=True)
print(price_list[:5])
