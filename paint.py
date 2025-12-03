import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image,ImageTk,ImageDraw

root = tk.Tk()
image = Image.new( "RGB", ( 1000, 1000), "white")

root.title('paint')
root.resizable(True,True)

color='black'

def Test():
    global color
    color= colorchooser.askcolor(title='color')[1]
    messagebox.askyesno('yes or no', '6+7=67?')

def paint_draw(event):
    x1, y1 = (event.x - 1), (event.y - 1) 
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_rectangle(x1, y2 ,x2, y1 , fill=color,outline=color)

def fill_fon():
    global image
    image = Image.new( "RGB", ( 1000, 1000), color)
    update_canvas_image()

def update_canvas_image(): 
    global canvas_image, photo 
    photo = ImageTk.PhotoImage(image) 
    canvas_image = canvas.create_image(0, 0, image=photo, anchor="nw")

button = tk.Button(root,text='press me',command=Test)
button.grid(row=0,column=4,padx=10,pady=10)

button = tk.Button(root,text='filling all',command=fill_fon)
button.grid(row=0,column=2,padx=10,pady=10)

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.grid(row=2,column=5)

canvas.bind("<B1-Motion>",paint_draw)

update_canvas_image()

root.mainloop()