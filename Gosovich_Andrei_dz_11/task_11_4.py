
__author__ = "Госович Андрей Михайлович"

# 4.	Начать работу над проектом «Склад оргтехники».
# Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    """
    Класс объекта Склад
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.equipment = {}


class Equipment:
    """
    Общий класс для всего оборудования
    """
    counter = 0  # счётчик количества имеющегося оборудования для создания уникального инфентарного номера

    def __init__(self, name, serial_number):
        self.__name = name  # название оборудования
        self.__equipment_type = None  # тип оборудования
        self.__serial_number = serial_number  # серийный номер
        self.warehouse = None  # Warehouse  # склад расположения
        self.organization = None  # подразделение - владелец
        Equipment.counter += 1  # увеличить счётчик количество, при создании нового экземпляра
        self.__inventory_number = Equipment.counter  # инвентарный номер.

    @property
    def serial_number(self):  # запрос серийного номера
        return self.__serial_number

    @property
    def inventory_number(self):  # запрос инвентарного номера
        return self.__inventory_number

    @property
    def name(self):  # запрос названия оборудования
        return self.__name


class Printer(Equipment):
    """
    Класс для типа оборудования - Принтер
    """
    def __init__(self, name, color, serial_number):
        super().__init__(name, serial_number)
        self.__equipment_type = "Printer"  # тип оборудования. Не изменный.
        self.__color = color  # цветной/чб

    @property
    def equipment_type(self):  # запрос типа оборудования
        return self.__equipment_type

    @property
    def color(self):
        return self.__color

    def __str__(self):
        return f"{self.equipment_type} {self.name}, inv: {self.inventory_number}"


class Scanner(Equipment):
    """
    Класс для типа оборудования - Сканер
    """
    def __init__(self, name, scanner_type, serial_number):
        super().__init__(name, serial_number)
        self.__equipment_type = "Scanner"  # тип оборудования. Не изменный.
        self.__scanner_type = scanner_type  # ручной, планшетный, протяжной

    @property
    def equipment_type(self):  # запрос типа оборудования
        return self.__equipment_type

    @property
    def scanner_type(self):
        return self.__scanner_type

    def __str__(self):
        return f"{self.equipment_type} {self.name}, inv: {self.inventory_number}"


class Copier(Equipment):
    """
    Класс для типа оборудования - Ксерокс (копир)
    """
    def __init__(self, name, copy_size, serial_number):
        super().__init__(name, serial_number)
        self.__equipment_type = "Copier"  # тип оборудования. Не изменный.
        self.__copy_size = copy_size  # размер копируемой бумаги

    @property
    def equipment_type(self):  # запрос типа оборудования
        return self.__equipment_type

    @property
    def copy_size(self):
        return self.__copy_size

    def __str__(self):
        return f"{self.equipment_type} {self.name}, inv: {self.inventory_number}"


if __name__ == "__main__":
    p1 = Printer("HP 3340", "Цветной", 342)
    p2 = Printer("Conica 123", "ч/б", 443)
    s1 = Scanner("HP 150", "Планшетный", 305)
    c1 = Copier("Xerox 379", "A4 - A0", 693)
    print(p1)
    print(p2)
    print(s1)
    print(c1)
