'''
 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
  и возвращает сумму наибольших двух аргументов.
'''
def my_func(var_1, var_2, var_3) -> float:
    '''
    Функция суммирования двух слогаемых. без минимального
    :param iner: int
    :return: float
    '''
    result = None
    #Расчет суммы всех элементов
    my_sum = var_1+var_2+var_3
    #Поиск минимального введенного пользователем значения
    my_list=var_1, var_2, var_3
    for itm in my_list:
        if not result:
            result = itm
            continue
        if itm < result:
            result = itm
    #Вычисление суммы двух наибольших элементов
    my_sum = my_sum - result
    return my_sum
#Проверка на ввод корректных данных
while True:
    var_1 = input('Укажите первое число: \n')
    var_2 = input('Укажите втоорое число: \n')
    var_3 = input('Укажите третье число: \n')
    try:
        # Пробуем преобразовать к числу с плавающей точкой
        var_1 = float(var_1)
        var_2 = float(var_2)
        var_3 = float(var_3)
    except ValueError as e:
        print(f'Ошибка при вводе: введено не число')
        continue
    break
my_summ_elem = my_func(var_1, var_2, var_3)

print(my_summ_elem)