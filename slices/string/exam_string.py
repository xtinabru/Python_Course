# Question 1  🐇

# The first index in a string value is
# 0

# Question 2  ⚪️

# The last index in a string value is
# line length - 1

# Question 3  ⚪️

# If you try to use an index that is outside the range of the string value, then
# an IndexError will occur

# Question 4  ⚪️

# Which operator determines whether one string value is contained within another?
# in

# Question 5  ⚪️

# Which string method returns the index of the first occurrence of a substring in a string?
# find()

# Question 6 ⚪️

# Which string method returns a copy of a string value with all leading whitespace characters removed?
# lstrip()

# Question 7 ⚪️

# Which string method returns a copy of a string value with all leading and trailing whitespace characters removed?
# strip()

# Question 8 ⚪️

# Which string method returns true if the string value contains only letters and has at least one character?
# isalpha()

# Question 9 ⚪️

# Which string method returns true if the string value contains only numbers and has at least one character?
# isdigit()

# Question 10 ⚪️

# name = 'джо'
# print(name.lower())
# print(name.upper())
# print(name)

# ➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿

# TASK 1 🟣

# The program outputs the length of the string s.

# s = "Python rocks!"
# print(len(s))

# TASK 2 🟣

# Complete the code below so that the program outputs
# the fourth character of the string, s.

# s = "Python rocks!"
# print(s[3:4])

# # or

# s = 'Python rocks!'
# res = s[3]

# print(res)

# TASK 3 🟣

# Complete the code below so that the program outputs the 2nd through 5th characters of string s.

# s = "Python rocks!"
# print(s[1:5])

# TASK 4 🟣

# Complete the code below so that the program outputs the string s without leading or trailing whitespace characters.

# s = "    Python rocks!     "
# print(s.strip())

# TASK 5 🟣

# Complete the code below so that the program outputs the string s in capital letters (uppercase).

# s = "Python rocks!"
# print(s.upper())

# TASK 6 🟣

# Complete the code below so that the output of the program is the string s in which the “o” character is replaced with the “@” character

# s = "Python rocks!"
# print(s.replace("o", "@"))

# TASK 7 🟣 EACH THIRD

#  A line of text is given as input to the program. Write a program that removes from it all characters with indices divisible by 3, that is, characters with indices 0, 3, 6, ...

# text = str(input())

# result = ""

# for i in range(len(text)):
#     if i % 3 != 0:
#         result += text[i]

# print(result)

# or

# s = input()
# n = len(s)

# new_s = ""
# for i in range(n):
#     if i % 3 == 0:
#         continue

#     new_s += s[i]

# print(new_s)

# TASK 8 🟣

# text = input()
# result = text.replace('1', 'one')

# print(result)

# TASK 9 🟣

# text = input()
# result = text.replace("@", "")

# print(result)

# TASK 10 🟣

# text = input()

# first_index = text.find("f")

# if first_index == -1:
#     print(-2)

# else:
#     second_index = text.find("f", first_index + 1)
#     if second_index == -1:
#         print(-1)
#     else:
#         print(second_index)

# TASK 11 🟣

# text = input()

# first_h = text.find("h")
# last_h = text.rfind("h")

# sub_to_reverse = text[first_h + 1 : last_h]

# reversed_str = sub_to_reverse[::-1]

# result = text[first_h + 1] + reversed_str + text[last_h:]
# print(result)
