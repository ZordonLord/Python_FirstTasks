# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, 
# где все коэффициенты случайные от -10 до 10.
# например, k=2 -> -x^2 + 3*x - 8 = 0 
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x  = 0 
# тут коэффициенты 3,0,-2,0

import random
# number = int(input("Введите натуральное число: "))
int_array = [11, -19, 17, 0] # [random.randint(-20,20) for _ in range(number+1)]
print(int_array)
strint_part = ""
for i in range(len(int_array)):
    if int_array[i] != 0:
        if abs(int_array[i]) == 1:
            strint_part += f"x^{len(int_array) - 1 - i} +"
        else:
            strint_part += f" {int_array[i]}*x^{len(int_array) - 1 - i} +"
strint_part = strint_part.replace("+ -", "- ")[:-6]+" = 0"
strint_part = strint_part.replace("^1", "")
print(strint_part)