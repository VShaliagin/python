def my_list_user(**kwargs) -> float:
    '''
    Функция вывода данных о пользователе в строку
    :param iner: str
    :return: list
    '''
    result = ''
    for value in kwargs.values():
        result += f'{value} '
    return result

    # result = None
    # result = f'{name} {surname} {bith_year} {city} {email} {num_tel}'
    # return result
#Запрашиваем данные от пользователя
name = input('Укажите имя пользователя: \n')
surname = input('Укажите фамилию пользователя: \n')
city = input('Укажите город проживания пользователя: \n')
bith_year = input(f'Укажите год рождения пользователя:\n')
email = input(f'Укажите email пользователя:\n')
num_tel = input(f'Укажите номер телефона пользователя:\n')

user_id = {
    'user_name': name,
    'user_surname': surname,
    'user_city': city,
    'user_bith_year': bith_year,
    'user_email': email,
    'user_num_tel': num_tel,
}
print(my_list_user(**user_id))


