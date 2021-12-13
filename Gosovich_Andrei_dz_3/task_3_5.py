from random import choice

__author__ = "Госович Андрей Михайлович"

# 5.	Реализовать функцию get_jokes(), возвращающую n шуток
# , сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?


def get_jokes(n, repeats=True):
    """
    Joke generator.
    Generate given count of jokes from three words.
    :param n: count of jokes.
    :param repeats: can be words repeat.
    :return: list of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(0, n):
        if repeats:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        else:
            jokes.append(f"{nouns.pop(nouns.index(choice(nouns))) if len(nouns) > 0 else 'извините,'} "
                         f"{adverbs.pop(adverbs.index(choice(adverbs))) if len(adverbs) > 0 else 'шутки'} "
                         f"{adjectives.pop(adjectives.index(choice(adjectives))) if len(adjectives) > 0 else 'закончились'}")

    return jokes


print(get_jokes(7, repeats=False))
