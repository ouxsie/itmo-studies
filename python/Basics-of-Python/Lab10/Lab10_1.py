import pandas as pd
import tkinter as tk
from tkinter import ttk

#   Task 1 // Столбики: 'Name', 'Price', 'Amount', 'Store'
#   Магазины: 'Веселый Лук' 'Смешной Огурец' 'Хихикающая Капуста' 'Улыбка Помидора' 'Грустный Баклажан'

data = pd.read_csv('Lab10_1.txt')
#print(data['Store'].unique())

#   Магазин 'Веселый Лук'
happy_onion = data.query('Store == "Веселый Лук"')
happy_onion = happy_onion.drop('Store', axis=1)

# Запаковываем первый магазин в кортежи
happy_onion_list = list(happy_onion.itertuples(index=False, name=None))

# Считаем выручку и сохраняем в словарь
happy_onion_revenue = happy_onion['Price'].sum()
dict = {'Веселый Лук' : happy_onion_revenue}


#   Магазин 'Смешной Огурец'
hilarious_cucumber = data.query('Store == "Смешной Огурец"')
hilarious_cucumber = hilarious_cucumber.drop('Store', axis=1)

hilarious_cucumber_list = list(hilarious_cucumber.itertuples(index=False, name=None))

hilarious_cucumber_revenue = hilarious_cucumber['Price'].sum()
dict['Смешной Огурец'] = hilarious_cucumber_revenue


#   Магазин 'Хихикающая Капуста'
giggling_cabbage = data.query('Store == "Хихикающая Капуста"')
giggling_cabbage = giggling_cabbage.drop('Store', axis=1)

giggling_cabbage_list = list(giggling_cabbage.itertuples(index=False, name=None))

giggling_cabbage_revenue = giggling_cabbage['Price'].sum()
dict['Хихикающая капуста'] = giggling_cabbage_revenue


#   Магазин 'Улыбка Помидора'
tomatos_smile = data.query('Store == "Улыбка Помидора"')
tomatos_smile = tomatos_smile.drop('Store', axis=1)

tomatos_smile_list = list(tomatos_smile.itertuples(index=False, name=None))

tomatos_smile_revenue = tomatos_smile['Price'].sum()
dict['Улыбка Помидора'] = tomatos_smile_revenue

#   Магазин 'Грустный Баклажан'
sad_eggplant = data.query('Store == "Грустный Баклажан"')
sad_eggplant = sad_eggplant.drop('Store', axis=1)

sad_eggplant_list = list(sad_eggplant.itertuples(index=False, name=None))

sad_eggplant_revenue = sad_eggplant['Price'].sum()
dict['Грустный Баклажан'] = sad_eggplant_revenue

#   Магазины с наибольшей выручкой
total_revenue = pd.Series(dict, name='Revenue')
total_revenue.index.name = 'Name'
total_revenue = total_revenue.sort_values(ascending=False)
total_revenue = total_revenue.reset_index()

#   первая цифра - по y, вторая - по x
#   print(total_revenue.iloc[0,0])

#   -------------------------- Графика --------------------------

def what_store(name):
    if name == 'Веселый Лук':
        return happy_onion
    elif name == 'Смешной Огурец':
        return hilarious_cucumber
    elif name == 'Хихикающая Капуста':
        return giggling_cabbage
    elif name == 'Улыбка Помидора':
        return tomatos_smile
    elif name == 'Грустный Баклажан':
        return sad_eggplant

def store1_click():
    store = what_store(total_revenue.iloc[0,0])
    column_names = store.columns
    store1_window = tk.Toplevel(root)
    store1_window.geometry('400x200')
    store1_window.title('Подробная статистика')

    n_rows = store.shape[0]
    n_cols = store.shape[1]

    i = 0
    for j, col in enumerate(column_names):
        text = tk.Text(store1_window, width=16, height=1, bg="#F08080")
        text.grid(row=i, column=j)
        text.insert(tk.INSERT, col)

    for i in range(n_rows):
        for j in range(n_cols):
            text = tk.Text(store1_window, width=16, height=1)
            text.grid(row=i + 1, column=j)
            text.insert(tk.INSERT, store.iloc[i][j])

    shop_revenue = tk.Label(store1_window, text=f'Общая выручка магазина составляет {total_revenue.iloc[0,1]}.',
                            font='Helvetica 10')
    shop_revenue.grid(row=i + 3, column=0, columnspan=n_cols)
    store1_window.mainloop()

def store2_click():
    store = what_store(total_revenue.iloc[1,0])
    column_names = store.columns
    store2_window = tk.Toplevel(root)
    store2_window.geometry('400x200')
    store2_window.title('Подробная статистика')

    n_rows = store.shape[0]
    n_cols = store.shape[1]

    i = 0
    for j, col in enumerate(column_names):
        text = tk.Text(store2_window, width=16, height=1, bg="#F08080")
        text.grid(row=i, column=j)
        text.insert(tk.INSERT, col)

    for i in range(n_rows):
        for j in range(n_cols):
            text = tk.Text(store2_window, width=16, height=1)
            text.grid(row=i + 1, column=j)
            text.insert(tk.INSERT, store.iloc[i][j])

    shop_revenue = tk.Label(store2_window, text=f'Общая выручка магазина составляет {total_revenue.iloc[1,1]}.',
                            font='Helvetica 10')
    shop_revenue.grid(row=i + 3, column=0, columnspan=n_cols)
    store2_window.mainloop()

def store3_click():
    store = what_store(total_revenue.iloc[2,0])
    column_names = store.columns
    store3_window = tk.Toplevel(root)
    store3_window.geometry('400x200')
    store3_window.title('Подробная статистика')

    n_rows = store.shape[0]
    n_cols = store.shape[1]

    i = 0
    for j, col in enumerate(column_names):
        text = tk.Text(store3_window, width=16, height=1, bg="#F08080")
        text.grid(row=i, column=j)
        text.insert(tk.INSERT, col)

    for i in range(n_rows):
        for j in range(n_cols):
            text = tk.Text(store3_window, width=16, height=1)
            text.grid(row=i + 1, column=j)
            text.insert(tk.INSERT, store.iloc[i][j])

    shop_revenue = tk.Label(store3_window, text=f'Общая выручка магазина составляет {total_revenue.iloc[2,1]}.',
                            font='Helvetica 10')
    shop_revenue.grid(row=i + 3, column=0, columnspan=n_cols)
    store3_window.mainloop()


root = tk.Tk()
root.geometry('310x120')
root.title('Статистика по магазинам')

title = tk.Label(root, text='Магазины с наибольшей выручкой', font='Helvetica 12 bold')
title.grid(row=0, column=0, columnspan=3)


store1_name = tk.Label(root, text=total_revenue.iloc[0,0], font='Helvetica 12')
store1_name.grid(row=1, column=0, columnspan=1)

store1_revenue = tk.Label(root, text=total_revenue.iloc[0,1], font='Helvetica 12')
store1_revenue.grid(row=1, column=1, columnspan=1)

store1_b = ttk.Button(root)
store1_b.config(text='Подробнее', command=store1_click)
store1_b.grid(row=1, column=2, columnspan=1)


store2_name = tk.Label(root, text=total_revenue.iloc[1,0], font='Helvetica 12')
store2_name.grid(row=2, column=0, columnspan=1)

store2_revenue = tk.Label(root, text=total_revenue.iloc[1,1], font='Helvetica 12')
store2_revenue.grid(row=2, column=1, columnspan=1)

store2_b = ttk.Button(root)
store2_b.config(text='Подробнее', command=store2_click)
store2_b.grid(row=2, column=2, columnspan=1)


store3_name = tk.Label(root, text=total_revenue.iloc[2,0], font='Helvetica 12')
store3_name.grid(row=3, column=0, columnspan=1)

store3_revenue = tk.Label(root, text=total_revenue.iloc[2,1], font='Helvetica 12')
store3_revenue.grid(row=3, column=1, columnspan=1)

store3_b = ttk.Button(root)
store3_b.config(text='Подробнее', command=store3_click)
store3_b.grid(row=3, column=2, columnspan=1)


root.mainloop()

