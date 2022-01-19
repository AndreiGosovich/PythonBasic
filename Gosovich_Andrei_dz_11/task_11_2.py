
__author__ = "Госович Андрей Михайлович"

# 2.	Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyDivisionByZeroException(ZeroDivisionError):
    pass


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise MyDivisionByZeroException
    print(str(a / b))
except MyDivisionByZeroException:
    print("Деление на ноль недопустимо!")
