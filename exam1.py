# 1
s = 13
k = -5
d = s + 2  # 15
s = d  # 15
k = 2 * s  # 30

# print(s + k + d)
# 15 +30+ 15 = 60


# 2

a = 17 // (23 % 7)  # 23 % 7  = 2 ********* 17// 2 = 8
b = 34 % a * 5 - 29 % 4 * 3  # 10 - 3 =7
# print(a * b) # 7*8 = 56

# Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*).
# h = 4, l = 17


h = 4
l = 17

# print("*" * l)
# print("*", " " * (l - 2), "*", sep="")
# print("*", " " * (l - 2), "*", sep="")
# print("*" * l)

# 3
"""
a = int(input())
b = int(input())
"""


first_result = (a + b) ** 2
second_result = a**2 + b**2
# print("Квадрат суммы", str(a), "и", str(b), "равен", first_result)
# print("Сумма квадратов", str(a), "и", str(b), "равна", second_result)

# 4 (9,29,7,27)
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = a**b + c**d
print(result)
"""

# 5 (1+11+111 = 123)

n = int(input())
nn = int(str(n) * 2)
nnn = int(str(n) * 3)

result = n + nn + nnn

print(result)
