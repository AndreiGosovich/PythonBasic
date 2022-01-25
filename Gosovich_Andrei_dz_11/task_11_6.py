
__author__ = "Госович Андрей Михайлович"

# 6.	Продолжить работу над предыдущим заданием.
# Реализовать механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

# т.к. реализация не предусматривает указание количества при отправке на склад и при выдаче ввиду того, что каждое
# оборудование уникально и имеет свой серийный номер, то вместо проверки количества, будем считать что серийный номер
# должен быть числом и выполнять данную проверку.

from task_11_5 import *


class Equipment(Equipment):
    def __init__(self, name, serial_number):
        Equipment.chek_data(serial_number)
        super().__init__(self, name, serial_number)

    @staticmethod
    def chek_data(serial_number):
        """
        Проверка ввода в качестве серийного номера только числа
        :param serial_number:
        :return:
        """
        if not isinstance(serial_number, int):
            raise ValueError("В качестве серийного номера допустимо использовать только числа!")
        return True


class Printer(Equipment, Printer):
    pass


class Scanner(Equipment, Scanner):
    pass


class Copier(Equipment, Copier):
    pass


p1 = Printer("Canon 304", 209)
print(p1.serial_number)
s2 = Scanner("Epson", "45")
print(s2.serial_number)
