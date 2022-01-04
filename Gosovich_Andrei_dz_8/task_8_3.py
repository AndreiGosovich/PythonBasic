__author__ = "Госович Андрей Михайлович"

# 3.	Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):
    @wraps(func)  # спрятать декоратор
    def wrapper(*args, **kwargs):
        print(str(func).split(" ")[1], end="(")
        if args:
            print(*(f"{arg}: {type(arg)}" for arg in args), sep=", ", end=", ")  # позиционные аргументы
        if kwargs:
            print(*(f"{arg}: {type(arg)}" for arg in kwargs.values()), sep=", ", end=", ")  # именованные аргументы
        result = func(*args, **kwargs)
        if result:
            print(f"Result: {result}: {type(result)})")  # результат
        return result

    return wrapper


@type_logger
def calc_cube(x, y, named_arg=0):
    return x ** 3


calc_cube(2, "Привет", named_arg=34.5)
