'''

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.

'''
#объявил класс склад
class Warehouse:
    def __init__(self, name_office):
        self.name_office = name_office
        self.__box = []
    @property
    def box(self):
        return tuple(self.__box)
    @box.setter
    def box(self, other):

        self.__box.append(other)

    def add_warehouse(self, equipment):
        self.__box .append(equipment)
    def transfer_to(self, equipment):
        if not equipment in self.__box:
            raise KeyError(equipment)
        self.__box.remove(equipment)
    def move_to(self, equipment, other):
        self.transfer_to(equipment)
        other.add_warehouse(equipment)

    # Для обращения к списку по индексу
    def __getitem__(self, item):
        return self.__box[item]
    #Для прохода по циклу for
    def __iter__(self):
        if len(self.__box) == 0:
            print (f'Список пуст')
        return self.__box.__iter__()

#класс оргтехника
class Office_equipment:
    def __init__(self, brand, color, coast, quantity):
        self.brand = brand
        self.color = color
        self.coast = coast
        self.quantity = quantity
    def __str__(self):
        return f'Модель {self.brand} цвет {self.color} стоимость {self.coast} количество {self.quantity}'

class Printer(Office_equipment):
    def __init__(self, brand, color, coast, quantity, type_print, max_size_paper):
        super().__init__(brand, color, coast, quantity)
        self.type_print = type_print
        self.max_size_paper = max_size_paper


class Scanners(Office_equipment):
    def __init__(self, brand, color, coast, quantity, max_size_scan, scanner_resolution):
        super().__init__(brand, color, coast, quantity)
        self.max_size_scan = max_size_scan
        self.scanner_resolution = scanner_resolution

class Xerox(Office_equipment):
    def __init__(self, brand, color, coast, quantity, max_size_xerox, xerox_resolution):
        super().__init__(brand, color, coast, quantity)
        self.max_size_xerox = max_size_xerox
        self.xerox_resolution = xerox_resolution

print_hp = Printer('HP', 'grey', 4500, 12, 'laser', 'a4')
print_canon = Printer('Canon', 'white', 6500, 5, 'matrix', 'a5')

scan_epson = Scanners('Epson', 'black', 4690, 5, 'A4', '400 DPI')
scan_plustek = Scanners('Plustek', 'black', 170390, 1, 'A3', '600 DPI')

xerox_1 = Xerox('Xerox', 'white', 9600, 2, 'А4', '1200 DPI')
xerox_2 = Xerox('HP', 'white', 300000, 1, 'А3', '600 DPI')

warehouse_1 = Warehouse('склад')
warehouse_2 = Warehouse('офис')

# Добавить элементы

warehouse_1.box = print_hp
warehouse_1.box = print_canon
warehouse_1.box = scan_plustek
warehouse_1.box = xerox_2
print(f'Склад содержит следующие позиции:')
for el in warehouse_1:
    print(el)
print(f'\nВ офисе находятся:')
for el in warehouse_2:
    print(el)
# Передадим в офис print_hp. Проверим на отсутствие элемента на складе и присутствие в офисе
warehouse_1.move_to(print_hp, warehouse_2)
print(f'\nПосле передачи на складе')
for el in warehouse_1:
    print(el)
print(f'\nВ офисе')
for el in warehouse_2:
    print(el)