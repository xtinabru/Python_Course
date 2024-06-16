# Quantity counting 🍀

# The key to counting is using a counter variable.

# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#         print("Was entered", counter, "numbers which are more than 10.")

# Counting quantities is a very common scenario. It consists of two steps:

# 1. Creating a counter variable and giving it its initial value: counter = 0;
# 2. Increment counter variable by 1: counter = counter + 1.

# ❗️ Often when writing programs you need to use several counters. Let's modify the previous program:

# let's also count the number of zeros among the entered numbers.

# counter1 = 0
# counter2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
#         print("Было введено", counter1, "чисел, больших 10.")
#         print("Было введено", counter2, "нулей.")

# 🔅 count the number of numbers from a range [1,100] whose square ends in 4

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
#         print(counter)

# Calculating sum and product 🍀

# 🔅 Programm which counts 10 numbers and defines the sum of which is bigger than 10

# total = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
#         print("The sum of the numbers bigger than 10 equals", total)

# Counting sums consists of two steps:

# 1. Creating a sum variable and giving it its initial value: total = 0;
# 2. Increment sum variable by the needed number: total = total + num

# 🔅 Programm that calculates the sum of natural numbers from 1 to 100

# total = 0
# for i in range(1, 101):
#     total = total + i
#     print("Sum =", total)

# 🔅 Programm that asks for 10 integers and finds their average:

# total = 0
# for i in range(10):
#     num = int(input())
#     total = total + num
#     average = total / 10
#     print("Median = ", average)

# ❗️ When we multiply total = 1 NOT 0

# Exchange of variable values 🍀

# USE temporary variable

# temp = x
# x = y
# y = temp

# x, y = y, x

# Signal marks 🍀

# Сигнальная метка (флажок) может использоваться, когда надо, чтобы одна часть
# программы узнала о происходящем в другой части программы.

# 🟠
# Напишем программу, определяющую, что натуральное число является простым:

# num = int(input())
# flag = True  # создаём флажок и ставим его в True, что означает "число простое".

# for i in range(2, num): # Цикл проходит по всем числам от 2 до num - 1 (в данном случае от 2 до 9). Переменная i последовательно принимает значения 2, 3, 4, ..., 9.
#     if (
#         num % i == 0
#     ):  # если исходное число делится на какое-либо отличное от 1 и самого себя
#       # Детали проверки для num = 10:
#       # i = 2: 10 % 2 == 0 → делится, значит, flag = False.
#       # i = 3: 10 % 3 != 0 → не делится, ничего не меняется.
#       # i = 4: 10 % 4 != 0 → не делится, ничего не меняется.
#       # i = 5: 10 % 5 == 0 → делится, но flag уже False.
#       # И так далее для i = 6, 7, 8, 9.
#         flag = False
# if num == 1:
#     print("Это единица, она не простая и не составная")
# elif flag == True:
#     print("Число простое")
# else:
#     print("Число составное")

# Maximum and minimum🍀

# 🟠 programm which takes 10 positive numbers and finds the biggest

# largest = 0

# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print("The largest is", largest)

# if not only positive, we may use:

largest = int(input())  # принимаем первое число за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print("Наибольшее число равно", largest)
