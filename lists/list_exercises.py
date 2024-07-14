# Ex 1  🟧
# Complete the above code using the indexer so that it prints the 17th (in order) element of the list primes

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[16])

# Ex 2  🟧
# Complete the following code using an indexer so that it prints the last element of the primes list.

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[-1])

# Ex 3  🟧
# Complete the above code using slices so that it prints the first 6 elements of the primes list. ### The output should be the string [2, 3, 5, 7, 11, 13].

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[:6])

# Ex 4  🟧
# Complete the code below so that it prints the sum of the minimum and maximum elements of the numbers list.

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# max_number = max(numbers)
# min_number = min(numbers)
# result = max_number + min_number
# print(result)

# or
# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# res = min(numbers) + max(numbers)

# print(res)

# Ex 5  🟧
# Complete the code below so that it prints the arithmetic mean of the elements in the evens list.

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)

# print(average)

# Ex 6  🟧
# Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.

# rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

# rainbow[3] = "Зеленый"
# rainbow[-1] = "Фиолетовый"

# print(rainbow)

# Ex 7  🟧
# Complete the above code so that it displays a "reversed" list of languages ​​(that is, the elements will be in reverse order).

# languages = [
#     "Chinese",
#     "Spanish",
#     "English",
#     "Hindi",
#     "Arabic",
#     "Bengali",
#     "Portuguese",
#     "Russian",
#     "Japanese",
#     "Lahnda",
# ]

# print(languages[::-1])

# Ex 8  🟧
# Complete the following code using the concatenation (+) and list-by-number (*) operators so that it outputs a list:
#
# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]

# print(numbers1 * 2 + numbers2 * 9 + numbers3)
