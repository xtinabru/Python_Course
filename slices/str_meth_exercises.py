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

# 5 .com or .org

n = input()

if n.endswith(".com") or n.endswith(".ru"):
    print("YES")
else:
    print("NO")
