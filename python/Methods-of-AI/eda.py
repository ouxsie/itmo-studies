# **Лабораторная работа 1. Кластеризация и снижение размерности.**

## Датасет: Cifer-Fraud-Detection-Dataset-AF from Huggingface


импорт библиотек

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')

настройка визуализации

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

задание Random State

RANDOM_STATE = 28
np.random.seed(RANDOM_STATE)

**1. загрузка и первичный анализ данных**

from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загрузка датасета
fraud_data = load_dataset('CiferAI/Cifer-Fraud-Detection-Dataset-AF', data_files='Cifer-Fraud-Detection-Dataset-AF-part-1-14.csv')

print(fraud_data)

df = pd.DataFrame.from_dict(fraud_data['train'], orient='columns')
print(df.head())

#дропаем ID отправителя и получателя (для деидентификации)
df = df.drop(columns=['nameOrig', 'nameDest'])

One-hot кодирование переменной type (через dummies)

df = pd.get_dummies(df, columns=['type'], prefix='type', dtype = 'int')
print(df.head())

Разбиение на предикторы (X) и целевую переменную (y_true)

X = df.drop(columns=['isFraud', 'isFlaggedFraud'])
y_true = df['isFraud']

print("Описание датасета:")
print(f"Количество образцов: {len(X)}")
print(f"Количество признаков: {len(X.columns)}")
print(f'Количество классов: {len(np.unique(y_true))}')
print(f"\nНазвания признаков: ")
for i, name in enumerate(X.columns):
    print(f"{i+1}. {name}")

разделение на train/test для оценки устойчивости

X_train, X_test, y_train, y_test = train_test_split(
    X, y_true, test_size=0.2, random_state=RANDOM_STATE, stratify=y_true
)

print(f"Размер обучающей выборки: {X_train.shape}")
print(f"Размер тестовой выборки: {X_test.shape}")

Проверка на пропущенные значения

print(f"\nПропущенные значения в данных: {pd.DataFrame(X_train).isnull().sum().sum()}")

Визуализация распределений признаков

fig, axes = plt.subplots(4, 3, figsize=(16, 12))
axes = axes.ravel()

for idx, col in enumerate(X_train.columns):
    axes[idx].hist(X_train[col], bins=20, edgecolor='black', alpha=0.7)
    axes[idx].set_title(col, fontsize=10)
    axes[idx].set_xlabel('Value')
    axes[idx].set_ylabel('Frequency')

Логарифмированные значения признаков

X_log = np.log1p(np.array(X_train))
X_log = pd.DataFrame(X_log, columns=X_train.columns.values)
print(X_log.head())

fig, axes = plt.subplots(4, 3, figsize=(16, 12))
axes = axes.ravel()

for idx, col in enumerate(X_log.columns):
    # Гистограмма с KDE
    axes[idx].hist(X_log[col], bins=20, edgecolor='black', alpha=0.5, density=True,
                   color='skyblue', label='Histogram')

    # KDE с настройками
    sns.kdeplot(X_log[col], ax=axes[idx], color='darkred', linewidth=2,
                label='KDE', alpha=0.6)

    axes[idx].set_title(f'Distribution of {col}', fontsize=10, fontweight='bold')
    axes[idx].set_xlabel('Value', fontsize=9)
    axes[idx].set_ylabel('Density', fontsize=9)
    axes[idx].legend(fontsize=8)
    axes[idx].grid(True, alpha=0.3)

# Скрываем лишние субплоты
for idx in range(len(X_log.columns), len(axes)):
    axes[idx].set_visible(False)

Yeo-Johnson

from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='yeo-johnson')
X_yj = np.log1p(np.array(X_train))
X_yj = pt.fit_transform(X_yj)
X_yj = pd.DataFrame(X_yj, columns=X_train.columns.values)

fig, axes = plt.subplots(4, 3, figsize=(16, 12))
axes = axes.ravel()

for idx, col in enumerate(X_yj.columns):
    # Гистограмма с KDE
    axes[idx].hist(X_yj[col], bins=20, edgecolor='black', alpha=0.5, density=True,
                   color='skyblue', label='Histogram')

    # KDE с настройками
    sns.kdeplot(X_yj[col], ax=axes[idx], color='darkred', linewidth=2,
                label='KDE', alpha=0.6)

    axes[idx].set_title(f'Distribution of {col}', fontsize=10, fontweight='bold')
    axes[idx].set_xlabel('Value', fontsize=9)
    axes[idx].set_ylabel('Density', fontsize=9)
    axes[idx].legend(fontsize=8)
    axes[idx].grid(True, alpha=0.3)

# Скрываем лишние субплоты
for idx in range(len(X_yj.columns), len(axes)):
    axes[idx].set_visible(False)

Анализ корреляций

correlation_matrix = pd.DataFrame(X_yj, columns=X_yj.columns).corr(method='kendall')

Визуализация корреляционной матрицы

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title('Корреляционная матрица признаков Cifer-Fraud-Detection-Dataset', fontsize=14)
plt.tight_layout()
plt.show()


# Поиск сильно коррелированных признаков
high_corr_pairs = []
for i in range(len(X_train.columns)):
    for j in range(i+1, len(X_train.columns)):
        if abs(correlation_matrix.iloc[i, j]) > 0.7:
            high_corr_pairs.append((X_train.columns[i], X_train.columns[j],
                                   correlation_matrix.iloc[i, j]))

print("Пары признаков с высокой корреляцией (|r| > 0.7):")
for pair in high_corr_pairs:
    print(f"{pair[0]} <-> {pair[1]}: {pair[2]:.3f}")

# Анализ выбросов с помощью IsolationForest
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.1, random_state=RANDOM_STATE)
outliers = iso_forest.fit_predict(X_train)
n_outliers = (outliers == -1).sum()

print(f"Обнаружено потенциальных выбросов: {n_outliers} ({n_outliers/len(X_train)*100:.1f}%)")
print("Примечание: выбросы обнаружены для диагностики, удаление не производится")

# Стандартизация данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Данные стандартизированы")
print(f"Среднее по признакам (train): {X_train_scaled.mean(axis=0).mean():.6f}")
print(f"Стд. отклонение по признакам (train): {X_train_scaled.std(axis=0).mean():.6f}")

**Гипотезы о структуре данных**

1. Выбросы в нуле, которые можно видеть на графиках распределений oldBalanceOrg и newBalanceDest после логарифмирования и преобразования Йео-Джонсона связаны с одной стороны с пополнением пустого счёта, а с другой - с опустошением счёта с деньгами, и эти операции в представленном датасете появлялись достаточно часто, чтобы вызвать такой "спайк".

2. С учётом значительной связи между oldbalanceOrg и newbalanceOrig, а также между oldbalanceDest и newbalanceDest, методы снижения размерности покажут свою эффективность.

3. Первые 4 компоненты смогут объяснить более 80% дисперсии данных.
