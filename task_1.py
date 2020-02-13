'''1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные
(список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''

class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.__box = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
    def __str__(self):
        return ('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_1 ]))

    def __add__(self):
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_1[0])):
                self.__box[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        return ('\n'.join(['\t'.join([str(j) for j in i]) for i in self.__box]))

matrix_1 = [[1, 2, 3, 13], [4, 5, 6, 16], [7, 8, 9, 19]]
matrix_2 = [[9, 8, 7, 17], [6, 5, 4, 24], [3, 2, 1, 31]]

print(f'Матрица 1: \n{Matrix(matrix_1, matrix_2).__str__()}')
print(f'Матрица 2: \n{Matrix(matrix_2, matrix_1).__str__()}')
print(f'Сумма матриц:\n{Matrix(matrix_1, matrix_2).__add__()}')