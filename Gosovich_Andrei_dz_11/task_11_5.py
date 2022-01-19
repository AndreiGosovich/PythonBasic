
__author__ = "Госович Андрей Михайлович"

# 5.	Продолжить работу над предыдущим заданием.
# Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

from task_11_4 import *


class Warehouse(Warehouse):
    def __str__(self):
        return f"{self.name}, {self.address}"

    def add_equipment(self, equipment):  # поместить оборудование на склад
        """
        Добавить оборудование на склад
        :param equipment:
        :return:
        """
        self.equipment[equipment.serial_number] = equipment  # добавить оборудование на склад
        equipment.warehouse = self  # прописать склад в оборудовании
        equipment.organization = ""  # очистить организацию

    def remove_equipment(self, equipment):
        """
        Убрать оборудование со склада
        :param equipment: Объект оборудования
        :return:
        """
        self.equipment.pop(equipment.serial_number)


class Equipment(Equipment):
    def set_to_warehouse(self, wh: Warehouse):
        """
        Поместить оборудование на склад
        :param wh: объект Склад
        :return:
        """
        wh.add_equipment(self)  # добавить оборудование на склад
        self.warehouse = wh  # прописать склад в оборудовании
        self.organization = ""  # очистить организацию

    def issue_equipment(self, org_name):
        """
        Выдача оборудования организации
        :param org_name: Название подразделения
        :return:
        """
        self.organization = org_name  # прописать название организации в оборудовании
        self.warehouse.remove_equipment(self)  # убрать оборудования со склада
        self.warehouse = None  # отвязать склад от оборудования


class Printer(Equipment, Printer):
    pass


class Scanner(Equipment, Scanner):
    pass


class Copier(Equipment, Copier):
    pass


if __name__ == "__main__":
    warehouse = Warehouse("Основной склад", "Проектируемый проезд д1")
    p1 = Printer("HP", "Цветной", 345)
    s1 = Scanner("Canon 5", "Протяжный", 920)
    s1.set_to_warehouse(warehouse)
    warehouse.add_equipment(p1)
    print(p1)
    print(warehouse.equipment[345].equipment_type)
    print(len(warehouse.equipment))
    print(*warehouse.equipment.values())

    p1.issue_equipment("Отдел по работе с персоналом")
    print(p1.organization, p1.warehouse)
    print(len(warehouse.equipment))

    print(*warehouse.equipment.values())
