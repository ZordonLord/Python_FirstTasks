# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    a1 = []
    for j in range(num_columns):
        a2 = []
        for i in range(num_rows):
            if j == 0 or i == 0:
                a2.append(j+i+1)
            else: 
                a2.append(operation(j+1, i+1))
        a1.append(a2)
    for row in a1:
        print(*row)


print_operation_table(lambda x, y: x - y, 5, 1)
