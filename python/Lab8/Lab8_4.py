import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter
c = CurrencyConverter()


def startcurrency_select(event):
    global sc_choice
    sc_choice = event.widget.get()


def endcurrency_select(event):
    global ec_choice
    ec_choice = event.widget.get()


def button_click():
    global money, sc_choice, ec_choice
    newcurrency = c.convert(float(money.get()), sc_choice, ec_choice)
    newcurrency = round(newcurrency, 2)
    new_window = tk.Toplevel(root)
    new_window.geometry("300x80")
    label = tk.Label(new_window, text=f"Ваша сумма в новой выбранной валюте: {newcurrency}")
    label.pack()
    new_window.mainloop()


root = tk.Tk()
root.geometry("320x130")
root.title('Конвертер валют')

currencies = ['RUB', 'USD', 'EUR', 'GBP']

global money

money = tk.StringVar(root)
entry = tk.Entry(root, textvariable=money)
entry.grid(row=0, column=0, columnspan=4, padx=4, pady=4)

startcurrency_label = tk.Label(root, text="Выберете исходную валюту")
startcurrency_label.grid(column=0, row=1)
startcurrency = ttk.Combobox(root, values=currencies)
startcurrency.grid(column=1, row=1)
startcurrency.bind("<<ComboboxSelected>>", startcurrency_select)

endcurrency_label = tk.Label(root, text="Выберете целевую валюту")
endcurrency_label.grid(column=0, row=2)
endcurrency = ttk.Combobox(root, values=currencies)
endcurrency.grid(column=1, row=2)
endcurrency.bind("<<ComboboxSelected>>", endcurrency_select)

button = tk.Button(root)
button.config(text="Конвертировать")
button.config(command=button_click)
button.grid(row=3, column=0, columnspan=4, padx=4, pady=4)

root.mainloop()