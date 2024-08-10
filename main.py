from tkinter import *

brush_size = 10
eraser_size = 50

root = Tk()
root.geometry('800x800')
root.title('paint')

def size_changer(val):
    global brush_size
    brush_size=int(val)
def draw(event):
    canvas.create_oval(event.x - brush_size,
                       event.y - brush_size,
                       event.x + brush_size,
                       event.y + brush_size,
                       fill='black')
def eraser(event):
    canvas.create_oval(event.x - eraser_size,
                       event.y - eraser_size,
                       event.x + eraser_size,
                       event.y + eraser_size,
                       fill='red')
canvas = Canvas(root,width=800, height=700,bg='light grey')
canvas.bind('<B1-Motion>', draw)
canvas.bind('<B3-Motion>', eraser)

brush_slider = Scale(root,from_=1, to=100, orient='horizontal', command=size_changer)

brush_slider.pack()
canvas.pack()

root.mainloop()