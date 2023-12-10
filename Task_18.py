# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 2, 3, 4, 5]
k = 6

if list_1[0] > k:
    range_num = list_1[0] - k
else:
    range_num = k - list_1[0]
min_range = range_num
best_num = list_1[0]
i = 0
for i in range(len(list_1)):
    if list_1[i] > k:
        range_num = list_1[i] - k
    else:
        range_num = k - list_1[i]
    if range_num < min_range:
        min_range = range_num
        best_num = list_1[i]
print(best_num)