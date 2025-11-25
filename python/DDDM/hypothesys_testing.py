import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('income.csv', sep=';')

df = df.dropna(subset=['position_category', 'income_чиновник'])

cb = df.loc[df['state_agency'] == 'mincult', 'income_month_const_чиновник'].tolist()
#cb = list(cb)
print(cb)

print(df['state_agency'].unique()[1])

# Создаём словарь для хранения массивов
income_arrays = {}

for agency in df['state_agency'].unique():
    # Получаем массив доходов для текущего агентства
    income_array = df.loc[df['state_agency'] == agency, 'income_month_const_чиновник'].values
    # Сохраняем в словарь с ключом по названию агентства
    income_arrays[agency] = income_array

ministries = list(income_arrays.keys())
ministries[0]

ministries = list(income_arrays.keys())
for i in range(len(ministries)):
  if ministries[i] != 'minfin':
    print()
    print(f'Минфин vs {ministries[i]}')
    t_stat, p_value = stats.ttest_ind(income_arrays['minfin'], income_arrays[f'{ministries[i]}'])
    print(f"t-статистика: {t_stat:.2}, p-значение: {p_value:.2}")
  if ministries[i] != 'digital':
    print()
    print(f'Минцифры vs {ministries[i]}')
    t_stat, p_value = stats.ttest_ind(income_arrays['digital'], income_arrays[f'{ministries[i]}'])
    print(f"t-статистика: {t_stat:.2}, p-значение: {p_value:.2}")
  else:
    continue

mean_income_by_ministry_array = []
for i in range(len(ministries)):
  print()
  print(f'Среднее в {ministries[i]}')
  print(income_arrays[f'{ministries[i]}'].mean())
  mean_income_by_ministry_array.append(income_arrays[f'{ministries[i]}'].mean().tolist())

print(mean_income_by_ministry_array)

data_array = {}
for i in range(len(ministries)):
  new_data = {f'{ministries[i]}': mean_income_by_ministry_array[i]}
  data_array.update(new_data)

data_df = pd.DataFrame(list(data_array.items()), columns=['ministry','mean_salary'])

data_df = data_df.drop(13)

seaborn.barplot(y='ministry', x='mean_salary', data=data_df)
plt.show()

Гипотеза 3 (м vs ж)

hyp_3_df = df[df['state_agency'] != 'mcx']

male_salaries = hyp_3_df.loc[df['gender'] == 'm', 'income_month_const_чиновник'].tolist()
female_salaries = hyp_3_df.loc[df['gender'] == 'f', 'income_month_const_чиновник'].tolist()

t_stat_gender, p_value_gender = stats.ttest_ind(male_salaries, female_salaries)
print(f"t-статистика: {t_stat:.2}, p-значение: {p_value:.2}")

male_mean = np.nanmean(male_salaries).tolist()
female_mean = np.nanmean(female_salaries).tolist()

print(f'Средняя зп мужчин: {male_mean}, средняя зп женщин: {female_mean}')

seaborn.barplot(x=['Зарплата женщин', 'Зарплата мужчин'], y=[female_mean, male_mean])
plt.show()
