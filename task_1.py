print('#' * 20 + ' Ex_1 ' + '#' * 20)
my_name = 'Valerii'
my_surname = 'Shaliagin'
attempt = 1
q_name = 'Введите ваше имя.\n'
user_name = input(q_name)
q_surname = 'Введите вашу фамилию.\n'
user_surname = input(q_surname)
print(f'Добро пожаловать, {user_surname} {user_name}. Это первая задача на курсе "Основы языка Python"\nМеня зовут: {my_surname} {my_name}')
print(f'А теперь попробуем произвести простейшие математические операции для двух введенных чисел"')

q_number_1 = 'Введите первое целое число.\n'
number_1 = int(input(q_number_1))
q_number_2 = 'Введите второе целое число.\n'
number_2 = int(input(q_number_2))
q_operation = 'Введите желаемую операцию, которую Вы хотите произвести с числами (+ - / *).\n'
operation = input(q_operation)

while attempt > 0:
    if operation == '+':
        result = number_1 + number_2
        print(f'Результат: {number_1} + {number_2} = {result}')
        attempt -=1
    elif operation == '-':
        result = number_1 - number_2
        print(f'Результат: {number_1} - {number_2} = {result}')
        attempt -= 1
    elif operation == '*':
        result = number_1 * number_2
        print(f'Результат: {number_1} * {number_2} = {result}')
        attempt -= 1
    elif operation == '/':
        result = number_1 / number_2
        print(f'Результат: {number_1} / {number_2} = {result}')
        attempt -= 1
    else:
        print('Был введен некорректный оператор. Попробуйте еще раз.')
        q_operation = 'Введите желаемую операцию, которую Вы хотите произвести с числами (+ - / *).\n'
        operation = input(q_operation)

print(f'Спасибо Вам, {user_name}, за использование данной программы')