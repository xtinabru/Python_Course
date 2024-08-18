# Ex 1 🌸

# def do_something(number):
#     return number * 2

# print(do_something(10)) # 20

# Ex 2 🌸

# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result

# print(do_something([2, 2, 2, 2])) # 16

# Ex 3 🌸

# def get_sum(x, y, z):
#     return x + y + z
#     print("Сумма равна", x + y + z)


# print(get_sum(1, 2, 3)) # 6

# Ex 4 Конвертер километров 🌸

# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214

# # считываем данные
# num = int(input())

# # вызываем функцию и выводим результат с нужным форматированием
# result = convert_to_miles(num)
# print(f"{result:.4f}") if num == 1 else print(f"{result:.3f}")

# OR


# # объявление функции
# def convert_to_miles(km):
#     ml = km * 0.6214
#     return ml

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))


# Ex 5 Количество дней 🌸

# объявление функции
# def get_days(month):
#     if month == 2:
#         return 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     else:
#         return 31


# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))


# Ex 6 Делители 1🌸

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа


# # объявление функции
# def get_factors(num):
#     factors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     return factors


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))


# Ex 7 Делители 2 🌸


# объявление функции
def number_of_factors(num):
    count = 0  # Инициализируем счетчик делителей
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1  # Увеличиваем счетчик за каждый делитель
    return count  # Возвращаем количество делителей


# считываем данные
n = int(input())

# вызываем функцию и выводим результат
print(number_of_factors(n))
