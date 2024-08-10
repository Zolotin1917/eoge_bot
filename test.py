from tkinter import *
from tkinter import colorchooser,messagebox
brush_size = 10
brush_color = 'black'
def draw(event):
    canv.create_oval(event.x - brush_size,
                          event.y - brush_size,
                          event.x + brush_size,
                          event.y + brush_size,
                          fill=brush_color, outline=brush_color)
def chooseColor():
    global brush_color
    (rgb, hx) = colorchooser.askcolor()
    brush_color = hx
def setBrushSize(value):
    global brush_size
    brush_size = int(value)
root = Tk()
root.geometry("800x600")

root.title("MyPaint")
root.columnconfigure(6, weight=1)
root.rowconfigure(2,weight=1)

canv = Canvas(root, bg="white")

canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

canv.bind("<B1-Motion>", draw)
Button(root, text = 'Выбор цвета', width=11, command=chooseColor).grid(column=1, row = 0, padx=5)
v=IntVar(value=brush_size)
Scale(root, variable=v, from_=1, to=100, orient=HORIZONTAL, command=setBrushSize).grid(row = 0, column=2, padx=5)
root.mainloop()