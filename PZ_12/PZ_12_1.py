# Реализовать прототип в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу.
from tkinter import*
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext

window = Tk()
window.title('Регистрация')
window.geometry('726x528')
window['bg'] = '#f99'
Label(text='Регистрационная страница электронной библиотеки', bg='#f99', height=3, font='arial 14').place(x=5, y=-10)
Label(text='Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой.', bg='#f99', font='arial 11').place(x=5, y=55)
Label(text='Введите регистрационное имя:', bg='#f99', font='arial 11').place(x=5, y=105)   # создала метки  с
Entry(width=19, font='arial 11').place(x=250, y=108)                            # помощью LABEL
Label(text='Введите пароль:', bg='#f99', font='arial 11').place(x=5, y=130)
Entry(width=19, font='arial 11').place(x=250, y=133)                 # создание текстовых полей с помощью  ENTRY
Label(text='Подтвердите пароль:', bg='#f99', font='arial 11').place(x=5, y=155)
Entry(width=19, font='arial 11').place(x=250, y=158)
Label(text='Ваш возраст:', bg='#f99', font='arial 11').place(x=5, y=195)
selected = IntVar()
Radiobutton(window, text='До 20', value=0, bg='#f99', variable=selected).place(x=110, y=196)  # cоздание переключателей
Radiobutton(window, text='20-30', value=1, bg='#f99', variable=selected).place(x=180, y=196)
Radiobutton(window, text='30-50', value=2, bg='#f99', variable=selected).place(x=250, y=196)
Radiobutton(window, text='Старше 50', value=3, bg='#f99', variable=selected).place(x=320, y=196)
Label(text='На каких языках читаете:', bg='#f99', font='arial 11').place(x=5, y=238)
chk = BooleanVar()
chk.set(True)
Checkbutton(window, text='русский', variable=chk).place(x=190, y=240)  # создала флажки с помощью Checkbutton
chk1 = BooleanVar()
chk1.set(False)
Checkbutton(window, text='английский', variable=chk1).place(x=260, y=240)
chk2 = BooleanVar()
chk2.set(False)
Checkbutton(window, text='французский', variable=chk2).place(x=350, y=240)
chk3 = BooleanVar()
chk3.set(False)
Checkbutton(window, text='немецкий', variable=chk3).place(x=445, y=240)
Label(text='Какой формат данных является для Вас предпочтительным', bg='#f99', font='arial 11').place(x=5, y=280)
n = scrolledtext.ScrolledText(window, width=10, height=1)
n.place(x=10, y=300)
n.insert('1.0', 'HTML' + '\n'), n.insert('2.0', 'Plain text')
Label(text='Ваши любимые авторы:', bg='#f99', font='arial 11').place(x=5, y=367)
scrolledtext.ScrolledText(window, width=45, height=3).place(x=12, y=390)
Button(text="Ок").place(x=10, y=450)         # создание кнопок
Button(text="Отменить").place(x=40, y=450)
Scrollbar().pack(side=RIGHT, fill=Y)
window.mainloop()

