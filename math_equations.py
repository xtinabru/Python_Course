#  1 🍎

# Найдите все пары натуральных чисел (и их количество), являющихся решением уравнения 12x + 13y = 777

# As  x, y  = N
# x <= 64, y <= 59  ------->  as if x = 65, 12 * 65 = 780 which is more than 777
# so x <= 64


# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print("x = ", x, "y = ", y)
# print(total)


# 2 🍎

# Найдите все тройки натуральных чисел (и их количество), являющихся решением уравнения x** 2 + y**2 + z**2 = 2020

# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x**2 + y**2 + z**2 == 2020:
#                 total += 1
#                 print("x =", x, "y =", y, "z =", z)
# print("Общее количество натуральных решений =", total)

# 3 🍎

# Solve the equation 28n + 30k + 31m = 365

# total = 0
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             if 28 * x + 30 * y + 31 * z == 365:
#                 total += 1
#                 print("x =", x, "y =", y, "z =", z)


# 4 🍎

# There is 100 r.

# total = 0

# for b in range(101):
#     for k in range(101):
#         for t in range(101):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 total += 1
#                 print("b =", b, "k =", k, "t =", t)

# print("Total solutions:", total)


# 5 🍎 Euler's Sum of Powers Conjecture 🌶️🌶️
