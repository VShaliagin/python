'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:
    classname = "Date"
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def get_print(self):
        print(f'{int(self.day)} {int(self.month)} {int(self.year)}')
    @classmethod
    def day_to_int(cls, date):
        day, month, year = map(int, date.split('-'))

        return (day, month, year)
    @staticmethod
    def valid(date_int):
        day, month, year = Date.day_to_int(date_int)
        if 2099 >= year <= 2000 or 12 > month < 1 or 1 > day > 31:
            return print('Не верная дата')
        elif month in (4, 6, 9, 11) and day > 30:
            return print(f'Количество дней в {month} месяце равно 30.')
        elif month == 2 and day > 29:
            return print(f'Количество дней в {month} месяце не больше 29.')
        else:
            return print(f'Дата {day}-{month}-{year} удовлетворяет условию')

print(Date.day_to_int('15-12-2019'))
print(Date.day_to_int('11-09-2012'))

Date.valid('34-10-2015')
Date.valid('31-04-3019')
Date.valid('23-11-2019')
Date.valid('30-02-2013')


