'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

#from sys import argv

#функция по расчету факториал
def my_factorial(a, i = 1, s = 1):
    while i <= a:
        s = s * i
        yield s
        i+=1

# args = argv
# x = args[1]

#Вызов функции по расчету 15! (факториал)
for el in my_factorial(15):
    print(el)
