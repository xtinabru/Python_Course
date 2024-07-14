# List basics 🤍

# Function len() ◽️

# In order to calculate the length of a list, we use the built-in function len() (from the word length - length).

# Example^

# numbers = [2, 4, 6, 8, 10]
# languages = ["Python", "C#", "C++", "Java"]

# print(len(numbers))
# print(len(languages))
# print(len(["Python", "C++", "Java"]))

# Operator in ◽️

# The in operator allows you to check whether a list contains an element.

# numbers = [2, 4, 6, 8, 10]

# if 2 in numbers:
#     print("There is number 2")
# else:
#     print("There is no 2")

# ◽️ we can use in with NOT:

# numbers = [2, 4, 6, 8, 10]

# if 0 not in numbers:
#     print("There is no 0")

# ◽️ Indexation

# To index lists in Python, square brackets [] are used, which indicate the index (number) of the desired element in the list:

# numbers = [2, 4, 6, 8, 10] # 0,1,2,3,4
# or
# 10,8,6,4,2 => -1,-2,-3,-4,-5
# print(numbers[17]) ### IndexError: index out of range

# ◽️ Slices

# numbers = [2, 4, 6, 8, 10]
# print(numbers[1:3])  # [4, 6]
# print(numbers[2:5])  # [6, 8, 10]

# ◽️ numbers[x:y]
# First  - the beginning, second - stop(not included)

# When using slices with lists, we can also omit the second parameter in the numbers[x:] slice (but put a colon), then the slice is taken to the end of the list. Similarly, if you omit the first parameter numbers[:y], you can take a slice from the beginning of the list.

# The numbers[:] slice returns a copy of the original list.

# ◽️ Using slicers to change elements within a given range

# fruits = ["apple", "apricot", "banana", "cherry", "kiwi", "lemon", "mango"]
# fruits[2:5] = ["банан", "вишня", "киви"]
# print(fruits)

# ◽️ Concatenation operation + and multiplication by number *

# print([1, 2, 3, 4] + [5, 6, 7, 8]) # [1, 2, 3, 4, 5, 6, 7, 8]
# print([7, 8] * 3) # [7, 8, 7, 8, 7, 8]
# print([0] * 10) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# a = [1, 2, 3, 4]
# b = [7, 8]
# a += b
# b *= 5

# print(a) # [1, 2, 3, 4, 7, 8]
# print(b) # [7, 8, 7, 8, 7, 8, 7, 8, 7, 8]

# ◽️ Functions sum(), min(), max()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("The sum =", sum(numbers))

# numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
# print("Min number =", min(numbers))
# print("Max number =", max(numbers))

# ◽️ Difference between lists and strings

# ❕ a very important difference: strings are immutable objects, and lists are mutable.

# ❕❕❕
# s = "abcdefg"
# s[1] = "x"  # object does not support item assignment

# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[1] = 101
# print(numbers) # [1, 101, 3, 4, 5, 6, 7]
