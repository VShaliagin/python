'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def my_division(divident=1, divider=1) -> float:
    '''
    Функция деления двух чисел
    :param iner: int
    :return: float
    '''
    division = 0
    while True:
        divident = input('Укажите делимое: \n')
        divider = input('Укажите делитель: \n')
        try:
            #Пробуем преобразовать к числу с плавающей точкой
            divident = float(divident)
            divider = float(divider)
            #Делитель не может равняться 0
            if divider == 0.0:
                print(f'Ошибка при вводе: на ноль делить нельзя')
                continue
        except ValueError as e:
            print(f'Ошибка при вводе: введено не число')
            continue
            break
        break
    return divident / divider
result = None

result = my_division()
print(result)