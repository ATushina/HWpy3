# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_opposite_index(numbers):
    l = len(numbers)//2 + 1 if len(numbers) % 2 != 0 else len(numbers)//2
    new_numbers = [numbers[i]*numbers[len(numbers)-i-1] for i in range(l)]
    print(new_numbers)

from random import randint
n = int(input("Ведите количество элементов списка: "))
numbers = []
for i in range(n):
    numbers.append(randint(0, 10))
print (numbers)
mult_opposite_index(numbers)