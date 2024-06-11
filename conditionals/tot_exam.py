# 1

# year = int(input())

# if year % 100 == 0:
#     print("YES")
# else:
#     print("NO")

# 2

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# colour1 = (x1 + y1) % 2

# colour2 = (x2 +y2) % 2

# if colour1 == colour2:
#   print("YES")
# else:
#   print("NO")

# 3

# age = int(input())
# sex = input()

# if 10 <= age <= 15 and sex == "f":
#     print("YES")
# else:
#     print("NO")

# 4

# numeral = int(input())

# if numeral == 1:
#     print("I")
# elif numeral == 2:
#     print("II")
# elif numeral == 3:
#     print("III")
# elif numeral == 4:
#     print("IV")
# elif numeral == 5:
#     print("V")
# elif numeral == 6:
#     print("VI")
# elif numeral == 7:
#     print("VII")
# elif numeral == 8:
#     print("VIII")
# elif numeral == 9:
#     print("IX")
# elif numeral == 10:
#     print("X")
# else:
#     print("ошибка")

# 5

# numeral = int(input())

# if numeral % 2 != 0:
#     print("YES")
# elif 2 <= numeral <= 5 and numeral % 2 == 0:
#     print("NO")
# elif 6 <= numeral <= 20 and numeral % 2 == 0:
#     print("YES")
# else:
#     print("NO")

# 6 🌶️🐘

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())


# if a2 - a1 == b2 - b1 or a2 - a1 == b1 - b2:
#     print("YES")
# else:
#     print("NO")


# 7 🐎
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

# horizontal = a2 - a1
# vertical = b2 - b1

# if (
#     (horizontal == 1 and vertical == 2)
#     or (horizontal == 2 and vertical == 1)
#     or (horizontal == -1 and vertical == -2)
#     or (horizontal == -2 and vertical == -1)
#     or (horizontal == 1 and vertical == -2)
#     or (horizontal == 2 and vertical == -1)
#     or (horizontal == -1 and vertical == 2)
#     or (horizontal == -2 and vertical == 1)
# ):
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# difference_product = (x1 - x2) * (y1 - y2)

# if difference_product == 2 or difference_product == -2:
#     print("YES")
# else:
#     print("NO")

# 8 👑

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a == c or a == c + 1 or a == c - 1) and (b == d or b == d + 1 or b == d - 1):
    print("YES")
elif c - a == d - b or c - a == b - d:
    print("YES")
elif a == c or b == d:
    print("YES")
else:
    print("NO")
