# Exercise 1. Trangle 📐

# There is a number - n.
# Write a program which print a numerical triangle with a height n as:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21

# n = int(input())
# cur = 1

# for i in range(n):
#     for _ in range(i + 1):
#         print(cur, end=" ")
#         cur += 1
#     print()


# Exercise 2. Trangle 📐

# There is a number - n.
# Write a program which print a numerical triangle with a height n as:

# 1
# 121
# 12321
# 1234321
# 123454321

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")

#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()

# Exercise 3. Denominator - 1 🌶️

# There are a and b (a < b). Write a program which finds a natural number [a,b] with a max sum of denominators.
# If there are several numbers => so the maximum

# a = int(input())

# b = int(input())

# max_sum = 0  # будет хранить максимальную сумму делителей, найденную на данный момент.
# max_number = 0  # будет хранить число, соответствующее этой сумме делителей.

# for number in range(a, b + 1):
#     current_sum = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             current_sum += i
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_number = number
#     elif current_sum == max_sum and number > max_number:
#         max_number = number
# print(max_number, max_sum)

# Exercise 4. Denominator - 2 🌶️

# There is a natural number n. Write a program which prints graphical representation of the divisibility of numbers from 1 to n.
# In each line you need to print the next number and as many “+” symbols as there are divisors for this number.

# n = int(input())

# for i in range(1, n + 1):
#     div_count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             div_count += 1
#     print(i, "+" * div_count, sep="", end="\n")

# Exercise 5. Digital root 🫚

# There is a natural number n. Write a program which finds a digital root of  the n.
# DR  =  192 = 1 + 9 + 2 = 12 => 1 + 2 = 3

# n = int(input())

# while n > 9:
#     current_sum = 0
#     while n > 0:
#         last_digit = n % 10
#         current_sum += last_digit
#         n = n // 10
#     n = current_sum

# print(n)

# Exercise 6. Sum of factorials 🥨

# n = int(input())
# cur_sum = 0
# cur_factorial = 1

# for i in range(1, n + 1):
#     cur_factorial *= i
#     cur_sum += cur_factorial

# print(cur_sum)

# 3
# 1!+2!+3!

# Exercise 7. Prime numbers 🧁

# a = int(input())
# b = int(input())

# for i in range(a, b + 1):
#     if i > 1:
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)
