import pandas as pd
import tkinter as tk

# В датасете: назначение перевода, тип транзакции (1 - доход, 0 - расход), сумма транзакции соответственно

data = [
    ('Ремонт помещения', 1, 74984, 'Февраль'),
    ('Покупка оборудования', 0, 65351, 'Ноябрь'),
    ('Аренда помещения', 0, 9058, 'Март'),
    ('Ремонт помещения', 0, 83917, 'Июнь'),
    ('Аренда помещения', 1, 16662, 'Январь'),
    ('Благотворительность', 1, 58877, 'Июль'),
    ('Офисные расходы', 0, 24873, 'Март'),
    ('Транспортные расходы', 1, 35245, 'Август'),
    ('Консультационные услуги', 1, 73848, 'Март'),
    ('Аренда помещения', 0, 29122, 'Октябрь'),
    ('Ремонт помещения', 1, 17585, 'Февраль'),
    ('Зарплата сотрудникам', 1, 15612, 'Сентябрь'),
    ('Оплата коммунальных услуг', 1, 76877, 'Июнь'),
    ('Научные исследования', 0, 59539, 'Июль'),
    ('Благотворительность', 0, 6311, 'Август'),
    ('Закупка материалов', 1, 60188, 'Октябрь'),
    ('Обслуживание техники', 0, 31883, 'Август'),
    ('Закупка материалов', 0, 59819, 'Март'),
    ('Маркетинговая кампания', 1, 59462, 'Июнь'),
    ('Научные исследования', 0, 72964, 'Апрель')
]

df = pd.DataFrame(data)
df.rename(columns={0:"Name", 1:"Type", 2:"Income", 3:"Month"}, inplace=True)

#   Task 1

gross_income_data = df.query('Type == 1')
gross_income = gross_income_data['Income'].sum()

gross_expidenture_data = df.query('Type == 0')
gross_expidenture = gross_expidenture_data['Income'].sum()

#   Task 2

months = df.groupby('Month')['Income'].sum()

months.index.name = 'Month'
months = months.sort_values(ascending=False)
months = months.reset_index()

#   Task 3
total = gross_income - gross_expidenture

print(months)

#   Task 4
#   -------------------------- Графика --------------------------

root = tk.Tk()
root.geometry('200x200')
root.title('Транзакции')

title = tk.Label(root, text='Статистика транзакций', font=('Arial', 12))
title.grid(column=0, row=0, columnspan=2)


income_label = tk.Label(root, text='Общий доход')
income_label.grid(column=0, row=1, columnspan=1)

income_show = tk.Label(root, text=gross_income)
income_show.grid(column=1, row=1, columnspan=1)


expidenture_label = tk.Label(root, text='Общий расход')
expidenture_label.grid(column=0, row=2, columnspan=1)

expidenture_show = tk.Label(root, text=gross_expidenture)
expidenture_show.grid(column=1, row=2, columnspan=1)


big_money_month = tk.Label(root, text='Месяц с наиб. доходом')
big_money_month.grid(column=0, row=3, columnspan=1)

big_money_show = tk.Label(root, text=months.iloc[0,0])
big_money_show.grid(column=1, row=3, columnspan=1)


small_money_month = tk.Label(root, text='Месяц с наиб. расходом')
small_money_month.grid(column=0, row=4, columnspan=1)

small_money_show = tk.Label(root, text=months.iloc[-1,0])
small_money_show.grid(column=1, row=4, columnspan=1)


total_label = tk.Label(root, text='Текущий баланс', font='Arial 10')
total_label.grid(column=0, row=5, columnspan=2)

total_show = tk.Label(root, text=total)
total_show.grid(column=0, row=6, columnspan=2)

root.mainloop()
