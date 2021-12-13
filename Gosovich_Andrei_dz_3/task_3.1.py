
__author__ = "Госович Андрей Михайлович"

# 1.	Написать функцию num_translate(),
# переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(text_to_translate):
    """
    Translate numbers [0:10] from english to russian
    :text_to_translate: text to translate
    :return: string
    """

    dictionary = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    return dictionary.get(text_to_translate)


print(num_translate(input("Введите цифру на английском: ")))
