# Code review 💌


# Code review - checking the source code of a program in order to detect and correct errors and inaccuracies that went unnoticed during initial development.

# During the code review process the following can be corrected:

# 🖍 factual errors;
# 🖍 code performance;
# 🖍 code readability and code formatting errors.

#  🔅
# The purpose of code review is to improve the quality of the program code and improve the programmer's skills.

# ❗️ Code performance

# WAS

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# 1 ❗️❗️❗️prodictivity

# : Несложно понять, что перебирать все числа от 2 до num - 1 не имеет смысла. Достаточно проверить числа от 2 до num // 2 + 1:

# num = int(input())
# flag = True

# for i in range(2, num // 2 + 1):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# 2 ❗️❗️❗️prodictivity

#  Правую границу num // 2 + 1 проверки можно улучшить, если заметить, что у любого составного числа есть делитель (отличный от 1), не превосходящий квадратного корня из числа. Таким образом, имеет смысл перебирать делители от 2 до корня из n + 1.

# num = int(input())
# flag = True

# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# Если программе на вход подается простое число num = 1934234249, то она будет работать примерно 0.066 секунд. По сути мы улучшили время работы программы в 4000 раз! 😎


# 3 ❗️❗️❗️prodictivity

# Предыдущие оптимизации касались случая, когда проверяемое число является простым. В случае если число является составным и мы нашли его первый делитель (отличный от 1), мы прерываем цикл с помощью оператора break:

# num = int(input())
# flag = True

# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
#         break
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# EXAMPLES OF CODE REVIEWS❗️

# 1 💮

# print('A')
# print('A')
# print('A')
# print('A')
# print('A')
# print('A')
# print('A')
# print('A')
# print('A')
# print('A')

# for _ in range(10):
# print('A')


# 2 💮

# i = 1
# while i < 101:
#     if i % 7 == 0:
#         print(i)
#         i += 1 # < --------here------

# i = 1
# while i < 101:
#     if i % 7 == 0:
#         print(i)
#     i += 1

# ##### HAS BECOME
# for i in range(7, 101, 7):
#     print(i)

# 3 💮


# for i in range(1, 100):
#     print(101 - i)


# HAS BECOME

# for i in range(1, 101):
#     print(101 - i)

#     # AND

# for i in range(100, 0, -1):
#     print(i)

# 4 💮

# a = 1
# for i in range(1, 1000):
#     if i % 2 == 1:
#         a = a + 1
# print(a)


# # HAS BECOME

# total = 0
# for i in range(1, 1001, 2):
#     total += i
# print(total)

# 5 💮

# n = input()
# a = 0
# for i in range(n):
#     a = a * i
# print(a)

# # HAS BECOME

# n = int(input())
# a = 1
# for i in range(1, n + 1):
#     a = a * i
# print(a)

# # OR          ########
# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

#  ⚠️ В модуле math есть функция factorial(), которая вычисляет факториал числа. Поэтому вместо реализации своей версии, куда правильнее и удобнее воспользоваться уже готовой.
