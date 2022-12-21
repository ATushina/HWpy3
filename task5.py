#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input("Ведите число: "))
result_list = [0] * (num * 2 + 1)

for i in range(num + 1):
    if i == 0:
        continue
    elif i == 1:
        result_list[num + i] = 1
        result_list[num - i] = 1
    else:
        result_list[num + i] = result_list[num + i - 1] + result_list[num + i - 2]
        result_list[num - i] = result_list[num - i + 2] - result_list[num - i + 1]
    
print(result_list)
