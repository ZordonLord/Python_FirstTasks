# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

day_distance = int(input("Введите расстояние в день: "))
distance = int(input("Введите расстояние: "))
days = distance//day_distance + (distance%day_distance > 0)
print(days)