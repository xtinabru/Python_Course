# SLICES 🥪

# s = 'abcdefghij'

# Positive indexes:      0  1  2  3  4  5  6  7  8  9
# String:                a  b  c  d  e  f  g  h  i  j
# Negative indexes:    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# index range separated by colon s[x:y]

# print(s[2:5])        cde
# print(s[0:6])        abcdef
# print(s[2:7])        cdefg

# the first number is where the slice begins (inclusive) and the second number is where the slice ends (non-inclusive)
# print(s[2:])       c d e f g h i j
# print(s[:7])       a b c d e f g

# The slice s[:] returns the original string. 🔹

# Negative indexes in slices 🍰

# When using negative indexes, the first slice parameter must be less than the second, or must be omitted. 🔹

# print(s[-9:-4])      b c d e f
# print(s[-3:])        h i j
# print(s[:-3])        a b c d e f g

# You can remove the last character from a string using the slice s[:-1]🔹

# Step of slice 🥪

# print(s[1:7:2])     b d f

# Negative step  🔹

# print(s[::-1])  jihgfedcba


# print(s[1:7:2])
# print(s[3::2])
# print(s[:7:3])
# print(s[::2])
# print(s[::-1])
# print(s[::-2])

# bdf
# dfhj
# adg
# acegi
# jihgfedcba
# jhfdb

# 🔹🔹🔹

# s[2:5]	cde	строка состоящая из символов с индексами 2,3,4
# s[:5]	abcde	первые пять символов строки
# s[5:]	fghij	строка состоящая из символов с индексами от 5 до конца
# s[-2:]	ij	последние два символа строки
# s[:]	abcdefghij	вся строка целиком
# s[1:7:2]	bdf	строка состоящая из каждого второго символа с индексами от 1 до 6
# s[::-1]	jihgfedcba	строка в обратном порядке, так как шаг отрицательный

# 🌀 мы хотим заменить символ с индексом 4 на Х

# s = 'abcdefghij'

# ❗️❗️❗️s[4] = 'X'  ❌ В Python строки являются неизменяемыми, то есть мы не можем менять их содержимое с помощью индексатора. Мы должны создать новую строку. Следующий код использует срезы и решает поставленную задачу:

# s = s[:4] + 'X' + s[5:]
