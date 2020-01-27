q_list = 'Введите элементы произвольного списка через пробельный символ.\n'
users_list = list(input(q_list).split(' '))
print(f'исходный: {users_list}')
for itm in range(0,len(users_list),2):
    elem = users_list.pop(itm)
    users_list.insert(itm+1, elem)
print(f'Полученный: {users_list}')