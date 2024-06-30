# Ex 1 💚

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)


# 123
# 345

# 1 3
# 1 4
# 1 5
# 2 3
# 2 4
# 2 5
# 3 3
# 3 4
# 3 5

# Ex 2 💚

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end="")


# # 1 2 3
# # 3 4


# # 1 3 + 4

# # 1 4 + 5

# # 2 3 5
# # 2 4 6
# # 3 3 6
# # 3 4 7

# Ex 3 💚

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)


# 99 100 101

# c0 i99 t99  => c1 t9
# while 9>0 => c2 t0
# while 0>0 ----------------
# for i100 t100 100>0 => c3 t10
# while t10>0 c4 => t10//10 = t1
# while t1>0 => c5 t1//10 =t0
# while 0>0 _ _ _ _ _ _ _ _
# for i=101, t101 101>0 => c6 t101//10 = t10
# while t10>0 => c7 t10//10 =t1
# while t1>0 => c8 t1//10 = t0
# while t0>0 --------------
# for...----------
# print 8

# T1 TABLE 🧱

# Number n (n <= 9). Write a program that prints a table of size n×3 consisting of a given number (the numbers are separated by one space).

# n = int(input())

# for i in range(n):
#     for j in range(3):
#         print(n, end=" ")
#     print()

# T2 TABLE 2 📗

# Number n (n <= 9). Write a program that prints a table of size n X 5, where in the line i there is number i

# n = int(input())

# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=" ")
#     print()

# 3

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3

# T3 TABLE 3 📕

# Number n (n <= 9). Write a program that prints a table of sum from 1 to n (incl)
# We mean the addition table from 1 to 9

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, "+", j, "=", i + j)
#     print()

# 1

# 1 + 1 = 2
# 1 + 2 = 3
# 1 + 3 = 4
# 1 + 4 = 5
# 1 + 5 = 6
# 1 + 6 = 7
# 1 + 7 = 8
# 1 + 8 = 9
# 1 + 9 = 10

# T5 ⭐️ Star Triangle 🌶️🌶️

# Given an odd ( %2 != 0) natural number n.

# Write a program that prints an isosceles star triangle with base n as shown in the example:

# n = int(input())

# for i in range(n // 2 + 2):
#     for j in range(i):
#         print("*", end="")
#     print()
# for l in range(n // 2 + 1, 0, -1):
#     for k in range(l - 1):
#         print("*", end="")
#     print()

# *
# **
# ***
# **
# *

# T6 Numerical triangle 🍕

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
