
__author__ = "Госович Андрей Михайлович"

# 4.	Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

from time import perf_counter
import random

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

src = [random.randint(1, 10000) for _ in range(10000)]

# вариант с перебором элементов
time_start = perf_counter()
result = []
for i, el in enumerate(src[1:]):
    if el > src[i]:
        result.append(el)


print(result[:1000])
print(f"{(perf_counter() - time_start):f}")

# вариант с генераторами
time_start = perf_counter()


def gen1(src):
    gen = (el for el in src[:-1])
    for el1 in src[1:]:
        if el1 > next(gen):
            yield el1


result1 = gen1(src)

print(list(result1)[:1000])
print(f"{(perf_counter() - time_start):f}")

# вариант с list comprehensions
time_start = perf_counter()

result1 = [el for i, el in enumerate(src[1:]) if el > src[i]]

print(result1[:1000])
print(f"{(perf_counter() - time_start):f}")
