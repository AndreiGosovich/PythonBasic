
__author__ = "Госович Андрей Михайлович"

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


if __name__ == "__main__":
    response = currency_rates("eur")
    print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
    response = currency_rates("USD")
    print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
    response = currency_rates("piastre")
    print(f"{response[0].strftime('%d.%m.%Y')}: {response[1]} руб.")
