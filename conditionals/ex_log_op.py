# ex.1 🍀
# num = int(input())

# if 100 <= num <= 999:
#     print("The number is three digit number")

# ex.2  🍀 Whether 3 digits are different or not

# num = int(input())
# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# if a != b and a != c and b != c:
#     print("Digits are diffirent")
# else:
#     print("They are not different")

# ex.3 🍀 XY

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(" 1st quarter")
# if x < 0 and y > 0:
#     print("2 square")
# if x < 0 and y < 0:
#     print("3 square")
# if x > 0 and y < 0:
#     print("4 square")

# ❌
# if my_city == 'Oulu' or 'Helsinki' or 'Tampere':
#    print('I live in Finland')

# ✔️
# if my_city == 'Oulu' or my_city == 'Helsinki' or my_city == 'Tampere':
#    print('I live in Finland)

#
# ex 4 🎲 What number wins?

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print("Number", num1, "won")
# else:
#     print("Number", num2, "won")

# ex 5 🍀
# What will show if we enter 7

# a = int(input())

# if a >= 2 and a <= 17:  # true
#     b = 3
#     p = a * a + b * b  # 58
# else:
#     b = 5

# p = (a + b) * (a + b)
# print(p)

# ex 6 🍀 BELONGING

# x = int(input())

# if -1 < x < 17:
#     print("Belongs")
# else:
#     print("Doesn't belong")

# ex 7 🍀 BELONGING
# x = int(input())

# if x <= -3 or x >= 7:
#     print("Belongs")
# else:
#     print("Doesn't belong")

# ex 8 🍀 BELONGING

# x = int(input())

# if -30 < x <= -2 or 7 < x <= 25:
#     print("Belongs")
# else:
#     print("Doesn't belong")


# ex 9 BEAUTIFUL NUMBER 🌶️

# num = int(input())

# if 999 < num <= 9999 and (num % 7 == 0 or num % 17 == 0):
#     print("YES")
# else:
#     print("NO")

# ex 10 Triangle inequality🌶️

# a, b, c = int(input()), int(input()), int(input())

# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")

# ex 11 Leap Year 📅

# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Yes")
# else:
#     print("No")

# ex 12 ♜♜♜

# a, b, c, d = int(input()), int(input()), int(input()), int(input())

# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")

# ex 13 ♜ 🌶️
# a, b, c, d = int(input()), int(input()), int(input()), int(input())

# if (a == c + 1 or a == c - 1 or a == c) and (b == d + 1 or b == d - 1 or b == d):
#     print("YES")
# else:
#     print("NO")
