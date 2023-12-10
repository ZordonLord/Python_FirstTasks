# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Обязательно сделате без get_dummies.
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
print(data.head())
print()

one_hot_encoding = []
for item in lst:
    if item == 'robot':
        one_hot_encoding.append([1, 0])
    else:
        one_hot_encoding.append([0, 1])

data2 = pd.DataFrame(one_hot_encoding, columns=['robot', 'human'])
print(data2.head())