print('#' * 20 + ' Ex_4 ' + '#' * 20)
q_number = 'Введите целое положительное число.\n'
user_number = int(input(q_number))
user_max_number = 0
var_number = user_number # для сохранения пользовательского значения при выводе максимальной цифры
while True:
    if var_number > 10:
        if var_number % 10 > user_max_number:
            user_max_number = var_number % 10
            var_number = var_number // 10
        else:
            var_number = var_number // 10
    else:
        if var_number > user_max_number:
            user_max_number = var_number % 10
        break
print(f'Максимальная цифра в веденном числе {user_number } равняется: {user_max_number}')