
__author__ = "Госович Андрей Михайлович"

# 5.	*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys

import utils

response = utils.currency_rates(sys.argv[1])
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")

