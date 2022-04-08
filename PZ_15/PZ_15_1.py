# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]  # вввод чисел
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
for i in range(m):  # цикл в цикле по количеству строк и столбцов
    for o in range(n):
        if matrix[i][o] > 10:  # если переменная под индексом[строка][столбец] > 10, то присвоить ей значение 0
            matrix[i][o] = 0
print('Полученная матрица:')
for i in matrix:
    print(*i)
