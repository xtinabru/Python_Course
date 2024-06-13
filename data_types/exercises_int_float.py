# ex 1 The biggest and the smallest 🪐
# Find the biggest and the smallest numbers

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

# biggest = max(a, b, c, d, e)
# smallest = min(a, b, c, d, e)

# print("Наименьшее число =", smallest)
# print("Наибольшее число =", biggest)

# ex 2 Sorting 3️⃣🌶️
# Write a program that orders three numbers from largest to smallest.

# a, b, c = int(input()), int(input()), int(input())

# biggest = max(a, b, c)
# smallest = min(a, b, c)
# mediun = (a + b + c) - biggest - smallest

# print(biggest)
# print(mediun)
# print(smallest)

# ex 3 Interesting number 🌄
# The number is interesting if:
#  the difference between the max and the min digit = median

# a = int(input())

# first_digit = a // 100
# second_digit = (a // 10) % 10
# third_digit = a % 10

# biggest = max(first_digit, second_digit, third_digit)
# smallest = min(first_digit, second_digit, third_digit)
# medium = (first_digit + second_digit + third_digit) - biggest - smallest

# if (biggest - smallest) == medium:
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# ex 4 Absolute value / modulus 🎁

# a1, a2, a3, a4, a5 = (
#     float(input()),
#     float(input()),
#     float(input()),
#     float(input()),
#     float(input()),
# )
# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

# ex 5 Manhattan distance 🌇
# the distance between two points is equal to the sum of the moduli of the differences of their coordinates.

# p1, p2, q1, q2 = float(input()), float(input()), float(input()), float(input())

# distance = (abs(p1 - q1)) + (abs(p2 - q2))
# print(int(distance))
