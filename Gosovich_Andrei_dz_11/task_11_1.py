
__author__ = "Госович Андрей Михайлович"

# 1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый — с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re


class Date:
    def __init__(self, str_date):
        if Date.chek_date(str_date):
            self.str_date = str_date
            self.year = Date.convert_to_int(str_date)["year"]
            self.day = Date.convert_to_int(str_date)["day"]
            self.month = Date.convert_to_int(str_date)["month"]

    @classmethod
    def convert_to_int(cls, str_date):
        day, month, year = str_date.split("-")
        return {"day": int(day), "month": int(month), "year": int(year)}

    @staticmethod
    def chek_date(str_date):
        re_date = re.compile(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{2}|\d{4})$')

        # общая проверка формата введённой строки
        if not re_date.match(str_date):
            raise ValueError("Введён неверный формать даты.\nДолжен быть «день-месяц-год»")
        # проверка месяца
        month = Date.convert_to_int(str_date)["month"]
        if month not in range(1, 13):
            raise ValueError("Неверное значение месяца. Должен быть в диапазон от 1 до 12")
        # проверка количество дней в месяце
        day = Date.convert_to_int(str_date)["day"]
        if month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32):
            raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 31")
        if month in [4, 6, 9, 11] and day not in range(1, 31):
            raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 30")
        # проверка на високосный год
        if month == 2:
            year = Date.convert_to_int(str_date)["year"]
            if year % 4 == 0:
                if year % 100 != 0:  # год високосный
                    if day not in range(1, 30):
                        raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 29")
                else:
                    if year % 400 != 0:  # год не високосный
                        if day not in range(1, 29):
                            raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 28")
                    elif day not in range(1, 30):  # год високосный
                        raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 29")
            elif day not in range(1, 29):  # год не високосный
                raise ValueError("Неверное количество дней. В указанном месяце должно быть в диапазоне от 1 до 28")
        return True


date = Date("29-02-1844")
print(date.day, date.month, date.year)
