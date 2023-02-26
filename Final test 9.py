from tkinter import *
from random import *
canvas_width, canvas_height = 500, 500

def click():
    canvas.delete('all')
    side = randint(20, 400)
    x = randint(1, 500 - side)
    y = randint(1, 500 - side)
    z = randint(1, 500 - side)
    t = randint(1, 3)
    if t == 1:
        canvas.create_rectangle(x, y, x + side, y + side)
    elif t == 2:
        canvas.create_oval(x, y, x + side, y + side)
    elif t == 3:
        canvas.create_polygon(x, y, z, x + side, y + side, z + side)

root = Tk()
canvas = Canvas(root,  width=canvas_width,
height=canvas_height, bg='white')
canvas.pack()

Button(text='Генерация', command=click).pack()

root.mainloop()