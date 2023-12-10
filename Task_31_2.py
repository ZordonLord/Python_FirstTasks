# посчитать сумму всех целых чисел от 1 до 
# некоего N, котороe вводит пользователь

def summa(num):
    res = 0
    while True:
        if num == 0:
            break
        res += num
        num -= 1
    return res

# summa(3) = 3 + 2 + 1 + 0

def summa_rec(num):
    if num == 0:
        return 0
    return num + summa_rec(num - 1)

#summa_rec(4) = (4 + ( 3 + (2 + (1 + 0)))) погружение
# всплытие  4 + (3 + (2 + 1)) = 4  + 3 + 3 = 4 + 6 = 10


num = int(input("Введите натуральное число "))
print(f"Сумма всех целых чисел от 1 до {num} равна {summa(num)}")
print(f"Сумма рекурсией равна {summa_rec(num)}")

count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)