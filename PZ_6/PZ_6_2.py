# Дан список А размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент Bk равен сумме элементов А с номерами от 1 до K.
from random import randint
a = []

n = int(input("Введите количество элементов в списке:"))
while n:           # цикл, который задает рандомные числа из диапазона
    a.append(randint(0, 15))
    n -= 1
print(a)

o = a[0]
b = [o]
for i in range(1, len(a)):      # цикл, удовлетворяющий условию элемент Bk равен сумме элементов А
    o += a[i]
    b.append(o)
print(b)
