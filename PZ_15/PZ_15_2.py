# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]  # ввод чисел
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:         # цикл по матрице и вывод без скобок каждой строки
    print(*i)
for i in range(len(matrix)):       # цикл в цикле по количеству строк и столбцов
    for j in range(len(matrix[0])):
        if i > j or i < j:
            matrix[i][j] = matrix[i][j] * 2   # цикл умножит значения на 2 по всей матрице, кроме главной диагонали
print('Полученная матрица:')
for i in matrix:
    print(*i)

