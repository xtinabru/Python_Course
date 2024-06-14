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

# Ex 2 💛
# Average values

# 1) arithmetic mean of numbers a and b:
# (a + b)/2

# 2) geometric mean of numbers a and b:
# sqrt of a * b

# 3) harmonic mean of numbers a and b:
#  2 * a * b / (a + b)

# 4) mean square of numbers a and b:
# sqrt of (a**2 + b**2)/2

from math import pow, sqrt

a = float(input())
b = float(input())

arithm = (a + b) / 2
geometr = sqrt(a * b)
harm = (2 * a * b) / (a + b)
sqr = sqrt((a**2 + b**2) / 2)

print(arithm)
print(geometr)
print(harm)
print(sqr)
