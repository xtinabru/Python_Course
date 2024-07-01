# 🔸Revision

# 1)
# s1 = 'Python'
# s2 = "Pascal"

# 2)
# s = input()
# num = int(input())

# 3)
# s = 'Hello'
# n = len(s)  # 5
# print(n)

# 4)
# 'AB' + 'cd'	                  'ABcd'
# 'A' + '7' + 'B'	               'A7B'
# 'Hi'* 4	                      'HiHiHiHi'

# 5)
# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')


# 🟡 Indexation

# s = "Python"
# print()

# Unlike many programming languages, Python has the ability to work with negative indices. If the first character of a string has index 0, then the last element is assigned index -1.

# s[-6]	P
# s[-5]	y
# s[-4]	t
# s[-3]	h
# s[-2]	o
# s[-1]	n

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
# Positive indexes 0	1	2	3	4	5
# String	P	y	t	h	o	n
# Negative indexes 	-6	-5	-4	-3	-2	-1

# s = "abcdef"
# for i in range(len(s)):
#     print(s[i])


# s = "abcdef"
# for c in s:
#     print(c)

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
# s = "abcdef"

# for i in range(len(s)):
#     print(i, end=" ")

# print()

# for c in s:
#     print(c, end=" ")

# 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

# Ex 1 🟠

# s = "abcdefg"
# print(s[0] + s[2] + s[4] + s[6])

# aceg

# Ex 2 🟠

# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

# aaagggdddd

# Ex 3 🟠

s = "01234567891011121314151617"
for i in range(0, len(s), 5):
    print(s[i], end="")
