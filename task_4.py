'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
from random import choice

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return(f'Автомобиль {self.name} {self.color} поехал со скоростью {self.speed} км/ч.')
    def stop(self):
        return(f'Автомобиль {self.name} {self.color} остановился.')
    def turn(self):
        turn = choice(['поехал налево', 'поехал направо', 'развернулся'])
        return(f'Автомобиль {self.name} {self.color} цвета {turn}.')
    def show_speed(self):
        return(f'Скорость {self.name} составляет {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            return (f'Автомобиль {self.name} превышает разрешенный скоростной режим ({speed_limit} км/ч).')
        else:
            return (f'Скорость {self.name} составляет {self.speed}. В пределах разрешенных значения для класса авто ({speed_limit} км/ч).')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')
        speed_limit = 40
        if self.speed > speed_limit:
            return (f'Автомобиль {self.name} превышает разрешенный скоростной режим ({speed_limit} км/ч).')
        else:
            return (f'Скорость {self.name} составляет {self.speed}. В пределах разрешенных значения для класса авто ({speed_limit} км/ч).')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

# Создание экземпляры классов
hyundai = WorkCar(50, 'красный', 'Hyundai Solaris', False)
toyota = WorkCar(40, 'белый', 'Toyota Camry', False)
honda = TownCar(60, 'серый', 'Honda Fit', False)
audi = TownCar(65, 'черный', 'Audi A4', False)
skoda = PoliceCar(100, 'белый', 'Skoda Octavia')
ford_police = PoliceCar(90, 'белый', 'Ford Focus')
ford = SportCar(100, 'желтый', 'Ford Mustang', False)

print(audi.go())
print(toyota.stop())
print(honda.turn())
print(toyota.turn())
print(honda.show_speed())
print(audi.show_speed())
print(hyundai.show_speed())
print(toyota.show_speed())
print(ford_police.show_speed())
print(f'{hyundai.name} полицейский автомобиль? {hyundai.is_police}')
print(f'{ford_police.name} полицейский автомобиль? {ford_police.is_police}')
