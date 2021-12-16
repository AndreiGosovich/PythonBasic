
__author__ = "Госович Андрей Михайлович"

# 3.	*(вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

# 2.	Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import decimal
from datetime import datetime as dt

from requests import get

URL = "http://www.cbr.ru/scripts/XML_daily.asp"


def currency_rates(currency_code):
    resource_from_site = get(URL)
    content = resource_from_site.content.decode(encoding=resource_from_site.encoding)
    date_of_currency = content[content.index('Date="') + len('Date="'): content.index('" name')]
    for el in content.split("</NumCode>")[1:]:
        currency = el.split("</Valute>")[0]
        char_code = currency[currency.index("<CharCode>") + len("<CharCode>"):currency.index("</CharCode>")]
        nominal = currency[currency.index("<Nominal>") + len("<Nominal>"):currency.index("</Nominal>")]
        value = currency[currency.index("<Value>") + len("<Value>"):currency.index("</Value>")]
        if char_code == currency_code.upper():
            return [dt.strptime(date_of_currency, "%d.%m.%Y"), decimal.Decimal(value.replace(",", ".")) / int(nominal)]
    return [dt.strptime(date_of_currency, "%d.%m.%Y"), None]


response = currency_rates("eur")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
response = currency_rates("USD")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
response = currency_rates("piastre")
print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
