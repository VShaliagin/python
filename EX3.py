seasons = ('зима', 'весна', 'лето', 'осень')
seasons_dict = {'1':1, '2':1, '3':2, '4':2, '5':2, '6':3, '7':3, '8':3, '9':4, '10':4, '11':4, '12':1}
q_month = 'Введите порядковый номер месяца.\n'
users_month = input(q_month)
print(f'{seasons[seasons_dict.get(users_month)]}')