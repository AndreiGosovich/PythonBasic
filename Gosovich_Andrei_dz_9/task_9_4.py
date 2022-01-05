
__author__ = "Госович Андрей Михайлович"

# 4.	Реализуйте базовый класс Car:
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, 
# что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
# выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print("Машина в пути")
        
    def stop(self):
        print("Машина стоит")
        
    def turn(self, direction):
        print(f"Машина повернула на {direction}")
    
    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed > 60:
            print(f"Превышение скорости!")


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(SportCar, self).__init__(speed, color, name)


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed > 40:
            print(f"Превышение скорости!")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


sport_car = SportCar(60, "red", "BMW")
sport_car.show_speed()

work_car = WorkCar(60, "red", "BMW")
work_car.show_speed()
print(work_car.is_police)

police_car = PoliceCar(120, "White", "VAZ")
police_car.turn("лево")
print(police_car.is_police)

town_car = TownCar(60, "Green", "Nissan")
town_car.go()
town_car.turn("Право")
town_car.show_speed()
town_car.stop()
