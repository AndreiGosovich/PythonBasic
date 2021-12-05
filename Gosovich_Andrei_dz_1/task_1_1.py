
__author__ = 'Госович Андрей Михайлович'

# Задача - 1.	Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration в секундах:
# a.	до минуты: <s> сек;
# b.	до часа: <m> мин <s> сек;
# c.	до суток: <h> час <m> мин <s> сек;
# d.	* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
#
# Примечание: можете проверить себя здесь, подумайте,
# можно ли использовать цикл для проверки работы кода
# сразу для нескольких значений продолжительности, будет ли тут полезен список?

durations = (99999, 4000, 1200, 53)  # список значений

# перебор значений списка
for pos, duration in enumerate(durations):
    result_string = ""
    days = duration // (60 * 60 * 24)  # расчёт дней
    hours = duration % (60 * 60 * 24) // (60 * 60)  # расчёт часов
    minutes = duration % (60 * 60) // 60  # расчёт минут
    seconds = duration % (60 * 60) % 60  # расчёт секунд

    # проверка на нули
    if days > 0:
        result_string = "{} дн ".format(str(days))
    if hours > 0:
        result_string = "{}{} час ".format(result_string, str(hours))
    if minutes > 0:
        result_string = "{}{} мин ".format(result_string, str(minutes))
    if seconds > 0:
        result_string = "{}{} сек".format(result_string, str(seconds))

    # вывод результата
    print("{}: {}".format(pos + 1, result_string))
