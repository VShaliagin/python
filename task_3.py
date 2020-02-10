"""3. Создать текстовый файл (не программно), построчно записать фамеилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет среднй величины
дохода сотрудников."""

import os.path as path
from functools import reduce

#зарплаты всех сотрудников
salary = []
base_path = path.join(path.dirname(__file__), 'task_3.txt')
list_workers = []

with open(base_path, 'r', encoding='UTF-8') as file:
    for line in file:
        line_list = line.split(' ')
        # Вычисление общей зарплаты всех сотрудников
        if int(line_list[1]) < 20000:
            #Добавление в список фамилий сотрудников полчающих менее 20000 в месяц
            list_workers.append(line_list[0])
        #создание списка всех зарплат сотрудников
        salary.append(int(line_list[1]))
#Расчет средней зарплаты работников фирмы
#Примененив функцию reduce для расчета средней зарплаты
salary_avg = (reduce(lambda x, y: x + y, salary))/len(salary)

print(f'Список работников получающих зарплату менее 20000: {list_workers}')
print(f'Cредняя зарплата сотрудников составляет {salary_avg}')

