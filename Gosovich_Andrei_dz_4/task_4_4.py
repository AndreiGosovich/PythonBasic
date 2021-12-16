
__author__ = "Госович Андрей Михайлович"

# 4.	Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import utils

response = utils.currency_rates("gbp")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
response = utils.currency_rates("AUD")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
response = utils.currency_rates("rub")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
