
__author__ = "Госович Андрей Михайлович"

# 2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def cloth(self):
        pass


class Clothes(AbstractClothes):
    total_cloth = 0

    def __init__(self, name):
        self.name = name

    @property
    def cloth(self):
        return Clothes.total_cloth


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.__v = v
        Clothes.total_cloth += self.cloth  # при создании добавить необходимую ткань в общие потребности

    @property
    def v(self):
        return self.v

    @v.setter
    def v(self, v):
        # при изменении размера, пересчитать вклад в общие потребности по ткани
        Clothes.total_cloth -= self.cloth  # убрать значение предыдущего размера
        self.__v = v  # изменить размер
        Clothes.total_cloth += self.cloth  # пересчитать общий объём ткани по новому размеру

    def __str__(self):
        return f"{self.name}, размер {self.__v}"

    @property
    def cloth(self):
        return self.__v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.__h = h
        Clothes.total_cloth += self.cloth  # при создании добавить необходимую ткань в общие потребности

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        # при изменении размера, пересчитать вклад в общие потребности по ткани
        Clothes.total_cloth -= self.cloth  # убрать значение предыдущего размера
        self.__h = h  # изменить размер
        Clothes.total_cloth += self.cloth  # пересчитать общий объём ткани по новому размеру

    def __str__(self):
        return f"{self.name}, размер {self.__h}"

    @property
    def cloth(self):
        return self.__h * 2 + 0.3


clothes = Clothes("Main")
coat = Coat("Пальто", 40)
coat_2 = Coat("Пальто_2", 38)
suit = Suit("Костюм", 38)
print(f"{coat}, необходимо ткани: {coat.cloth}")
print(f"{coat_2}, необходимо ткани: {coat_2.cloth}")
print(f"{suit}, необходимо ткани: {suit.cloth}")
print(f"Всего необходимо ткани: {clothes.cloth}")
coat.v = 100
print(f"{coat}, необходимо ткани: {coat.cloth}")
print(f"Всего необходимо ткани: {clothes.cloth}")
