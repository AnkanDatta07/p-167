# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:47:16 2023

@author: Ankan Datta
"""

from tkinter import *
from tkinter import ttk
root = Tk()

root.title("Working on canvas using functions")
root.geometry("990x655")
root.configure(bg = "cyan")

choose_color = Label(root, text = "CHOOSE COLOR", bg = "cyan")
choose_color.place(relx = 0.6, rely = 0.9, anchor = CENTER)
coordinates_value = [10,50,100,200,300,400,500,600,700,800,900]

canvas = Canvas(root, width = 990, height = 490, bg = "white", highlightbackground="gray")

fillcolor = ["green", "yellow", "red", "blue", "black"]

dropdown_color = ttk.Combobox(root, state = "readonly", value = fillcolor, width = 10)
dropdown_color.place(relx=0.8, rely = 0.9, anchor = CENTER)

keypress = ""

startx = Label(root, text = "StartX", bg = "cyan")
startx.place(relx=0.1, rely = 0.85, anchor = CENTER)
starty = Label(root, text = "StartY", bg = "cyan")
starty.place(relx=0.3, rely=0.85, anchor = CENTER)
endx = Label(root, text = "EndX", bg = "cyan")
endx.place(relx=0.5, rely=0.85,anchor = CENTER)
endy = Label(root, text = "EndY", bg = "cyan")
endy.place(relx=0.7, rely=0.85, anchor = CENTER)

d1 = ttk.Combobox(root, state = "readonly", values=coordinates_value, width = 10)

d1.place(relx=0.2, rely=0.85, anchor = CENTER)

d2 = ttk.Combobox(root, state = "readonly", values=coordinates_value, width = 10)

d2.place(relx=0.4, rely=0.85,anchor = CENTER)

d3 = ttk.Combobox(root, state = "readonly", values=coordinates_value, width = 10)

d3.place(relx=0.6, rely=0.85,anchor = CENTER)

d4 = ttk.Combobox(root, state = "readonly", values=coordinates_value, width = 10)

d4.place(relx=0.8, rely=0.85, anchor = CENTER)


def circle(event):
    global keypress
    global oldx
    global oldy
    global newx
    global newy
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'c'
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    global keypress
    global oldx
    global oldy
    global newx
    global newy
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'r'
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    global keypress
    global oldx
    global oldy
    global newx
    global newy
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'i'
    draw(keypress, oldx, oldy, newx, newy)

def draw(keypress, oldx, oldy, newx, newy):
    fillcolor = dropdown_color.get()
    if keypress == 'c':
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy, fill = fillcolor)
        
    if keypress == 'r':
        draw_rectangle = canvas.create_rectangle(oldx, oldy, newx, newy, fill = fillcolor)
        
    if keypress == 'i':
        draw_line = canvas.create_line(oldx, oldy, newx, newy, fill = fillcolor)

root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<i>", line)

canvas.pack()

root.mainloop()
