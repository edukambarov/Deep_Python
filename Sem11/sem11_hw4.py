# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
#
# Атрибуты класса:
#
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
#
# Методы класса:
#
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный список data размером rows x cols и заполняет его нулями.
#
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки. Например:
#
#
# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.
#
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
#
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.
#
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.
#
# Пример
#
# На входе:
#
#
# # Создаем матрицы
# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]
#
# matrix2 = Matrix(2, 3)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]
#
# # Выводим матрицы
# print(matrix1)
#
# print(matrix2)
# На выходе:
#
#
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# На входе:
#
#
# # Сравниваем матрицы
# print(matrix1 == matrix2)
# На выходе:
#
#
# False
# На входе:
#
#
# # Выполняем операцию сложения матриц
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)
# На выходе:
#
#
# 8 10 12
# 14 16 18
# На входе:
#
#
# # Выполняем операцию умножения матриц
# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]
#
# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]
#
# result = matrix3 * matrix4
# print(result)
# На выходе:
#
#
# 25 28
# 57 64
# 89 100

class Matrix:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)


    def __repr__(self):
        return Matrix({self.rows}, {self.cols})

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                return self.data == other.data
            raise ValueError('Несоразмерные матрицы')
        raise TypeError('Передан объект неподходящего класса')

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                new_data = [[self.data[i][j] + other.data[i][j]
                             for j in range(len(self.data[0]))]
                            for i in range(len(self.data))]
                res_matrix = Matrix(self.rows, self.cols)
                res_matrix.data = new_data
                return res_matrix
            raise ValueError('Несоразмерные матрицы')
        raise TypeError('Передан объект неподходящего класса')

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                new_data = [[sum(self.data[i][k] * other.data[k][j]
                                 for k in range(len(self.data[0])))
                             for j in range(len(other.data[0]))]
                            for i in range(len(self.data))]
                res_matrix = Matrix(self.rows, self.cols)
                res_matrix.data = new_data
                return res_matrix
            raise ValueError('Несоразмерные матрицы')
        raise TypeError('Передан объект неподходящего класса')

if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)

    print(matrix2)

    print(matrix1 == matrix2)

    matrix_sum = matrix1 + matrix2

    print(matrix_sum)
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)

