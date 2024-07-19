# ⭐️
# the split() method splits a string using an arbitrary delimiter into a list of words, and the join() method assembles a string from a list of words using a given delimiter.

# ⭐️ split()
# The split() method splits a string into words using a sequence of whitespace characters as a delimiter, and returns a list of these words.

# s = "Python is the most powerful language"
# words = s.split()
# print(words) # ['Python', 'is', 'the', 'most', 'powerful', 'language']

# ❗️The split() method splits the STRING into words and RETURNS a LIST

# Ex
# numbers = input().split() # 1 2 3 4 5
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers) # [1, 2, 3, 4, 5]

# ❗️Optional parameter split('.')

# ip = "192.168.1.24"
# numbers = ip.split(".")  #
# print(numbers) # ['192', '168', '1', '24']

# ⭐️ join()
# The join() method assembles a string from the elements of a list, using as a delimiter the string to which the method is applied.

# words = ["Python", "is", "the", "most", "powerful", "language"]
# s = " ".join(words)
# print(s) # Python is the most powerful language

# Examples:
# words = ['Мы', 'учим', 'язык', 'Python']
# print('*'.join(words))
# print('-'.join(words))
# print('?'.join(words))
# print('!'.join(words))
# print('*****'.join(words))
# print('abc'.join(words))
# print('123'.join(words))

# ❗️ There is a big difference between the results of calling s.split() and s.split(' '). The difference in behavior occurs when the line contains multiple spaces between words.
# s = "I love  Python"
# words1 = s.split()
# words2 = s.split(" ")
# print(words1) # ['I', 'love', 'Python']
# print(words2) # ['I', 'love', '', 'Python']

# ❗️ The split() and join() methods are string methods, they cannot be applied to lists!
# print([1, 2].split()) # AttributeError: 'list' object has no attribute 'split'

# ❗️The string join() method does not work for lists whose elements are not of string data type.

# numbers = [1, 2, 3, 4]  # список чисел
# s = "*".join(numbers)
# print(s) # TypeError: sequence item 0: expected str instance, int found

# ❗️In fact, the join() method can take not only a list, but also a string as an argument.

# s = "+".join("pygen")
# print(s) # p+y+g+e+n
