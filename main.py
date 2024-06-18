import pandas as pd
import numpy as np

# Генерация DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание матрицы нулей размером (количество строк, количество уникальных значений)
one_hot = np.zeros((len(data), len(unique_values)), dtype=int)

# Установка единиц в позиции, соответствующей каждому уникальному значению
for i, value in enumerate(data['whoAmI']):
    index = np.where(unique_values == value)[0][0]
    one_hot[i, index] = 1

# Преобразование one_hot в DataFrame
one_hot_df = pd.DataFrame(one_hot, columns=unique_values)

# Вывод первых нескольких строк преобразованного DataFrame
print(one_hot_df.head())
