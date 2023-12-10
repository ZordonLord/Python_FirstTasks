# Задача 6. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# n = 385916 -> yes
# n = 123456 -> no

def sumnum (num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num/10)
    return sum

n = int(input("Введите шестизначное число: "))
a = int(n/1000)
b = int(n%1000)
if sumnum(a) == sumnum(b): print("yes")
else: print("no")