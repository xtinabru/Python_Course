# ex 1 🦹‍♂️

# Cisco has been told that Zoom's speed is n and Flash's speed is k.
# If Zoom is faster than Flash, you should output ‘NO’, and if Flash is faster than Zoom, you should output ‘YES’. In case their speeds are equal, you should output ‘Don't know’.

# n = int(input())

# k = int(input())

# if n > k:
#     print("NO")
# elif n < k:
#     print("YES")
# else:
#     print("Don't know")

# ex 2 📐
# Whether the triangle is equilateral, isosceles, or different-sided

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print("Равносторонний")
# elif a == b or b == c or a == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# ex 3 Median value 🤖

# a, b, c = int(input()), int(input()), int(input())

# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# else:
#     print(c)

# ex 4 Quantity of days 📅

# month = int(input())

# if month == 2:
#   print("28")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#   print("30")
# else:
#   print("31")

# ex 5 Weight 🏋🏻

# weight = int(input())

# if weight < 60:
#     print("Легкий вес")
# elif weight < 64:
#     print("Первый полусредний вес")
# else:
#     print("Полусредний вес")

# ex 6 Calculator 🧮🌶️

a, b, c = int(input()), int(input()), (input())

if c != "+" and c != "-" and c != "*" and c != "/":
    print("Неверная операция")
else:
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/" and b != 0:
        print(a / b)
    elif c == "/" and b == 0:
        print("На ноль делить нельзя!")
