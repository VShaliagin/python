'''Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла:
firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import os.path as path
import json
base_path = path.join(path.dirname(__file__), 'task_7.json')

# with open(base_path, 'r', encoding='UTF-8') as file:
#     templates = file.read()
#
# new_data = json.loads(templates)
# print(new_data)
#
# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))

my_dict={ }
avg_cash = 0
i=0


with open(base_path, 'r', encoding='UTF-8') as file:
    for line in file:
        line_elem = line.split(' ')
        if int(line_elem[2]) - int(line_elem[3])>0:
            profit =int(line_elem[2]) - int(line_elem[3])
            i += 1
            print(profit)
    print(profit/i)

#
