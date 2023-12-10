# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

import random
# sp = [1,2,3,4,5]
print(sp:=[random.randint(1,10) for _ in range(10)])
count = 0
for i in range(len(sp)):
    if sp[i] > sp[i-1] and sp[i] > sp[(i+1)%len(sp)]:
        count +=1
print(count)
print(sum([1 if sp[i] > sp[i-1] and sp[i] > sp[(i+1)%len(sp)] else 0 for i in range(len(sp))]))
print(sum([1 for i in range(len(sp)) if sp[i] > sp[i-1] and sp[i] > sp[(i+1)%len(sp)]]))