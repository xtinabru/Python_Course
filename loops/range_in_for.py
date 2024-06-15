# FUNCTION RANGE 🐌

# for i in range(10):
#     print("Hello", i)

# range(n) generates a sequence of numbers from 0 to n-1, and the for loop iterates through this sequence.


# Overloading range() with two parameters 🐜

# if we want to start not from 0, we can use OVERLOADING of range() function.

# For example: range (1, 5)    -     # right border is not inclusive

# range(n): creates a sequence of numbers 0, 1, 2, 3, ..., n - 1;
# range(n, m): creates a sequence of numbers n, n + 1, n + 2, ..., m - 2, m - 1.


# ☀️ Let's write a program that displays
# those numbers from the interval [100,999] and end 7

# for i in range(100, 1000): # перебираем числа от 100 до 999
#     if i % 7 == 0:        # остаток деления на 10, для получения последней цифры
#         print(i)

# Please note that we passed the number 1000 as the second parameter.

#  ❕ ❕ ❕
# If the first parameter is greater than the second, then the range() function generates an empty sequence. For example, calling the function range(10, 1) results in the generation of an empty sequence.

# Overloading range() with THREE parameters 🐜

# By passing two parameters to the range() function we can generate any sequence of integers with a step of 1. But what if you need to change the step? What if we want to generate a sequence of numbers 5, 10, 15, 20, 25?
#
# ❗️❗️❗️ In this case, there is another overload of the range() function that takes three parameters:
# range(n, m, k).
#
# The first parameter specifies the start of the sequence, the second parameter specifies the stop of the sequence, and the third – the number generation step.

# ☀️
# for i in range(56, 171, 2):
#     print(i)

# OR WE CAN USE

# for i in range(56, 171):
#     if i % 2 == 0:
#         print(i)

# ➖ NEGATIVE STEPS
# Example:

# for i in range(5, 0, -1):
#     print(i, end=" ")
# print("LET'S GO!")

# 🟡 Если величина шага отрицательна и первый параметр меньше второго, то функция range() генерирует пустую последовательность. Например, вызов функции range(1, 10, -1) приводит к генерации пустой последовательности.

# 🟡

# range(10)	0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 10)	1, 2, 3, 4, 5, 6, 7, 8, 9
# range(3, 7)	3, 4, 5, 6
# range(7, 3)	пустая последовательность
# range(2, 15, 3)	2, 5, 8, 11, 14
# range(9, 2, -1)	9, 8, 7, 6, 5, 4, 3
# range(3, 10, -2)	пустая последовательность

# 🟡 Функция range() может генерировать только целые числа, включая отрицательные.
# ⛔️ Величина шага не может равняться нулю. Следующий код:

# for i in range(1, 10, 0):
#     print(i)
# приведет к ошибке ValueError: range() arg 3 must not be zero.
