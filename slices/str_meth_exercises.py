# Ex 1 🔸🔸🔸

# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))  # 6

# Ex 2 🔸🔸🔸

# s = 'www.google.com'
# print(s.startswith('www')) # True

# Ex 3 🔸🔸🔸

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))   # 8

# Ex 4 🔸🔸🔸

# s = '     I learn Python language               '
# print(s.strip())           # I learn Python language

# Ex 5 🔸🔸🔸

# s = 'abcdababa'
# print(s.replace('ab', '123'))   # 123cd123123a

# TASKS 🟧

# 1  Quantity of words 🔸🔸🔸

# The input to the program is a string of text consisting of words separated by exactly one space. Write a program that counts the number of words in it.

# s = input()

# space_count = s.count(" ")

# word_count = space_count + 1

# print(word_count)


# 2  Genetics  🧬

# genetic_code = input()

# genetic_code = genetic_code.lower()

# adenine_count = genetic_code.count("а")
# guanine_count = genetic_code.count("г")
# cytosine_count = genetic_code.count("ц")
# thymine_count = genetic_code.count("т")

# print("Аденин:", adenine_count)
# print("Гуанин:", guanine_count)
# print("Цитозин:", cytosine_count)
# print("Тимин:", thymine_count)

# 3 Stranger Things 📻

# n = int(input())
# messages_from_odi = 0

# for _ in range(n):
#     message = input()
#     count_11 = message.count("11")
#     if count_11 >= 3:
#         messages_from_odi += 1

# print(messages_from_odi)

# 4 The quanttity of numbers 📟

# n = input()

# quantity = 0

# for i in n:
#     if i.isdigit():
#         quantity += 1

# print(quantity)

# 5 .com or .fi 🔑

# n = input()

# if n.endswith(".com") or n.endswith(".fi):
#     print("YES")
# else:
#     print("NO")

# 6 Most Frequent Symbol 🪅

# text = input()

# max_char = ""
# max_count = 0

# for char in text:
#     count = text.count(char)
#     if count > max_count or (count == max_count and char > max_char):
#         max_count = count
#         max_char = char

# print(max_char)


#  ------------OR WITH DICT -------------
# # Считываем строку текста от пользователя
# text = input()

# # Создаем пустой словарь для хранения частоты появления символов
# frequency = {}

# # Проходим по каждому символу в строке
# for char in text:
#     # Если символ уже есть в словаре, увеличиваем его частоту
#     if char in frequency:
#         frequency[char] += 1
#     # Если символа нет в словаре, добавляем его с частотой 1
#     else:
#         frequency[char] = 1

# # Переменные для хранения символа с максимальной частотой и самой высокой частоты
# max_char = ''
# max_count = 0

# # Находим символ с максимальной частотой
# for char, count in frequency.items():
#     # Если текущая частота больше максимальной или частоты равны, выбираем последний по порядку символ
#     if count > max_count or (count == max_count and char > max_char):
#         max_count = count
#         max_char = char

# # Выводим символ с максимальной частотой
# print(max_char)

# 7 First and last occurrence 🧸

# if "f" =  1 print index
# if "f" 2 or more print first and last indexes, using " "
# if there's no "f" print "NO"

# text = input()

# first_index = text.find("f")
# last_index = text.rfind("f")

# if first_index == -1:
#   print("NO")
# elif first_index == last_index:
#   print(first_index)
# else:
#   print(first_index, last_index)

# -------------OR---------------

# s = input()
# cnt = s.count("f")

# if cnt == 0:
#     print("NO")
# elif cnt == 1:
#     print(s.index("f"))
# else:
#     print(s.index("f"), s.rindex("f"))
