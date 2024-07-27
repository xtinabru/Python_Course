# 1 🩶
# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного списка, где у каждой строки удалён первый символ.

# keywords = [
#     "False",
#     "True",
#     "None",
#     "and",
#     "with",
#     "as",
#     "assert",
#     "break",
#     "class",
#     "continue",
#     "def",
#     "del",
#     "elif",
#     "else",
#     "except",
#     "finally",
#     "try",
#     "for",
#     "from",
#     "global",
#     "if",
#     "import",
#     "in",
#     "is",
#     "lambda",
#     "nonlocal",
#     "not",
#     "or",
#     "pass",
#     "raise",
#     "return",
#     "while",
#     "yield",
# ]

# new_keywords = [m[1:] for m in keywords]

# print(new_keywords)

# first_letters_of_three_letter_words = [m[0] for m in words if len(m) == 3]
# print(first_letters_of_three_letter_words)


# 2 🩶
# Дополните приведенный код, используя списочное выражение, так, чтобы получить новый список, содержащий длины строк исходного списка.

# keywords = [
#     "False",
#     "True",
#     "None",
#     "and",
#     "with",
#     "as",
#     "assert",
#     "break",
#     "class",
#     "continue",
#     "def",
#     "del",
#     "elif",
#     "else",
#     "except",
#     "finally",
#     "try",
#     "for",
#     "from",
#     "global",
#     "if",
#     "import",
#     "in",
#     "is",
#     "lambda",
#     "nonlocal",
#     "not",
#     "or",
#     "pass",
#     "raise",
#     "return",
#     "while",
#     "yield",
# ]

# lengths = [len(m) for m in keywords]

# print(lengths)

# 3 🩶
# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).

# keywords = [
#     "False",
#     "True",
#     "None",
#     "and",
#     "with",
#     "as",
#     "assert",
#     "break",
#     "class",
#     "continue",
#     "def",
#     "del",
#     "elif",
#     "else",
#     "except",
#     "finally",
#     "try",
#     "for",
#     "from",
#     "global",
#     "if",
#     "import",
#     "in",
#     "is",
#     "lambda",
#     "nonlocal",
#     "not",
#     "or",
#     "pass",
#     "raise",
#     "return",
#     "while",
#     "yield",
# ]

# new_keywords = [(m) for m in keywords if len(m) >= 5]

# print(new_keywords)

# 4 🩶

# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).

# Примечание. Результирующий список должен состоять из целых чисел.

# palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]

# print(palindromes)

# 5 🩶
# Списочное выражение 1

# На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, которая создает список, содержащий квадраты чисел от 1 до n (включительно), а затем выводит его элементы построчно, то есть каждый на отдельной строке.

# squares_of_numbers = [i**2 for i in range(1, int(input()) + 1)]

# squares_as_string = "\n".join([str(num) for num in squares_of_numbers])

# print(squares_as_string)

# or

# n = int(input())
# squares = [el ** 2 for el in range(1, n + 1)]

# for el in squares:
#     print(el)

# 6 🩶
# Списочное выражение 2

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.


# cubes = [int(el) ** 3 for el in input().split()]  # тут список
# cubes_str = " ".join(str(cube) for cube in cubes)

# print(cubes_str)

# 7 🩶
# В одну строку 1
# На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной строки в столбик.

# words = [word for word in input().split()]
# words_string = "\n".join(str(w) for w in words)

# print(words_string)

# 8 🩶
# В одну строку 2
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.

# import re

# text = input()

# numbers = re.findall(r"\d+\d*", text)

# result = "".join(numbers)

# print(result)

# ORRR

# digits = [el for el in input() if el.isdigit()]
# print(*digits, sep="")
