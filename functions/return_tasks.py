# 1 🌞 Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов.


# def compute_hypotenuse(a, b):
#     c = (a**2 + b**2) ** 0.5
#     return c


# print(compute_hypotenuse(3, 4))
# print(compute_hypotenuse(5, 12))
# print(compute_hypotenuse(1, 1))

# OR

# x = int(input())
# y = int(input())

# hypotenuse = compute_hypotenuse(x, y)

# print(hypotenuse)

# 📌 В модуле math имеется встроенная функция hypot(x, у) которая возвращает длину гипотенузы прямоугольного треугольника с катетами x и y.


# def get_distance(x1, y1, x2, y2):
#     return compute_hypotenuse(x1 - x2, y1 - y2)


# x1, y1 = float(input()), float(input())  # считываем координаты первой точки
# x2, y2 = float(input()), float(input())  # считываем координаты второй точки

# print(get_distance(x1, y1, x2, y2))  # вычисляем и выводим расстояние между точками

# import math

# def get_distance(x1, y1, x2, y2):
#     return math.hypot(x1 - x2, y1 - y2)

# # Считываем координаты первой точки
# x1, y1 = float(input("Введите координату x1: ")), float(
#     input("Введите координату y1: ")
# )

# # Считываем координаты второй точки
# x2, y2 = float(input("Введите координату x2: ")), float(
#     input("Введите координату y2: ")
# )

# # Вычисляем и выводим расстояние между точками
# print(f"Расстояние между точками: {get_distance(x1, y1, x2, y2)}")
