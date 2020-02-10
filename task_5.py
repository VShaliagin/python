'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import os.path as path
import random

summ_file = 0
# Определяем путь запуска файла
base_path = path.join(path.dirname(__file__), 'task_5.txt')
# После перезапуска программы очищаем файл с чмслами
open(base_path, 'w')
#Создаем генератор случайных чисел задан параметр генерации 10 чисел от 0 до 100
for i in range(0, 10):
    a = random.randint(1, 100)
    # расчет суммы сразу при генерации чисел
    #summ_file += a
    #Добавляем число в файл
    with open(base_path, 'a') as file:
        file.write(str(a) + ' ')
#Открываем файл на чтение и считываем числа
with open(base_path, 'r') as file:
    a = (file.read().split())
    print(f'Сгенерированный список: {a}')
    for i in range(0, len(a)):
        summ_file += int(a[i])
print(f'Сумма чисел списка равняется: {summ_file}')