
__author__ = "Госович Андрей Михайлович"

# 3.	Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и округление до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.


class OrganicCell:
    def __init__(self, cell_count: int):
        self.cell_count = int(cell_count)

    def __str__(self):
        return str(self.cell_count)

    def __add__(self, other):
        return OrganicCell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count - other.cell_count > 0:
            return OrganicCell(self.cell_count - other.cell_count)
        return "Ошибка выполнения операции."

    def __mul__(self, other):
        return OrganicCell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return OrganicCell(self.cell_count // other.cell_count)

    def make_order(self, cell_in_row: int):
        result = ""
        for i in range(1, self.cell_count + 1):
            result += "*"
            if i % cell_in_row == 0 and i < self.cell_count:
                result += "\n"
        return result


cell_1 = OrganicCell(12)
cell_2 = OrganicCell(7)

print("cell_1:", cell_1)
print("cell_2:", cell_2)
print("cell_1 + cell_2:", cell_1 + cell_2)
print("cell_1 - cell_2:", cell_1 - cell_2)
print("cell_2 - cell_1:", cell_2 - cell_1)
print("cell_1 * cell_2:", cell_1 * cell_2)
print("cell_1 / cell_2:", cell_1 / cell_2)
print("Cell_1:\n", cell_1.make_order(5), sep="")
print("cell_1 * cell_2:\n", (cell_1 * cell_2).make_order(15), sep="")
