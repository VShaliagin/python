print('#' * 20 + ' Ex_6 ' + '#' * 20)
q_dist_first_day = 'Введите расстояние, преодоленное спортсменом в первый день.\n'
dist_per_day = int(input(q_dist_first_day))
q_necessary_dist = 'Введите значение желаемой преодолеваемой дистанции.\n'
necessary_dist = int(input(q_necessary_dist))
number_day = 1
while dist_per_day < necessary_dist:
    dist_per_day = dist_per_day * 1.1
    number_day += 1
print(f' На {number_day}-й день спортсмен достиг результата — не менее { necessary_dist } км.')
