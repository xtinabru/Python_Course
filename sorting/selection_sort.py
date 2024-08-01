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
