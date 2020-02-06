'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

import os.path as path

from functools import reduce

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
#Определяем путь к меесту запуска программы
base_path = path.join(path.dirname(__file__))
#Создаем текстовый файл в папке с программой или очищаем существующий.
open(path.join(path.dirname(__file__), 'task_4_2.txt'), 'w', encoding='UTF-8')

# Открываем исходные файл в режиме чтения
with open(path.join(path.dirname(__file__), 'task_4_1.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
        line_list = line.split(' ')
        #jnrhsdftv новый файл в режиме дозаписи
        with open(path.join(path.dirname(__file__), 'task_4_2.txt'), 'a', encoding='UTF-8') as file_new:
            for key in my_dict:
                if str(key) == line_list[0]:
                    file_new.write(f'{str(my_dict.get(key))} {" ".join(map(str, line_list[1:]))}')


