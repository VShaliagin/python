print('#' * 20 + ' Ex_5 ' + '#' * 20)
q_income = 'Введите значение выручки фирмы.\n'
income = int(input(q_income))
q_expenses = 'Введите значение издержек фирмы.\n'
expenses = int(input(q_expenses))

if income > expenses:
    print(f'Отлично вы работаете с прибылью')
    profitability = ( income - expenses ) / income
    print(f'Рентабельность выручки составила: {profitability}')
    q_workers = 'Введите численность работников фирмы.\n'
    workers = int(input(q_workers))
    profit_per_employee = ( income - expenses ) / workers
    print(f'Прибыль фирмы в расчете на одного сотрудника составила: { profit_per_employee}')
else:
    print(f'Вы работаете в убыток')