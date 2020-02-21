'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузкуметодов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''
import math
class My_complex:
    def __init__(self, my_complex):
        self.my_complex = my_complex
    def __add__(self, other):
        res = complex(self.my_complex)+complex(other)
        return res
    def __mul__(self, other):
        res = complex(self.my_complex)*complex(other)
        return res

my_comp = complex(5, -6)
other = complex(5, 3)
print(f'Результат сложения комплексных чисел: {my_comp+other}')
print(f'Результат умножения комплексных чисел: {my_comp*other}')