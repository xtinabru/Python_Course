# Ex 1 💠💠💠

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)


# Итерация 1: last_digit = 12345 % 10 = 5, product = 1 * 5 = 5, num = 12345 // 10 = 1234
# Итерация 2: last_digit = 1234 % 10 = 4, product = 5 * 4 = 20, num = 1234 // 10 = 123
# Итерация 3: last_digit = 123 % 10 = 3, product = 20 * 3 = 60, num = 123 // 10 = 12
# Итерация 4: last_digit = 12 % 10 = 2, product = 60 * 2 = 120, num = 12 // 10 = 1
# Итерация 5: last_digit = 1 % 10 = 1, product = 120 * 1 = 120, num = 1 // 10 = 0

# Ex 2 💠💠💠

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1

#     num = num // 10

# print(total)

# Ex 3 💠💠💠
# Напишите программу, которая выводит его цифры в столбик в обратном порядке.

# n = int(input())

# while n > 0:
#     last_digit = n % 10
#     print(last_digit)
#     n = n // 10

# Ex 4  💠💠💠
# Напишите программу, которая меняет порядок цифр числа на обратный.

# n = int(input())

# while n > 0:
#     last_digit = n % 10
#     print(last_digit, end="")


# Ex 5 max, min
# Find the maximum and the mininum digit of the number

n = int(input())  # 1230
max_digit = 0
min_digit = n % 10

while n != 0:
    last_digit = n % 10

    if last_digit > max_digit:
        max_digit = last_digit

    if last_digit <= min_digit:
        min_digit = last_digit

    n //= 10

print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)
