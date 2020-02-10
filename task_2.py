'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

import os.path as path
base_path = path.join(path.dirname(__file__), 'task_2.txt')
n, i = 0, 0

with open(base_path, 'r', encoding='UTF-8') as file:
    for line in file:
        n += 1
    print(f'количество строк в документе: {n}')
with open(base_path, 'r', encoding='UTF-8') as file:
    for line in file:
        i += 1
        if line == '' or line == '\n':
            print(f'Количество слов в {i:>2} строке: 0')
        else:
            line_list = line.split(' ')
            print(f'Количество слов в {i:>2} строке: {len(line_list):<2}')