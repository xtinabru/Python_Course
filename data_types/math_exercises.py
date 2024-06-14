# Ex 1 Euclidean distance 🧡

# from math import pow, sqrt

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())


# result = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
# print(result)

# Ex 2 🩷
# Write a program to determine the area of ​​a circle and the circumference of a circle at a given radius

# from math import pow, pi

# R = float(input())

# S = pi * (pow(R, 2))
# C = 2 * pi * R

# print(S)
# print(C)

# Ex 3 💛
# Average values

# 1) arithmetic mean of numbers a and b:
# (a + b)/2

# 2) geometric mean of numbers a and b:
# sqrt of a * b

# 3) harmonic mean of numbers a and b:
#  2 * a * b / (a + b)

# 4) mean square of numbers a and b:
# sqrt of (a**2 + b**2)/2

# from math import pow, sqrt

# a = float(input())
# b = float(input())

# arithm = (a + b) / 2
# geometr = sqrt(a * b)
# harm = (2 * a * b) / (a + b)
# sqr = sqrt((a**2 + b**2) / 2)

# print(arithm)
# print(geometr)
# print(harm)
# print(sqr)

# Ex 4 💚
# Trigonometric expression

# from math import sin, cos, tan, radians

# x = float(input())
# x_rad = radians(x)

# result = sin(x_rad) + cos(x_rad) + tan(x_rad) ** 2
# print(result)

# Ex 5 💙 FLOOR AND CEIL

# from math import floor, ceil

# x = float(input())

# print(floor(x) + ceil(x))

# Ex 6 🩵 Quadratic equation 🌶️🌶️

# from math import sqrt

# a = float(input())
# b = float(input())
# c = float(input())

# D = b**2 - 4 * a * c

# if D < 0:
#     print("Нет корней")
# elif D == 0:
#     r = -b / (2 * a)
#     print(r)
# else:
#     r1 = (-b - sqrt(D)) / 2 * a
#     r2 = (-b + sqrt(D)) / 2 * a
#     print(r1)
#     print(r2)

#  Ex 7 Regular polygon 💜

from math import tan, pi

n = float(input())
a = float(input())

S = (n * a**2) / (4 * (tan(pi / n)))
print(S)
