# 1  🌼 Список четных 🌼

# На вход программе подается четное число n,n≥2. Напишите программу, которая выводит список четных чисел [2, 4, 6, ..., n].

# n = int(input())

# my_list = []

# for i in range(2, n + 1, 2):
#     my_list.append(i)

# print(my_list)


# 2 🌼 Сумма двух списков🌼

# На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.

# first_line = input()
# second_line = input()

# list_l = first_line.split()
# list_m = second_line.split()

# for i in range(len(list_l)):
#     list_l[i] = int(list_l[i])
#     list_m[i] = int(list_m[i])

# sum_list = []

# for i in range(len(list_l)):
#     sum_list.append(list_l[i] + list_m[i])

# for num in sum_list:
#     print(num, end=" ")


# OOOOOOOOOOOOR

# a = input().split()
# b = input().split()
# n = len(a)

# seq = [int(a[i]) + int(b[i]) for i in range(n)]
# print(*seq)


# 🌼 Сумма чисел 🌼

# На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
#  Строковый метод join() работает только со списком строк.


# Считываем строку и разбиваем её на части
# text = input().split()
# numbers = [int(x) for x in text]

# number_strings = [str(num) for num in numbers]


# result = "+".join(number_strings)
# total_sum = sum(numbers)
# print(f"{result}={total_sum}")


# # OOOOOOOR

# seq = input().split()
# expression = "+".join(seq)

# sm = 0
# for el in seq:
#     sm += int(el)
# expression += f"={sm}"

# print(expression)


# 🌼 Валидный номер 🌶️🌶️

# import re

# phone_number = input().strip()

# pattern1 = r"^\d{3}-\d{3}-\d{4}$"
# pattern2 = r"^7-\d{3}-\d{3}-\d{4}$"

# if re.match(pattern1, phone_number) or re.match(pattern2, phone_number):
#     print("YES")
# else:
#     print("NO")


# 🌼 Самый длинный 🌼

# text = input().split()

# lengths = [len(word) for word in text]

# max_length = max(lengths)

# print(max_length)


##### OOOOR
# lens = [len(el) for el in input().split()]
# print(max(lens))

### 🌼 Молодежный жаргон🌼

# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу:

# первая буква каждого слова удаляется и ставится в конец слова;
# затем в конец слова добавляется слог "ки".

# text = input().split()

# changed_words = [word[1:] + word[0] + "ки" for word in text]

# result = " ".join(changed_words)
# print(result)
