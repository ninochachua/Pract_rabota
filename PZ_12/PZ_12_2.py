# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ № 3 – 8.

from tkinter import *

def x2(vhod):
    r = {}
    for i in range(0, int(n.get()) + 1):
        r[i] = int(i) ** 3
    c['text'] = 'Сгенерированный словарь', r
    del r[list(r.keys())[0]], r[list(r.keys())[-1]]
    g['text'] = 'Сгенерированный словарь с удалёнными элементами', r


root = Tk()
root.title('Генерация словарей')
root.geometry("700x100")
Label(text='Количество:').grid(row=1, column=0)  # Создание текстовых меток с помощью Label
n = Entry(width=60, font='arial 12')
n.grid(row=1, column=1)
c = Label(font='arial 9')
c.grid(row=5, column=1)
g = Label(font='arial 9')
g.grid(row=6, column=1)
button1 = Button(text="Сгенерировать")     # Создание кнопок
button1.grid(row=4, column=1)
button1.bind('<Button-1>', x2)
root.mainloop()
