import tkinter as tk
from tkinter import ttk

global root, counter, a1t, a2t, a3t, b1t, b2t, b3t, c1t, c2t, c3t, announcer
a1t = a2t = a3t = b1t = b2t = b3t = c1t = c2t = c3t = 99
counter = 0


def a1_click():
    global a1t, counter
    if counter % 2 == 0:
        a1t = 1
        a1.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        a1t = 0
        a1.config(text="O")
        counter += 1
    win_check()

def a2_click():
    global a2t, counter
    if counter % 2 == 0:
        a2t = 1
        a2.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        a2t = 0
        a2.config(text="O")
        counter += 1
    win_check()

def a3_click():
    global a3t, counter
    if counter % 2 == 0:
        a3t = 1
        a3.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        a3t = 0
        a3.config(text="O")
        counter += 1
    win_check()

def b1_click():
    global b1t, counter
    if counter % 2 == 0:
        b1t = 1
        b1.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        b1t = 0
        b1.config(text="O")
        counter += 1
    win_check()

def b2_click():
    global b2t, counter
    if counter % 2 == 0:
        b2t = 1
        b2.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        b2t = 0
        b2.config(text="O")
        counter += 1
    win_check()

def b3_click():
    global b3t, counter
    if counter % 2 == 0:
        b3t = 1
        b3.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        b3t = 0
        b3.config(text="O")
        counter += 1
    win_check()

def c1_click():
    global c1t, counter
    if counter % 2 == 0:
        c1t = 1
        c1.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        c1t = 0
        c1.config(text="O")
        counter += 1
    win_check()

def c2_click():
    global c2t, counter
    if counter % 2 == 0:
        c2t = 1
        c2.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        c2t = 0
        c2.config(text="O")
        counter += 1
    win_check()

def c3_click():
    global c3t, counter
    if counter % 2 == 0:
        c3t = 1
        c3.config(text="X")
        counter += 1
    elif counter % 2 == 1:
        c3t = 0
        c3.config(text="O")
        counter += 1
    win_check()

def newgame_click():
    global counter, announcer, a1t, a2t, a3t, b1t, b2t, b3t, c1t, c2t, c3t
    a1t = a2t = a3t = b1t = b2t = b3t = c1t = c2t = c3t = 99
    counter = 0
    announcer.config(text="")
    a1.config(text="")
    a2.config(text="")
    a3.config(text="")
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    c1.config(text="")
    c2.config(text="")
    c3.config(text="")


#победные комбинации:
# a1+a2+a3 / b1+b2+b3 / c1+c2+c3
# a1+b1+c1 / a2+b2+c2 / a3+b3+c3
# a1+b2+c3 / a3+b2+c1

def win_check():
    global announcer
    if ((a1t == a2t == a3t == 1 or b1t == b2t == b3t == 1 or c1t == c2t == c3t == 1)
        or (a1t == b1t == c1t == 1 or a2t == b2t == c2t == 1 or a3t == b3t == c3t == 1)
            or (a1t == b2t == c3t == 1 or a3t == b2t == c1t == 1)):
        announcer.config(text='Кажется, крестики победили!')
    elif ((a1t == a2t == a3t == 0 or b1t == b2t == b3t == 0 or c1t == c2t == c3t == 0)
        or (a1t == b1t == c1t == 0 or a2t == b2t == c2t == 0 or a3t == b3t == c3t == 0)
            or (a1t == b2t == c3t == 0 or a3t == b2t == c1t == 0)):
        announcer.config(text='Кажется, нолики победили!')


root = tk.Tk()
root.geometry('290x220')
root.title('Крестики-нолики')

a1 = ttk.Button(root)
a1.config(command=a1_click)
a1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

a2 = ttk.Button(root)
a2.config(command=a2_click)
a2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

a3 = ttk.Button(root)
a3.config(command=a3_click)
a3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

b1 = ttk.Button(root)
b1.config(command=b1_click)
b1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

b2 = ttk.Button(root)
b2.config(command=b2_click)
b2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

b3 = ttk.Button(root)
b3.config(command=b3_click)
b3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

c1 = ttk.Button(root)
c1.config(command=c1_click)
c1.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

c2 = ttk.Button(root)
c2.config(command=c2_click)
c2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

c3 = ttk.Button(root)
c3.config(command=c3_click)
c3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

announcer = tk.Label(root)
announcer.grid(row=3, columnspan=3, padx=10, pady=10, sticky="nsew")

newgame = ttk.Button(root)
newgame.config(text="Начать новую игру", command=newgame_click)
newgame.grid(row=4, columnspan=3, padx=10, pady=10, sticky="nsew")

root.mainloop()
