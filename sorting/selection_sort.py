# 🐤 Сортировка выбором 🐤

# Сортировка выбором улучшает пузырьковую сортировку, совершая всего один обмен за каждый проход по списку. Для этого алгоритм ищет максимальный элемент и помещает его на соответствующую позицию. Как и для пузырьковой сортировки, после первого прохода самый большой элемент находится на правильном месте. После второго прохода на своё место становится следующий максимальный элемент. Проходы по списку повторяются n-1 раз, где n – длина списка, поскольку последний из них автоматически оказывается на своем месте.

# ❗️ Алгоритм сортировки выбором также считается учебным и практически не применяется вне учебной литературы. На практике используют более эффективные алгоритмы.


# a = [5, 1, 8, 2, 4]

# ⭐️ Первый проход:
# Находим максимальный элемент 8 в неотсортированной части списка и меняем его с последним элементом списка:

# [5, 1, 4, 2, 8]

# ⭐️ Второй проход:

# Находим максимальный элемент 5 в неотсортированной части списка и меняем его с предпоследним элементом списка:

# [2, 1, 4, 5, 8]

# ⭐️ Третий проход:

# Находим максимальный элемент 4 в неотсортированной части списка и меняем его с пред-предпоследним элементом списка:

# [2, 1, 4, 5, 8]

# ⭐️ Четвертый проход:
# Находим максимальный элемент 2 в неотсортированной части списка и меняем его с вторым элементом списка:

# [1, 2, 4, 5, 8]

# ❗️ Вместо максимального элемента можно искать минимальный.


# 🍇 Отсортируйте список по возрастанию, реализовав алгоритм сортировки выбором.
# a = [ 78,-32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)

# for i in range(n):
#     min_index = i
#     for j in range(i + 1, n):
#         if a[j] < a[min_index]:
#             min_index = j
#     if min_index != i:
#         a[i], a[min_index] = a[min_index], a[i]

# print(a)


######## OR

# n = len(a)

# for i in range(n):
#     mx_ind = n - 1 - i
#     for j in range(n - i):
#         if a[j] > a[mx_ind]:
#             mx_ind = j

#     a[n - 1 - i], a[mx_ind] = a[mx_ind], a[n - 1 - i]

# print(a)