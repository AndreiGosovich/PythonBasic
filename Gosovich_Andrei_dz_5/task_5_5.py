
__author__ = "Госович Андрей Михайлович"

# 5.	Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

from time import perf_counter
import random

src = [random.randint(1, 10000) for _ in range(10000)]
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# первый вариант
time_start = perf_counter()

result = [el for el in src if src.count(el) == 1]

print(result[:100])
print(f"{(perf_counter() - time_start):f}")

# второй вариант
time_start = perf_counter()
tmp = set()
result1 = set()
for el in src:
    if el not in tmp:
        if el in result1:
            tmp.add(el)
            result1.discard(el)
        else:
            result1.add(el)
result1 = [number for number in src if number in result1]
print(result1[:100])
print(f"{(perf_counter() - time_start):f}")
