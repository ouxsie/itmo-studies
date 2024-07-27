import tkinter as tk

root = tk.Tk()
root.geometry("300x100")
root.title("Привет :)")

user_name = tk.StringVar(root)
entry = tk.Entry(root, textvariable=user_name)
entry.pack()

def button_click():
    new_window = tk.Toplevel(root)
    new_window.geometry("300x100")
    label = tk.Label(new_window, text=f"Привет, {user_name.get()}!")
    label.pack()
    new_window.mainloop()

button = tk.Button(root)
button.config(text="Привет")
button.pack()

button.config(command=button_click)
root.mainloop()
