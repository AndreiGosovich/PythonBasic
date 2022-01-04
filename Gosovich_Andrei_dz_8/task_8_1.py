
__author__ = "Госович Андрей Михайлович"

# 1.	Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь
# учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile(r"\b(?P<username>[\w,_,\d,\.]+)[@](?P<domain>[\w,_,\d,\.]+\.\w+)\b")


def email_parse(email_address):
    if re.match(RE_EMAIL, email_address):
        return dict(*map(lambda x: x.groupdict(), RE_EMAIL.finditer(email_address)))
    else:
        msg = f"wrong email: {email_address}"
        raise ValueError(msg)


print(email_parse("someone@geekbrains.ru"))
