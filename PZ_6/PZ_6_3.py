# Дан список размера N и целое число. Осуществить сдвиг жлементов списка вправо на K позиций.
# Первые K элементов полученного списка положить равными 0.
from random import randint
a = []

n = int(input("Введите количество элементов в списке:"))
while n:                          # цикл, генерирующий рандомыне числа из диапазона
    a.append(randint(0, 15))
    n -= 1
print(a)

k = int(input("Введите число K:"))
while k:
    a.insert(0, 0)   # метод, вставляющий элемент в список по указанному индексу
    del a[-1]       # удаление элемента по индексу
    k -= 1
print(a)
