'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from sys import argv
from itertools import count, cycle

#Функция бесконечный итератора, генерирующего целые числа, начиная с указанного
def temp(x):
    for itm in count(x):
        print(itm)
#Бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
def temp_2(x):
    # заранее заданный список
    my_list = [1, 2, 3]
    for itm in cycle(my_list):
        print(itm)

args = argv

funcs = {
    'one': temp,
    'two': temp_2,
}

func = funcs[args[1]]
x = args[2]
print(func(int(x)))