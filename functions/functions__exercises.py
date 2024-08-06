# Ex 1 ⭐️

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)


# print_number(2, 3, 11)


# Ex 2 Что покажет приведенная ниже программа? ⭐️


# def print_text(text, num):
#     while num > 0:
#         print(text, end="")
#         num -= 1

# print_text("Python", 4) # PythonPythonPythonPython


# Ex 3  Звездный треугольник ⭐️

# fill = input()
# base = int(input())

# def draw_triangle(fill, base):
#     mid = (base // 2) + 1  # находим середину треугольника
#     # Рисуем первую половину треугольника
#     for i in range(1, mid + 1):
#         print(fill * i)
#     # Рисуем вторую половину треугольника
#     for i in range(mid - 1, 0, -1):
#         print(fill * i)

# draw_triangle(fill, base)


# Ex 4  ФИО ⭐️

# объявление функции
# def print_fio(name, surname, patronymic):
#     init_name = name[0]
#     init_surname = surname[0]
#     init_patron = patronymic[0]

#     fio = init_surname + init_name + init_patron
#     print(fio)


# # считываем данные
# name, surname, patronymic = input().upper(), input().upper(), input().upper()

# # вызываем функцию
# print_fio(name, surname, patronymic)

# Ex 5 Сумма цифр ⭐️

# n = int(input())

# def print_digit_sum(num):
#     total = 0
#     for digit in str(num):
#         total += int(digit)
#     print(total)

# print_digit_sum(n)
