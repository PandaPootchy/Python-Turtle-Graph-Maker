# This program makes a graph with a number of colloms and rows and a custom height and width
import tkinter
from tkinter.ttk import *
from tkinter.constants import *
from turtle import *

def turtle_graph_program():
    
    # Turtle Library
    def box(length, height):
        # Makes the box
        progress.step(1)
        for i in range(2):
            forward(length)
            left(90)
            forward(height)
            left(90)
            
    def graph(columns, rows, length, height):
        # Makes graph using boxes and goes back to starting position
        for i in range(rows):
            box(length, height)
            penup()
            forward(length)
            pendown()
        penup()
        forward(-length * rows)
        pendown()
        columns = columns - 1
        for i in range(columns):
            left(90)
            forward(height)
            right(90)
            for i in range(rows):
                box(length, height)
                penup()
                forward(length)
                pendown()
            penup()
            forward(-length * rows)
            pendown()
        right(90)
        forward(height * columns)
        left(90)
        progress.step(1)
    def centergraph(columns, rows, length, height):
        # Makes a graph in the center of the turtle screen 
        penup()
        goto(-rows * length / 2, -columns * height / 2)
        pendown()
        graph(columns, rows, length, height)
    # End of turtle library
    
    def chk_num():
        # Checks to see if user has input anythin
        box_width = e1.get()
        box_height = e2.get()
        col = e3.get()
        row = e4.get()
        
        if box_width == '':
            messagebox.showerror("Error", "You did not enter a value!")
        else:
            if box_width == '':
                messagebox.showerror("Error", "You did not enter a value!")
            else:
                if col == '':
                    messagebox.showerror("Error", "You did not enter a value!")
                else:
                    if row == '':
                        messagebox.showerror("Error", "You did not enter a value!")
                    else:
                        max_num()
    def max_num():
        # If max number is reached then a error window pops up
            box_width = int(e1.get())
            box_height = int(e2.get())
            col = int(e3.get())
            row = int(e4.get())
            
            if box_width in range(200):
                if box_width in range(200):
                    if col in range(200):
                        if row in range(200):
                            speed_test()
                        else:
                            messagebox.showerror("Error", "Number too big!")
                    else:
                        messagebox.showerror("Error", "Number too big!")
                else:
                    messagebox.showerror("Error", "Number too big!")
            else:
                messagebox.showerror("Error", "Number too big!")
                
    def turtle_reset():
        # Clears the screen and resets the turtles position
            clear()
            penup()
            goto(0,0)
            setheading(0)
            pendown()

    def turtle_exit():
        bye()
        tk.destroy()

    def speed_test():
        fast = var2.get()
        if fast == 3:
            speed(0)
            graph_draw()
        elif fast == 4:
            speed(3)
            graph_draw()
        elif fast == 0:
            messagebox.showerror("Error","Chose fast or slow")
            
    def graph_draw():
        # Test for if user has pressed yes or no
        box_width = int(e1.get())
        box_height = int(e2.get())
        col = int(e3.get())
        row = int(e4.get())
        value = var.get()
        if value == 1:
            b1.config(state = DISABLED)
            b2.config(state = DISABLED)
            progress.config(maximum=col*row+1)
            centergraph(col, row, box_width, box_height)
            b1.config(state = NORMAL)
            b2.config(state = NORMAL)
        elif value == 2:
            b1.config(state = DISABLED)
            b2.config(state = DISABLED)
            progress.config(maximum=col*row+1)
            graph(col, row, box_width, box_height)
            b1.config(state = NORMAL)
            b2.config(state = NORMAL)
        elif value == 0:
            messagebox.showerror("Error","Chose yes or no")

    # GUI variables      
    tk = tkinter.Tk()
    label = tkinter.Label
    button = tkinter.Button
    title = tk.title
    var = tkinter.IntVar()
    var2 = tkinter.IntVar()
    per = tkinter.StringVar()
    space = label(text="               ")
    messagebox = tkinter.messagebox
    e1 = tkinter.Entry(tk)
    e2 = tkinter.Entry(tk)
    e3 = tkinter.Entry(tk)
    e4 = tkinter.Entry(tk)
    r1 = tkinter.Radiobutton(tk, text="Yes", variable=var, value=1)
    r2 = tkinter.Radiobutton(tk, text="No", variable=var, value=2)
    r3 = tkinter.Radiobutton(tk, text="Fast", variable=var2, value=3)
    r4 = tkinter.Radiobutton(tk, text="Slow", variable=var2, value=4)
    progress = Progressbar(tk,orient=HORIZONTAL,length=200,mode='determinate')
    b1 = button(text="Draw", bg = "green", command = chk_num)
    b2 = button(text="Reset", bg = "red", command = turtle_reset)
    # The Gui
    tk.resizable(False, False)
    tk.update_idletasks()
    tk.protocol('WM_DELETE_WINDOW', turtle_exit)
    tk.iconbitmap('turtle.ico')
    title("Make A Graph")
    label(text="Enter box width: ").grid(column=0, row=0)
    e1.grid(column=1, row=0)
    label(text="Enter box height: ").grid(column=0, row=1)
    e2.grid(column=1, row=1)
    label(text="Enter how many coloms: ").grid(column=0, row=2)
    e3.grid(column=1, row=2)
    label(text="Enter how many rows: ").grid(column=0, row=3)
    e4.grid(column=1, row=3)
    label(text="Want the graph to be in the center: ").grid(column=0, row=4)
    r1.grid(column=1, row=4)
    r2.grid(column=2, row=4)
    label(text="How fast you want the turtle to draw: ").grid(column=0,row=5)
    r3.grid(column=1, row=5)
    r4.grid(column=2, row=5)
    label(text="").grid()
    label(text="Click draw when your ready.").grid(column=0, row=7)
    b1.grid(column=1, row=7)
    b2.grid(column=2, row=7)
    label(text="").grid(column=1, row=8)
    progress.grid(column=1, row=9)
    label(text="Drawing Progress:").grid(column=0, row=9)
    space.grid(column=0,row=10)
    
    tk.mainloop()
    
def starting():
    # Starts the main program
    tk.destroy()
    turtle_graph_program()

# The starting gui
tk = tkinter.Tk()
label = tkinter.Label
button = tkinter.Button
title = tk.title
tk.resizable(False, False)
tk.update_idletasks()
title("Turtle Graph Maker")
label(text="Welcome to graph drawing. This is a program were you can make a custom graph").grid()
label(text="Please remember the numbers you will put in resents pixels. If you dont know what a pixel is please look that up then press ok. If you already know what a pixel is then press ok.").grid()
button(text="Ok", command=starting).grid()
tk.iconbitmap('turtle.ico')
tk.mainloop()
