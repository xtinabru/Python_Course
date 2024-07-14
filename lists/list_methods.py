# List methods🩷

# Adding elements 📍📍📍

# Method append() 📍
# is used to add in the end of the list

# Example:

# numbers = [1, 1, 2, 3, 5, 8, 13]

# numbers.append(21)
# numbers.append(34)

# print(numbers) ### [1, 1, 2, 3, 5, 8, 13, 21, 34]

# ❗️ Please note that in order to use the append() method, the list must be created (it may be empty). Example:

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# print(numbers) [1, 2, 3]

# Method extend() 📍
# You can also extend a list with another list by calling the extend() method.

# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]

# numbers.extend(odds)
# print(numbers) ### [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

# ❗️ The append() method appends the entire string 'python' to the list, and the extend() method splits the string 'python' into the characters 'p', 'y', 't', 'h', 'o', 'n' and their adds as list items

# Deleting elements 📍📍📍

# You can use the del operator to delete elements of a list at a specific index.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[5]

# print(numbers)  # [1, 2, 3, 4, 5, 7, 8, 9]

# ❗️ Pay attention to the delete syntax, as it is different from a normal method call. When deleting elements, you do not need to pass an argument inside parentheses.

# The del operator also works with slices: we can remove an entire range of elements from a list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[2:7]

# print(numbers) # [1, 2, 8, 9]

# all evens

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[::2]

# print(numbers) ### [2, 4, 6, 8]
