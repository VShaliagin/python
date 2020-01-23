print('#' * 20 + ' Ex_2 ' + '#' * 20)
q_time = 'Введите время в секундах, для преобразования в формат чч:мм:сс. \n'
user_time = int(input(q_time))

sec_day = 86400 # Секунд в одном дне

if user_time > sec_day: #В случае если число введено больше чем секунд в сутках
    user_time = user_time % sec_day	
hour_time = user_time // 3600 # количество часов в значении, введенным пользователSем
if hour_time < 10:
    hour_time = f'0{hour_time}'
q_time = user_time % 3600 # переопределение пользовательского числа, отбросив количество часов
min_time = q_time // 60 # количество минут в значении, введенным пользователем
if min_time < 10:
    min_time =  f'0{min_time}'
sec_time = q_time % 60 # количество секунд в значении, введенным пользователем
if sec_time < 10:
    sec_time =  f'0{sec_time}'
print(f'Время в формате чч:мм:сс равняется: {hour_time}:{min_time}:{sec_time}')