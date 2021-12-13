
__author__ = "Госович Андрей Михайлович"

# 2.	*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной
# буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# 1.	Написать функцию num_translate(),
# переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate_adv(text_to_translate):
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

    translated_string = None
    if dictionary.get(text_to_translate.lower()):  # привести всю строку в нижний регистр и проверить, есть ли перевод
        translated_string = dictionary.get(text_to_translate.lower())
        if text_to_translate[0].isupper():  # если первая буква в верхнем регистре, то увеличить её и в переводе
            translated_string = translated_string.capitalize()

    return translated_string


print(num_translate_adv(input("Введите цифру на английском: ")))
