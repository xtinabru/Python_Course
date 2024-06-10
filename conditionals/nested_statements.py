# Nested and cascaded it 🪺

# if first_condition:
#     print()
# else:
#     if second_condition:
#         print()
#     else:
#         if third_condition:
#             print()


# THAT WAS DONE🍀 XY:

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

# NOW BECOMES 🪶

# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print("1st quarter")
#     else:
#         print("4 square")
# else:
#     if y > 0:
#         print("2 square")
#     else:
#         print("3 square")

# ex 1 100 to 5 💯

# grade = int(input("Put your points: "))

# if grade >= 90:
#     print(5)
# elif grade >= 80:
#     print(4)
# elif grade >= 70:
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)

# NOTA BENE ❗️
# else - is not necessary:

# ex 2 Traffic light🚦

# traffic_light_signal = input("Enter the signal: ")

# if traffic_light_signal == "red":
#     print("STOP")
# elif traffic_light_signal == "yellow":
#     print("WAIT")
# elif traffic_light_signal == "green":
#     print("GO")

# ex 3 Numbers 🔢
# Three integers are given. Determine how many of them match.
# The program should output one of the numbers:

# 1 🌸
# a, b, c = int(input()), int(input()), int(input())

# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)

# 2 🌸🌸
# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)

# 3 🌸🌸🌸

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)
