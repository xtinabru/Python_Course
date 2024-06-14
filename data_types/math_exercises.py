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

from math import pow, pi

R = float(input())


S = pi * (pow(R, 2))
C = 2 * pi * R

print(S)
print(C)
