'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class My_exception():
    def __init__(self, chislo):
        self.chislo = chislo
    def __truediv__(self, other):
        try:
            int(self.chislo) / int(other.chislo)
        except ZeroDivisionError as e:
            print(e)
            print('На ноль делить нельзя!')
            other.chislo = 1
            return (int(self.chislo) / int(other.chislo))
        else:
            return (int(self.chislo) / int(other.chislo))

dividend = My_exception(12)
divider = My_exception(0)
print(dividend/divider)
My_exception(4)
print(My_exception(4)/My_exception(7))