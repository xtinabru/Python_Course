# Ex 1 Amount of numbers 👑

# a = int(input())
# b = int(input())

# counter = 0

# for i in range(a, b + 1):
#     cube = i ** 3
#     if cube % 10 == 4 or cube % 10 == 9:
#         counter += 1

# print(counter)

# Ex 2 Sum of numbers👑

# n = int(input())

# sum = 0

# for i in range(n):
#     number = int(input())
#     sum += number

# print(sum)

# Ex 3 Asymptotic approximation👑

# import math

# n = int(input())

# sum_fractions = 0
# for i in range(1, n + 1):
#     sum_fractions += 1 / i

# log_n = math.log(n)

# result = sum_fractions - log_n
# print(result)

# Ex 4 Sum of numbers 2 🟢

# n = int(input())

# total = 0

# for i in range(1, n + 1):
#     last_digit = (i**2) % 10
#     if last_digit == 2 or last_digit == 5 or last_digit == 8:
#         total += i

# print(total)

# Ex 5 Factorial 🦑

# n = int(input())

# total = 1

# for i in range(1, n + 1):
#     total *= i

# print(total)

# Ex 6 🦑

# total = 1

# for i in range(10):
#     digit = int(input())
#     if digit != 0:
#         total *= digit

# print(total)

# Ex 7 Sum of divisors 🦑

# n = int(input())

# total = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, n % i)
#         total += i

# print(total)

# Ex 8 Alternating sum 🦑

# n = int(input())
# flag = True

# total = 0

# for i in range(1, n + 1):
#     if flag == True:
#         total += i
#     elif flag == False:
#         total -= i
#     flag = not flag


# print(total)

# Ex 9 Largest numbers 🌶️🌶️

# n = int(input())

# largest = 1
# second = 0

# for i in range(1, n + 1):
#     number = int(input())
#     if number > largest:
#         second = largest
#         largest = number
#     elif number > second:
#         second = number

# print(largest)
# print(second)

# Ex 10 Only even numbers 🌶️

# flag = True

# for i in range(10):
#     number = int(input())
#     if number % 2 != 0:
#         flag = False

# if flag:
#     print("YES")
# else:
#     print("NO")

# Ex 11 Fibonacci Sequence 🌶️

# n = int(input())

# first = 1
# second = 1

# if n == 1:
#     print(first)
# elif n == 2:
#     print(first, second)
# elif n > 2:
#     print(first, second, end=" ")
#     for i in range(2, n):
#         first, second = second, first + second
#         print(second, end=" ")
# print()


# # or

# n = int(input())
# a, b = 1, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# or
# num = int(input())
# a1 = 0
# a2 = 1
# for i in range(1, num + 1):
#     a3 = a1 + a2
#     print(a3, end=' ')
#     a2 = a1
#     a1 = a3


n = int(input())
f1, f2 = 1, 1
for i in range(n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
