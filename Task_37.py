import random

# получить список квадратов нечетных значений списка на входе
def square_even(sp):
    result =[]
    for item in sp:
        if item % 2:
            result.append(item**2)
    return result



# sp = [1,5,4,6,8,9,7,8,9,10]
sp = [random.randint(1,10) for _ in range(15)]
print(sp)
print(square_even(sp))
print([item**2  for item in sp if item %2 ])
print([item**2 if item % 2 else 0 for item in sp ])
print(sum([item**2  for item in sp if item %2 ]))

print({i: sp.count(i) for i in set(sp)})