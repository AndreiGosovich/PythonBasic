
__author__ = "Госович Андрей Михайлович"

# 7.	Реализовать проект «Операции с комплексными числами».
# Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.

import re

CHEK_STR = re.compile(r"(?P<first>\d+\.*\d*)(\s*\++\s*(?P<second>\d*\.*\d*i))*")


class ComplexNumber:
    def __init__(self, number):
        if CHEK_STR.match(number):
            self.__number = str(number)
            self.__a = CHEK_STR.match(str(number)).groupdict()["first"]
            self.__b = CHEK_STR.match(str(number)).groupdict()["second"] \
                if CHEK_STR.match(str(number)).groupdict()["second"] else "0j"

    def __str__(self):
        return f"{self.__a} + {self.__b}"

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number
        self.__a = CHEK_STR.match(str(number)).groupdict()["first"]
        self.__b = CHEK_STR.match(str(number)).groupdict()["second"] \
            if CHEK_STR.match(str(number)).groupdict()["second"] else "0j"

    def __add__(self, other):
        return ComplexNumber(f"{float(self.__a) + float(other.__a):,g} + "
                             f"{float(self.__b[:self.__b.index('i')]) + float(other.__b[:other.__b.index('i')]):,g}i")

    def __mul__(self, other):
        # (a + bi)(c + di) = (ac - bd) + (bc + ad)i
        ac = float(self.__a) * float(other.__a)
        bd = float(self.__b[:self.__b.index('i')]) * float(other.__b[:other.__b.index('i')])
        bc = float(self.__b[:self.__b.index('i')]) * float(other.__a)
        ad = float(self.__a) * float(other.__b[:other.__b.index('i')])
        return f"{ac - bd:,g} + {bc + ad:,g}i"


n = ComplexNumber("23 + 45i")
print(n)
n.number = "1+1i"
print(n)
n2 = ComplexNumber("5 + 1i")
print(n2)
print(f"({n}) + ({n2}) =", n + n2)
print(f"({n}) * ({n2}) =", n * n2)
