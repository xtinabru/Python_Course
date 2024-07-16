# Ex 1 🔹🔹🔹

# names = []
# names.append("Chromatica")
# print(names)

# Ex 2 🔹🔹🔹

# numbers = [4, 2, 8, 6, 5]
# numbers.append(7)
# numbers.append(1)
# print(numbers) # [4, 2, 8, 6, 5, 7, 1]

# Ex 3 🔹🔹🔹

# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers) #[4, 2, 1, 2, 3, 7, 17, 777]

# Ex 4 🔹🔹🔹

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors) #

# Task 1 🔵 🌶️

# Complete the given code so that it:

# Displayed the length of the list;
# Displayed the last element of the list;
# Displayed the list in reverse order (remember the slices);
# Printed YES if the list contains the numbers 5 and 17, and NO otherwise;
# Displayed a list with the first and last elements removed.

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])

# if 5 and 17 in numbers:
#   print("YES")
# else:
#   print("NO")

# print(numbers[1:-1])

# Task 2 🔵
# The input to the program is a natural number n, and then n strings. Write a program that creates a list from the given strings and displays it

# n = int(input())

# string_list = []

# for _ in range(n):
#     string = input()
#     string_list.append(string)

# print(string_list)

# Task 3  ABC🔵

# our_list = []

# for i in range(97, 123):
#     our_list.append(chr(i) * (i - 96))

# print(our_list)

# Task 4  A list of cubes🔵
# The program is given a natural number n as input, and then n integers. Write a program that creates a list of their cubes from the given numbers.

# n = int(input())

# list_of_cubes = []

# for _ in range(n):
#     number = int(input())
#     list_of_cubes.append(number**3)

# print(list_of_cubes)

# Task 5 List of denominators🔵

# n = int(input())

# denom_list = []

# for i in range(1, n + 1):
#     if n % i == 0:
#         denom_list.append(i)
# print(denom_list)

# Task 6 Sum of two 🔵

# n = int(input())

# numbers = []

# for _ in range(n):
#     number = int(input())
#     numbers.append(number)

# sum_list = []

# for i in range(n - 1):
#     sum_list.append(numbers[i] + numbers[i + 1])

# print(sum_list)

# or

# Считываем количество чисел
# n = int(input())

# # Считываем все числа и добавляем их в список
# numbers = [int(input()) for _ in range(n)]

# # Создаем список сумм соседних чисел
# sum_list = [numbers[i] + numbers[i + 1] for i in range(n - 1)]

# # Выводим результат
# print(sum_list)

# Task 7 Delete odd indexes 🔵

# n = int(input())
# numbers = []

# for i in range(n):
#     number = int(input())
#     numbers.append(number)

# i = 1
# while i < len(numbers):
#     del numbers[i]
#     i += 1

# print(numbers)

# or

# n = int(input())
# seq = []

# for _ in range(n):
#     cur = int(input())
#     seq.append(cur)

# print(seq[::2])

# Task 8 k-th letter of the word 🌶️🌶️ 🔵

# n = int(input())
# strings = [input() for _ in range(n)]

# k = int(input())
# result = ""

# for string in strings:
#     if len(string) >= k:
#         result += string[k - 1]

# print(result)

# Task 9. Characters of all lines🔵

# n = int(input())
# strings = [input() for _ in range(n)]
# result = []

# for string in strings:
#     for char in string:
#         result.append(char)

# print(result)

# or

# n = int(input())
# seq = []

# for _ in range(n):
#     s = input()
#     seq.extend(s)

# print(seq)
