
__author__ = 'Госович Андрей Михайлович'

# 1.	Выяснить тип результата выражений:
# ●	15 * 3
# ●	15 / 3
# ●	15 // 2
# ●	15 ** 2

math_expressions = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for expr in math_expressions:
    type_string = str(type(expr)).split()[1].replace(">", "").replace("'", "")
    print(f'Тип числа {expr}: {type_string}')

