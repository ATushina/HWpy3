# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_odd_index(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i % 2 != 0:
            sum += numbers[i]
    print(f"Сумма равна: {sum}")


from random import randint
n = int(input("Ведите количество элементов списка: "))
numbers = []
for i in range(n):
    numbers.append(randint(0, n))
print (numbers)
sum_odd_index(numbers)
   