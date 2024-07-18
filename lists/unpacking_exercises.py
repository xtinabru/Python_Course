# 1 ⭐️
# Complete the code below so that it prints the sum of the squares of the elements in the numbers list.

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

# sum_of_squares = 0

# for i in numbers:
#     sum_of_squares += i**2

# print(sum_of_squares)

# 2 ⭐️ Function value

# n = int(input())

# numbers = [int(input()) for _ in range(n)]

# print(*numbers, sep="\n")
# print()

# for number in numbers:
#     result = number**2 + 2 * number + 1
#     print(result)

# 3 ⭐️ Remove outliers

# The input to the program is a natural number n, and then n different natural numbers. Write a program that removes the smallest and largest values ​​from given numbers, and then prints the remaining numbers each on a separate line, without changing their order.

# n = int(input())

# numbers = [int(input()) for _ in range(n)]

# max_value = max(numbers)
# min_value = min(numbers)

# numbers.remove(max_value)
# numbers.remove(min_value)
# print(*numbers, sep="\n")

# OR

# n = int(input())

# numbers = [int(input()) for _ in range(n)]

# max_value = max(numbers)
# min_value = min(numbers)

# result = [i for i in numbers if i != max_value and i != min_value]
# print(*result, sep="\n")

# 4 ⭐️ No duplicates

# The program is given a natural number n as input, and then n lines. Write a program that prints only unique strings, in the same order in which they were entered.

# n = int(input())
# unique_str = []

# for _ in range(n):
#   string = input()
#   if string not in  unique_str:
#     unique_str.append(string)

# for string in unique_str:
#   print(string)


# 5 ⭐️ Google search - 1

# n = int(input())

# my_list = []
# for _ in range(n):
#     string = input()
#     my_list.append(string)

# question = input().lower()


# for string in my_list:
#     if question in string.lower():
#         print(string)

# 6 ⭐️ Google search - 2 🌶️🌶️

# n = int(input())

# str_list = []
# for _ in range(n):
#     string = input()
#     str_list.append(string)

# k = int(input())

# queries = []
# for _ in range(k):
#     quest = input().lower()
#     queries.append(quest)

# for string in str_list:
#   lowered_str = string.lower()
#   contains_all_queries = True

# for query in queries:
#   if query not in lowered_str:
#     contains_all_queries = False
#     break
#   if contains_all_queries:
#     print(string)

#  OR
# strings = [input() for _ in range(int(input()))]
# searches = [input() for _ in range(int(input()))]
# for string in strings:
#     for search in searches:
#         if search.lower() in string.lower():
#             continue
#         else:
#             break
#     else:
#         print(string)

# 7 ⭐️ Negatives, Zeros and Positives

# n = int(input())

# numbers = []
# for _ in range(n):
#     number = int(input())
#     numbers.append(number)

# negatives = []
# zeros = []
# positives = []

# for num in numbers:
#     if num < 0:
#         negatives.append(num)
#     elif num == 0:
#         zeros.append(num)
#     else:
#         positives.append(num)

# for num in negatives:
#     print(num)
# for num in zeros:
#     print(num)
# for num in positives:
#     print(num)
