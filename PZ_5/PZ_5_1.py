# Составить функцию, которая выполняет суммирование  числового ряда.
nums = []
i = 0
n = int(input("Введите количество суммируемых элементов:"))
while i < n:
    x = int(input("Введите число:"))
    nums.append(x)                  # объединение
    i += 1


def sum_nums(list):               #
    if len(list) == 0:
        return 0
    i = 0
    s = 0
    while i < len(list):
        s += list[i]
        i += 1
    return s


print(sum_nums(nums))