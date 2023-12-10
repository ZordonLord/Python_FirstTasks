# надо подсчитать количество сотрудников данной конторы
def calc_count(count_all):
    res = 0
    for item in count_all:
        if isinstance(item, int):
            res += item
        else:
            res += calc_count(item)
    return res



count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)
print(f"Количество сотрудников равно {calc_count(count_all)}")