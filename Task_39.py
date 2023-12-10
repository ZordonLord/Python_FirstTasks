# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

import random
# sp = [random.randint(1,10) for _ in range(10)]
# sp1 = [random.randint(1,10) for _ in range(5)]
# print(sp)
# print(sp1)
print(sp:=[random.randint(1,10) for _ in range(10)])
print(sp1:=[random.randint(1,10) for _ in range(5)])
sp1 = set(sp1)
result = []
for i in sp:
    if i not  in sp1:
        result.append(i)
print(result)
print(result2:=[i for i in sp if i not in set(sp1)])