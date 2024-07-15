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
