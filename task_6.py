'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран. Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import os.path as path

my_dict={ }

base_path = path.join(path.dirname(__file__), 'task_6.txt')

with open(base_path, 'r', encoding='UTF-8') as file:
    for line in file:
        my_summ = 0
        #разделяем строку по : название предмета и часы
        line_list = line.split(':')
        #разделяем часы по видам деятельности в отдельный список по пробельному символу
        line_list_2 = line_list[1].split(' ')
        lesson_hour = []
        for i in range(1, 4):
            hour_type = ''.join(filter(lambda x: x.isdigit(), line_list_2[i]))
            lesson_hour.append(hour_type)
        # Проверям являются ли элементы списка числом и расчитываем общую продолжительность курса
        for i in range(0, 3):
            if lesson_hour[i].isdigit():
                my_summ += int(lesson_hour[i])
            else:
                continue
        my_dict.setdefault(line_list[0], my_summ)
print(my_dict)
