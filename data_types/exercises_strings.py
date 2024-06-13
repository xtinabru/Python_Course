# ex 1  Write: 💖
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

# text = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''

# print(text)

# ex 2 "What's your name?" 💖
# Write:
# #Hello <введённое имя> <введённая фамилия>! You have just delved into Python

# name = str(input())
# last_name = str(input())

# print("Hello", name, last_name + "!", "You have just delved into Python")

# ex 3 Football team ⚽

# team = str(input())
# name_length = len(team)

# print("Футбольная команда", team, "имеет длину", name_length, "символов")

# ex 4 Three cities 🌆
# Write the shortest and then longest name

# city1, city2, city3 = str(input()), str(input()), str(input())

# a = len(city1)
# b = len(city2)
# c = len(city3)

# longest = max(a, b, c)
# shortest = min(a, b, c)

# if shortest == a:
#     shortest = city1
# elif shortest == b:
#     shortest = city2
# else:
#     shortest = city3

# if longest == a:
#     longest = city1
# elif longest == b:
#     longest = city2
# else:
#     longest = city3

# print(shortest)
# print(longest)

# ex 5 Arithmetic strings

s1, s2, s3 = str(input()), str(input()), str(input())

a = len(s1)
b = len(s2)
c = len(s3)

max_len  = max(a, b, c)
min_len = min(a, b, c)
mid_len = (a + b + c) - max_len - min_len

if mid_len - min_len == max_len - mid_len:
  print("YES")
else:
  print("NO")


1 3 5 

1 +