# Ex 1  First 12 🔺

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])

# Ex 2 Last 9 🔺

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# Ex 3 each 7🔺

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[0:-1:7])  or print(s[::7])

# Ex 4 s bakwards🔺

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# Ex 5 palindrome🔺

# s = input()

# if s == s[::-1]:
#     print("YES")
# else:
#   print("NO")

# Ex 6 Slices 🔺

# s = input()
# total = 0

# for i in s:
#     total += 1

# print(total)  # total amount of symbols
# print(s * 3)  # repeats 3 times
# print(s[0:1])  # first symbol
# print(s[0:3])  # first three
# print(s[-3:])  # last three
# print(s[::-1])  # backwards
# print(s[1:-1]) # delete 1 and the last

# Ex 7 Slices.2 🔺

# s = input()

# print(s[2:3])  # the third symbol
# print(s[-2:-1])  # before the last
# print(s[0:5])  # first 5 symbols
# print(s[0:-2])  # everithing exept the last 2 symbols
# print(s[::2]) # even
# print(s[1::2]) # odd
# print(s[::-1]) # backwards
# print(s[::-2])

# Ex 8 Two halfs🔺Write a program that will cut it into two equal parts, rearrange them and display them on the screen.

# s = input()

# median = (len(s) + 1) // 2

# first_part = s[:median]
# second_part = s[median:]

# result = second_part + first_part

# print(result)
