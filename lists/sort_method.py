# 🐻‍❄️
# sort(), which sorts the list elements in ascending or descending order.

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
# a.sort()
# print("Отсортированный список:", a)

# Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]

# 📍 By default, the sort() method sorts the list in ascending order.

# 📍If you want to sort the list in descending order, you must explicitly specify the parameter reverse = True

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
# a.sort(reverse=True)  # сортируем по убыванию
# print("Отсортированный список:", a)

# [1000, 99, 45, 34, 12, 9, 8, 7, 6, 1, 0, -2, -3, -67]

# 📍С помощью метода sort() можно сортировать списки содержащие не только числа, но и строки. В таком случае элементы списка сортируются в соответствии с лексикографическим порядком.

# a = ["бета", "альфа", "дельта", "гамма"]
# a.sort()
# print("Отсортированный список:", a)

# Отсортированный список: ['альфа', 'бета', 'гамма', 'дельта']

# Ex 1

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers) # [10, 8, 6, 5, 4, 4, 3, 2, 1]


# Ex 2

# numbers_str = input()
# number_list = numbers_str.split()

# numbers = []
# for num in number_list:
#     numbers.append(int(num))

# numbers.sort()
# sorted_asc = " ".join(str(num) for num in numbers)
# print(sorted_asc)

# numbers.sort(reverse=True)
# sorted_desc = " ".join(str(num) for num in numbers)
# print(sorted_desc)
