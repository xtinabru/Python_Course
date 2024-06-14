# ex 1 🪿

# language1 = 'JavaScript'
# language2 = 'Java'

# print(language1 in language2) #False
# print(language2 in language1) #True

# ex 2 🪿

# digits = '0123456789'

# print('45' in digits) #TRUE
# print('09' in digits) #FALSE

# ex 3 🌊
# Write a program that reads one line and then prints “YES” if the input line contains the substring “blue”, or “NO” otherwise.

# s = input()

# if "blue" in s:
#     print("YES")
# else:
#     print("NO")

# ex 4  Do we have rest? 🥂

# s = input()

# if "суббота" in s or "воскресенье" in s:
#     print("YES")
# else:
#     print("NO")

# ex 5 Correct e-mail 📧

s = input()

if "." in s and "@" in s:
    print("YES")
else:
    print("NO")
