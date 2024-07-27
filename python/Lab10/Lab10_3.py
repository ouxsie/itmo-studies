import pandas as pd
import tkinter as tk

#   Task 1

data = [
    ('Python для автоматизации задач', 48),
    ('Python для науки о данных', 35),
    ('Анализ временных рядов', 17),
    ('Анализ текста с Python', 5),
    ('Введение в нейронные сети', 27),
    ('Математика для Data Science', 5),
    ('Python для анализа данных', 42),
    ('Психолингвистика и Python', 57),
    ('Машинное обучение', 28),
    ('Обработка естественного языка', 49),
    ('Оптимизация алгоритмов на Python', 16),
    ('Анализ данных', 10),
    ('Управление проектами с Python', 5),
    ('Бизнес-аналитика и Python', 55),
    ('Основы Data Science', 37),
    ('Продвинутый Python', 2),
    ('Основы бизнес-анализа', 40),
    ('Компьютерное зрение', 58),
    ('Анализ маркетинговых данных', 39),
    ('Распределенные системы на Python', 51)
]

df = pd.DataFrame(data)
df.rename(columns={0:"Name", 1:"Students"}, inplace=True)

#   Task 2

df = df.sort_values(by='Students', ascending=False)

#   Task 3
#   -------------------------- Графика --------------------------

root = tk.Tk()
root.geometry('250x200')
root.title('Курсы')

title = tk.Label(root, text='Статистика по курсам', font=('Arial', 12))
title.grid(column=0, row=0, columnspan=2)


top_label = tk.Label(root, text='Самый популярный курс')
top_label.grid(column=0, row=1, columnspan=2)

top_show = tk.Label(root, text=df.iloc[0,0])
top_show.grid(column=0, row=2, columnspan=1)

top_show_number = tk.Label(root, text=f'{df.iloc[0,1]} студент(ов)')
top_show_number.grid(column=1, row=2, columnspan=1)


gap_1 = tk.Label(root, text=' ')
gap_1.grid(column=0, row=3, columnspan=2)

second_label = tk.Label(root, text='Второй по популярности курс')
second_label.grid(column=0, row=4, columnspan=2)

second_show = tk.Label(root, text=df.iloc[1,0])
second_show.grid(column=0, row=5, columnspan=1)

second_show_number = tk.Label(root, text=f'{df.iloc[1,1]} студент(ов)')
second_show_number.grid(column=1, row=5, columnspan=1)

gap_2 = tk.Label(root, text=' ')
gap_2.grid(column=0, row=6, columnspan=2)

third_label = tk.Label(root, text='Третий по популяронсти курс')
third_label.grid(column=0, row=7, columnspan=2)

third_show = tk.Label(root, text=df.iloc[2,0])
third_show.grid(column=0, row=8, columnspan=1)

third_show_number = tk.Label(root, text=f'{df.iloc[2,1]} студент(ов)')
third_show_number.grid(column=1, row=8, columnspan=1)

root.mainloop()

