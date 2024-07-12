# 🔅🔅🔅
# The classical task of sorting (ordering) a certain sequence requires storing all the data in computer memory. Unfortunately, without saving, it is impossible to sort them. And here a data structure comes to the rescue, which in most programming languages ​​is called an array. In Python it's called a list.

# Data structure is a software unit that allows you to store and process a variety of similar and/or logically related data.
# A list is a sequence of elements, numbered from 0, like characters in a string.

# 🔆 List creation

# numbers = [2, 4, 6, 8, 10]
# The list numbers consists of 5 elements, and each of them is an integer.

# numbers[0] == 2;
# numbers[1] == 4;
# numbers[2] == 6;
# numbers[3] == 8;
# numbers[4] == 10.


# languages = ['Python', 'C#', 'C++', 'Java']
# The list of languages ​​consists of 4 elements, each of which is a string.

# languages[0] == 'Python';
# languages[1] == 'C#';
# languages[2] == 'C++';
# languages[3] == 'Java'.

# ❗️ The values ​​enclosed in square brackets and separated by commas are called list elements.

# ❗️ The list can contain values ​​of different data types:

# info = ['Cris', 1999, 50]

# 🔆 Empty list

# There are two ways to create an empty list:

# Use empty square brackets [];
# Use a built-in function called list.
# The following two lines of code create an empty list:

# mylist = [] # empty list
# mylist = list() # also an empty list

# 🔆 List output

# To print the entire list, you can use the print() function:

# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']
# print(numbers)
# print(languages)

# 🔆 Function list()

# In addition to creating an empty list, it can CONVERT some types of objects into lists.

# For example, we know that the range() function produces a sequence of integers in a given range. To convert this sequence into a list, we write the following code:

# numbers = list(range(5))

# even_numbers = list(range(0, 10, 2))
# list contains even numbers 0, 2, 4, 6, 8

# odd_numbers = list(range(1, 10, 2))
# list contains odd numbers 1, 3, 5, 7, 9


# s = "abcde"
# chars = list(s)

# print(chars)

# ❗️ Array elements always have the same data type and are located in the computer memory as a continuous block, while list elements can be scattered throughout memory as desired and can have different data types.

# ❗️ Please note that when displaying the contents of a list using the print() function, all string elements of the list are surrounded by single quotes. If you want to output in double quotes, you need to write the output code yourself.
