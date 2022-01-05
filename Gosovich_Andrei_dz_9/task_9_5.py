
__author__ = "Госович Андрей Михайлович"

# 5.	Реализовать класс Stationery (канцелярская принадлежность):
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки класса Stationery")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки класса Pen")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки класса Pencil")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки класса Handle")


stationery = Stationery("Канцелфрия")
stationery.draw()
pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Марке")
handle.draw()
