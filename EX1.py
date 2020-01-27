user_list = [12, 'слово', 14.5, 5 -3j, True, None]

for idx, itm in enumerate(user_list, 1):
    print(f'{idx:>2}: {itm} - {type(itm)}')