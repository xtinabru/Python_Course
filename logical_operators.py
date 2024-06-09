# logical operators 🐍

# and - logical multiplication
# or - logical addition
# not - logical negotion

""" 💚 ex1 AND 💚"""

# There are 2 conditions
# TWO CONDITIONS AT THE SAME TIME

# age = int(input("How old are you?: "))
# grade = int(input("Your grade? "))
# if age >= 12 and grade >= 7:
#     print("Access is allowed")
# else:
#     print("Access is denied")


# this can add several conditions 🙃

# age = int(input("How old are you? "))
# grade = int(input("Your grade? "))
# city = input("Your city? ")

# if age >= 12 and grade >= 7 and city == "Oulu":
#     print("Access is allowed")
# else:
#     print("Access is denied")

""" 💚 ex2 OR 💚"""
# at least one condition

# city = input("Your city?: ")
# if city  == "Oulu" or city == "Helsingi" or city == "Tampere":
#     print("Access is allowed")
# else:
#     print("Access is denied")

""" 💚ex3 BOTH 💚"""
# age = int(input("How old are you?: "))
# grade = int(input("Your grade? "))
# city = input("Your city? ")

# if age >= 12 and grade >= 7 and (city == "Oulu" or city == "Helsingi"):
#     print("Access is allowed")
# else:
#     print("Access is denied")

""" 💚ex4 NOT 💚"""

# INVERTION!!!

# age = int(input("How old are you?"))
# if not (age < 12):
#     print("Access is allowed")
# else:
#     print("Access is denied")

# THE SAME:

# age = int(input("How old are you?"))
# if age >= 12:
#     print("Access is allowed")
# else:
#     print("Access is denied")

# 🟢
# if age >= 7 and age <= 9:
# The same:

# if 7 <= age <= 9: 👌🏻

# 🟢
# print(5 > 100 and 10 > 0) - FALSE
# print(10 > 0 or 5 > 100) - TRUE

# OR можно сравнить со сложением, где максимальное значение - 1. Рассмотрим 4 возможных случая.

# 1)Если первое утверждение истинно, а второе ложно, то результат - 1 + 0 = 1 (истина).

# 2)Если же, наоборот, первое ложно, а второе - истинно, то результат - 0 + 1 = 1 (истина).

# 3)Если оба верны, то результат - 1 + 1 = 1 (не забываем про максимальное значение), то есть снова истина.

# 4)Если оба неверны, то результат - 0 + 0 = 0 (ложь).

# AND сравнимо с умножением.

# 1)Если первое утверждение истинно, а второе ложно, то результат - 1 * 0 = 0 (ложь).

# 2)Если же, наоборот, первое ложно, а второе - истинно, то результат - 0 * 1 = 0 (тоже ложь).

# 3)Если оба неверны, то результат - 0 * 0 = 0 (опять ложь).

# 4)Если оба верны, то результат - 1 * 1 = 1 (истина).
