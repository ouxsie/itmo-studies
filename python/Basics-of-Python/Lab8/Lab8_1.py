import tkinter as tk

root = tk.Tk()
root.geometry("300x100")
root.title("Почти Hello World!")

label = tk.Label(root, text="Привет мир")
label.pack()

def button_click():
    button.config(text="Кнопка нажата")


button = tk.Button(root, text="Нажми меня")
button.pack()

button.config(command=button_click)

root.mainloop()
