import tkinter as tk

window = tk.Tk()
window.title('Hello!')
window.geometry('300x300')

var = tk.StringVar()


def insert_text():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


e = tk.Entry(window, show=None)
e.pack()

b1 = tk.Button(window, text='从这里输入', width=15, height=2, command=insert_text)
b1.pack()
b2 = tk.Button(window, text='从文尾输入', width=15, height=2, command=insert_end)
b2.pack()
t = tk.Text(window, height=8)
t.pack()

window.mainloop()
