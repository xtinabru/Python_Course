# Ex 1 🔸

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# print(s[7])

# Ex 2 🔸

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."

# print(s[-10])

# Ex 3 🔸

# input_string = input()

# for i in range(0, len(input_string), 2):
#     print(input_string[i])

# Ex 4 🔸

# input_string = input()

# for i in range(-1, -len(input_string) - 1, -1):
#     print(input_string[i])

# 0
# l
# l
# e
# h

# Ex 5 🔸# ФИО

# input_name = input()
# input_surname = input()
# patr_name = input()

# print(input_surname[0], input_name[0], patr_name[0], sep="")

# Ex 6 Number I 🔸#

# num = input()

# # 2514
# total = 0
# for i in num: #---------------------------------------!!!!!
#     total += int(i)

# print(total)

# OR

# s = input()
# sum = 0
# for i in range(0, len(s)):
#     sum += int(s[i])
# print(sum)

# OR

# FROM THE PREVIOUS

# n = int(input())
# total = 0
# while n:
#     last_digit = n % 10
#     total += last_digit
#     n //= 10
# print(total)

# Ex 7 Number II🔸

# x = input()

# contains_digit = False

# for i in x:
#   if i.isdigit():
#     contains_digit = True
#     break

# if contains_digit:
#   print("Цифра")
# else:
#   print("Цифр нет")

# Ex 8 How many times? 🔸

# x = input()

# total_plus = 0
# total_mult = 0

# for i in x:
#     if i == "+":
#         total_plus += 1
#     if i == "*":
#         total_mult += 1

# print("Символ + встречается", total_plus, "раз")
# print("Символ * встречается", total_mult, "раз")

# Ex 9 Neighbourhood ? 🔸

# x = input()

# count = 0  # счетчик для одинаковых соседних символов

# for i in range(1, len(x)):
#     if x[i] == x[i - 1]:
#         count += 1

# print(count)

# Ex 10 Гласные и согласные 🔸

# x = input()

# vowels = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
# consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

# count_vow = 0
# count_cons = 0

# for i in x:
#     if i in vowels:
#         count_vow += 1
#     elif i in consonants:
#         count_cons += 1

# print("Количество гласных букв равно", count_vow)
# print("Количество согласных букв равно", count_cons)

# Ex 11 Decimal to Binary

# dec_num = int(input())  # 5 101

# binary_num = ""

# while dec_num > 0:
#     binary_num = str(dec_num % 2) + binary_num
#     dec_num = dec_num // 2
# if binary_num == "":
#     binary_num = "0"

# print(binary_num)
