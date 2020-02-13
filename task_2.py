'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def res(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V
    @property
    def res(self):
        Coat_material = 2 * self.V + 0.3
        print(f'Потребуется материала на одно пальто: {Coat_material: <3}')
        return(Coat_material)

class Costume(Clothes):
    def __init__(self, H):
        self.H = H
    @property
    def res(self):
        Costume_material =2*self.H + 0.3
        print(f'Потребуется материала на один костюм {Costume_material: <3}')
        return(Costume_material)

coat = Coat(10)
costume = Costume(1.78)
total_material = coat.res + costume.res
print(f'Всего потребуется материала: {total_material: < 2}')