import os
import random


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sumOfElements(num):
    arr = []
    sum = 0
    for i in str(num).split('.'):
        arr.append(i)

    for a in arr:
        for b in a:
            sum += int(b)
    return sum
#
# print(sumOfElements(6782))


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def printMult(n):
    arr = []

    for i in range(1,n+1):
        mult = 1
        for j in range(i,1,-1):
            mult *= j
        arr.append(mult)


    return arr
#
# print(printMult(4))


# Задайте список из n чисел последовательности $(1+1\n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# N = 6
def printDict(N):
    n = [x for x in range(1,N+1)]
    m = [round((1+1/x)**x, 2) for x in n]
    d = dict(zip(n,m))
    return d

# print(printDict(N))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Enter a number: "))
array = []
summ = 0

try:
    for i in range(n):
        array.append(random.randint(-n, n))
        print(array[i], end=" ")

    print("\n")

    file = open('Numbers.txt', 'r')

    while True:
        line = file.readline()
        if not line:
            break

        summ += array[int(line)]
        print(summ, end=" ")

    print("\n")
    print("Result = " + str(summ))
except IndexError:
    print("list index out of range")




#Реализуйте алгоритм перемешивания списка.
array = [1,2,3,4,5,6,7,8,9]

random.shuffle(array)
# print(array)
