#   For interactivity
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
import seaborn as sns
import squarify

data = pd.read_csv('dataset.csv', sep=',', encoding='windows-1251')

#   Task 3
x = data['Name']
y = data['Amount']

plt.figure(figsize=(13, 7))

plt.title('Продажи по продукту', fontsize=20)
plt.xlabel('Название продукта', fontsize=15)
plt.ylabel('Количество продаж', fontsize=15)
plt.bar(x,y, color='lightcoral')

#   Task 4
sum_revenue_regions = data.groupby('Region')['Income'].sum()
sum_revenue_regions.to_csv('Supplimental_csv\Task4_14.csv')

data_sum = pd.read_csv('Supplimental_csv\Task4_14.csv', sep=',', encoding='utf-8')


x = data_sum['Region']
y = data_sum['Income']

plt.figure(figsize=(16, 7.5))

plt.title('Продажи по фед. округу', fontsize=20)
plt.xlabel('Фед. округ', fontsize=15)
plt.ylabel('Выручка с продаж', fontsize=15)

plt.bar(x, y, color='lightcoral')

#   Task 5

sum_revenue_months = data.groupby('Month')['Income'].sum()
sum_revenue_months.to_csv('Supplimental_csv\Task5_7.csv')

data_mon = pd.read_csv('Supplimental_csv\Task5_7.csv', sep=',', encoding='utf-8')

x = data_mon['Month']
y = data_mon['Income']

plt.figure(figsize=(8, 7))

plt.title('Выручка по месяцам (в %)',fontsize=20)
plt.pie(y, labels=x, autopct='%1.1f%%', shadow=True, explode=[0.1] * len(x), startangle=90)
plt.axis('equal')

#   Task 6

x = data['Amount']
y = data['Income']

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=100, c='red', alpha=0.5)

plt.title("Зависимость дохода от количества продаж", fontsize=20)
plt.xlabel('Количество продаж', fontsize=15)
plt.ylabel('Доход', fontsize=15)

#   Task 7

data_mon = pd.read_csv('Supplimental_csv\Task5_7.csv', sep=',', encoding='utf-8')
x = data_mon['Month']
y = data_mon['Income']

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='lightcoral', linestyle='-', linewidth=2, marker='o', markersize=10)

plt.title('Доход по месяцам', fontsize=20)
plt.ylabel('Доход',fontsize=15)

plt.grid(True)


#   Task 11

x = data['Amount']
sns.histplot(x=x, bins=15, color='lightcoral')

plt.title('Дистрибуция количества продаж', fontsize=20)
plt.xlabel('Кол-во продаж', fontsize=12)
plt.ylabel('Частота встречаемости значения', fontsize=12)

#   Task 12

sum_sales_regions = data.groupby('Region')['Amount'].sum()
sum_sales_regions.to_csv('Supplimental_csv\Task12.csv')

data_sales = pd.read_csv('Supplimental_csv\Task12.csv', sep=',', encoding='utf-8')

data_sales['Amount_duplicate'] = data_sales.loc[:, 'Amount']
data_sales.to_csv('Supplimental_csv\Task12_1.csv')

data_sales_1 = pd.read_csv('Supplimental_csv\Task12_1.csv', sep=',', encoding='utf-8')

data_sales_11 = data_sales_1[['Amount', 'Amount_duplicate']]

plt.figure(figsize=(10,8))
sns.heatmap(data_sales_11, annot=True, cmap='coolwarm')
plt.title('Продажи по регионам', fontsize=20)


#   Task 13

plt.figure(figsize=(10,8))
sns.boxplot(y=data['Income'], color='lightcoral')
plt.ylabel('Доход', fontsize=15)
plt.title('Доход с квартилями и выбросами', fontsize=20)

#   Task 14

data_sum = pd.read_csv('Supplimental_csv\Task4_14.csv', sep=',', encoding='utf-8')

plt.figure(figsize=(10,8))
squarify.plot(sizes=data_sum['Income'], label=data_sum['Region'],
              color=sns.color_palette("magma", len(data_sum)), alpha=.8)

plt.title('Доход по регионам (в тыс. RUB)', fontsize=20)

#   Task 15: кол-во продаж и доход от продаж + кнопки для изменения масштаба


fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.2)


x = data['Amount']
y = data['Income']

sc = ax.scatter(x, y, s=40, marker='o', color='lightcoral')
plt.title('Зависимость дохода от количесства продаж', fontsize=20)

ax_zoom_in = plt.axes([0.7, 0.05, 0.1, 0.075], facecolor='lightcoral')
ax_zoom_out = plt.axes([0.81, 0.05, 0.1, 0.075], facecolor='lightcoral')

button_zoom_in = Button(ax_zoom_in, 'Zoom in')
button_zoom_out = Button(ax_zoom_out, 'Zoom out')

def zoom_in(event):
    xlims = ax.get_xlim()
    new_xlims = [xlims[0] * 1.1, xlims[1] * 0.9]
    ax.set_xlim(new_xlims)
    plt.draw()

def zoom_out(event):
    xlims = ax.get_xlim()
    new_xlims = [xlims[0] * 0.9, xlims[1] * 1.1]
    ax.set_xlim(new_xlims)
    plt.draw()

button_zoom_in.on_clicked(zoom_in)
button_zoom_out.on_clicked(zoom_out)

#   Task 16

sum_sales_by_product = data.groupby('Name')['Income'].sum()
sum_sales_by_product.to_csv('Supplimental_csv\Task16.csv')

data_product = pd.read_csv('Supplimental_csv\Task16.csv', sep=',', encoding='utf-8')

#   Graph 16
plt.figure(figsize=(10,8))
sns.violinplot(data=data_product, x='Income')
plt.xlabel('Доход')
plt.title('Диапазон доходов', fontsize=20)

# Task 17

data_17s = data.pivot_table(index='Region', columns='Name', values='Income', fill_value=0)
data_17s = data_17s.reset_index()
data_17s.to_csv('Supplimental_csv\Task17.csv', sep=';', encoding='utf-8')

data_17 = pd.read_csv('Supplimental_csv\Task17.csv', sep=';', encoding='utf-8')
data_17 = data_17.set_index('Region')

data_17.plot(kind='bar', stacked=True, figsize=(10,15),
             color=sns.color_palette("magma", len(data)))

plt.show()
