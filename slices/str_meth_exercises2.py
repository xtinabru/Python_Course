# Ex 1  ⭐️

# s = 'aabbAA111ccDDaa'
# print(s.isalnum()) true
# print(s.isalpha()) false
# print(s.isdigit()) false

# Ex 2 ⭐️

# print('Cyberpunk 2077'.isalnum()) # false  - as there is  a space between

# Ex 3 ⭐️

# print('Cyberpunk'.isalnum()) # true
# print('2077'.isalnum()) # true

# Ex 4 ⭐️

# s = 'aabb!@#$11cc'
# print(s.islower()) # true

# Ex 5 ⭐️

# s = 'AAb!@#$11CC'
# print(s.isupper()) # false

# Ex 6 ⭐️

# print('2024-05-19'.islower()) # false
# print('2024-05-19'.isupper()) # false

# Ex 7 ⭐️

# s = '    abbc    '
# print(s.isspace()) # false


# TASK 1 ☀️

# bad comments '' or isspace = true ====> COMMENT SHOULD BE DELETED»

# should be  1) number from 1 2) : 3) text or COMMENT SHOULD BE DELETED

# n = int(input())

# for i in range(n):
#     comment = input()
#     if comment.isspace() == True or comment == "":
#         print(i + 1, ":", " ", "COMMENT SHOULD BE DELETED", sep="")
#     else:
#         print(i + 1, ":"," ", comment, sep="")


# TASK 2 🚗

# generated_number = input()

# # Допустимые буквы кириллицы
# valid_letters = "АВЕКМНОРСТУХ"

# # Предполагаем, что номер некорректный
# is_valid = False

# # Проверка длины строки
# if len(generated_number) == 9:
#     # Формат <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
#     if (generated_number[0] in valid_letters and
#         generated_number[1].isdigit() and
#         generated_number[2].isdigit() and
#         generated_number[3].isdigit() and
#         generated_number[4] in valid_letters and
#         generated_number[5] in valid_letters and
#         generated_number[6] == '_' and
#         generated_number[7].isdigit() and
#         generated_number[8].isdigit()):
#         is_valid = True
# elif len(generated_number) == 10:
#     # Формат <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
#     if (generated_number[0] in valid_letters and
#         generated_number[1].isdigit() and
#         generated_number[2].isdigit() and
#         generated_number[3].isdigit() and
#         generated_number[4] in valid_letters and
#         generated_number[5] in valid_letters and
#         generated_number[6] == '_' and
#         generated_number[7].isdigit() and
#         generated_number[8].isdigit() and
#         generated_number[9].isdigit()):
#         is_valid = True

# # Вывод результата
# if is_valid:
#     print("YES")
# else:
#     print("NO")

# # OR

# s = input()
# flag = 'NO'
# correct_letters = 'АВЕКМНОРСТУХ'

# if 9 <= len(s) <= 10:
#     letters = s[0] + s[4:6]
#     digits = s[1:4] + s[7:]
#     underscore = s[6]

#     if digits.isdigit() and underscore == "_":
#         flag = 'YES'

#     for c in letters:
#         if c not in correct_letters:
#             flag = 'NO'

# print(flag)


# TASK 3 CHECK NICKNAME 👩🌶️

# s = input()

# if s.startswith("@") and 5 <= len(s) <= 15 and s[1:].isalnum() and s == s.lower():
#     print("Correct")
# else:
#     print("Incorrect")
