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


# Ex 5 max, min 💠💠💠
# Find the maximum and the mininum digit of the number

# n = int(input())  # 1230
# max_digit = 0
# min_digit = n % 10

# while n != 0:
#     last_digit = n % 10

#     if last_digit > max_digit:
#         max_digit = last_digit

#     if last_digit <= min_digit:
#         min_digit = last_digit

#     n //= 10

# print("Максимальная цифра равна", max_digit)
# print("Минимальная цифра равна", min_digit)


# Ex 6 💠💠💠
# n = int(input())

# total = 0
# quantity = 0
# multiplication = 1
# original_n = n

# # sum
# while n > 0:
#     total += n % 10
#     n = n // 10

# # quantity
# n = original_n
# while n > 0:
#     n = n // 10
#     quantity += 1

# # multiplication
# n = original_n
# while n > 0:
#     last_digit = n % 10
#     multiplication *= last_digit
#     n = n // 10

# # arithmetic mean
# ar_mean = total / quantity

# # first digit
# first_digit = original_n
# while first_digit >= 10:
#     first_digit = first_digit // 10

# # last digit
# last_digit = original_n % 10

# # sum of first and last
# sum_first_last = first_digit + last_digit

# print(total)
# print(quantity)
# print(multiplication)
# print(ar_mean)
# print(first_digit)
# print(sum_first_last)


# OR


# n = int(input())
# total = 0
# count = 0
# product = 1
# len_str = len(str(n))
# first_number = (n // 10 ** (len_str - 1)) % 10
# summ_first_and_last = first_number + n % 10

# while n:
#     last_digit = n % 10

#     total += last_digit

#     count += 1

#     product *= last_digit

#     n //= 10

# print(total, count, product, total / len_str, first_number, summ_first_and_last, sep="\n")

# Ex 7  💠💠💠 Напишите программу, которая определяет его вторую (с начала) цифру.

# n = int(input())

# num_digits = len(str(n))

# if num_digits < 2:
#     print("There's no 2 digits.")
# else:
#     second_digit = (n // 10 ** (num_digits - 2)) % 10
#     print(second_digit)

# Ex 8 💠💠💠 Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

# n = int(input())

# n_to_string = str(n)  # Преобразуем число в строку для удобства доступа к каждой цифре

# first_digit = n_to_string[0]  # Получаем первую цифру

# equal_digit = True  # Устанавливаем флаг на True (предполагаем, что все цифры одинаковы)
# # т.е. мы делаем предположение, будто бы они равны

# index = 1

# while index < len(n_to_string):
#     if n_to_string[index] != first_digit:
#         equal_digit = False
#         break
#     index += 1

# if equal_digit:
#     print("YES")
# else:
#     print("NO")


# OR


# n = int(input())

# n_to_string = str(n)

# first_digit = n_to_string[0]

# equal_digit = True

# index = 1

# while index < len(n_to_string):
#     if n_to_string[index] != first_digit:
#         equal_digit = False
#         break
#     index += 1

# if equal_digit:
#     print("YES")
# else:
#     print("NO")


# Ex 9 💠💠💠
# Напишите программу, которая определяет,является ли последовательность его цифр при просмотре
# справа налево упорядоченной по неубыванию.

n = int(input())

n_str = str(n)


is_non_decreasing = True

for i in range(len(n_str) - 1):
    if n_str[i] < n_str[i + 1]:
        is_non_decreasing = False
        break

if is_non_decreasing:
    print("YES")
else:
    print("NO")
