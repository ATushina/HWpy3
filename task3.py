# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
x=[round(random.uniform(0, 10), 2) for x in range(10)]
print(x)

min= float((x[0]))%1
max= float((x[0]))%1
for i in x:
    i=(float(i))%1
    if i==0:
        continue

    if i>max:
        max=i
    elif i<min:
        min=i
    
print(f'Mинимальное значение дробной части элементов {round(min, 2)}')
print(f'Mаксимальное значение дробной части элементов {round(max, 2)}')
print(f'Разницa между максимальным и минимальным значением дробной части элементов {round((max-min),2)}')
