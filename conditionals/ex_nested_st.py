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

# a, b, c = int(input()), int(input()), (input())

# if c != "+" and c != "-" and c != "*" and c != "/":
#     print("Неверная операция")
# else:
#     if c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/" and b != 0:
#         print(a / b)
#     elif c == "/" and b == 0:
#         print("На ноль делить нельзя!")

# ex 7 Colourful 🍭

# first_colour, second_colour = input(), input()

# if (first_colour == "красный" and second_colour == "синий") or (
#     first_colour == "синий" and second_colour == "красный"
# ):
#     print("фиолетовый")
# else:
#     if (
#         first_colour != "красный"
#         and first_colour != "синий"
#         and first_colour != "желтый"
#     ) or (
#         second_colour != "красный"
#         and second_colour != "синий"
#         and second_colour != "желтый"
#     ):
#         print("ошибка цвета")
#     else:
#         if (first_colour == "красный" and second_colour == "желтый") or (
#             first_colour == "желтый" and second_colour == "красный"
#         ):
#             print("оранжевый")
#         elif (first_colour == "синий" and second_colour == "желтый") or (
#             first_colour == "желтый" and second_colour == "синий"
#         ):
#             print("зеленый")
#         elif first_colour == second_colour or second_colour == first_colour:
#             print(first_colour or second_colour)
#         else:
#             print("ошибка цвета")

# a, b = input(), input()🌈

# if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
#     print('зеленый')
# elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
#     print(a)
# else:
#     print('ошибка цвета')


# ex 8 Roulet🌶️
# my_num = int(input())
# if my_num == 0:
#     print("зеленый")
# else:
#     if 1 <= my_num <= 10 and my_num % 2 == 0:
#         print("черный")
#     elif 1 <= my_num < 10 and my_num % 2 != 0:
#         print("красный")
#     elif 11 <= my_num <= 18 and my_num % 2 == 0:
#         print("красный")
#     elif 11 <= my_num <= 18 and my_num % 2 != 0:
#         print("черный")
#     elif 19 <= my_num <= 28 and my_num % 2 == 0:
#         print("черный")
#     elif 19 <= my_num < 28 and my_num % 2 != 0:
#         print("красный")
#     elif 29 <= my_num <= 36 and my_num % 2 == 0:
#         print("красный")
#     elif 29 <= my_num <= 36 and my_num % 2 != 0:
#         print("черный")
#     else:
#         if my_num > 36 or my_num < 1:
#             print("ошибка ввода")

# ex 9  TWO LINES 🌶️🌶️ 🐈
# a, b, c, d = int(input()), int(input()), int(input()), int(input())

# if (a < c and b < d) and b != c and b > c:
#     print(c, b)
# elif (a < c and b < d) and b < c:
#     print("пустое множество")
# elif (a < c and b > d) and b != c:
#     print(c, d)
# elif (a < c and b == d) and b != c:
#     print(c, b)
# elif (a > c and b < d) or (a > c and b == d):
#     print(a, b)
# elif c < a < b < d and c < a:
#     print(a, d)
# elif c < d < a < b:
#     print("пустое множество")
# elif a > c and b > d and a < d:
#     print(a, d)
# elif a > c and b > d and a == d:
#     print(a)
# elif a == c and d > b:
#     print(a, b)
# elif a == c and d < b:
#     print(a, d)
# elif a == c and b == d:
#     print(a, b)
# elif b == c:
#     print(b)


# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 < a2:
#     amax = a2
# else:
#     amax = a1
# if b1 < b2:
#     bmin = b1
# else:
#     bmin = b2
# if amax > bmin:
#     print('пустое множество')
# elif amax == bmin:
#     print(amax)
# else:
#     print(amax, bmin)
