# Ex 1 range(8) 💙
# 0, 1, 2, 3, 4, 5, 6, 7

# Ex 2 range(1, 8) 💙
# 1, 2, 3, 4, 5, 6, 7

# Ex 3 range(3, 11, 2)💙
# 3, 5, 7, 9

# Ex 4 range(10, 0, -2)💙
# 10, 8, 6, 4, 2

# Ex 5 How many iterations?💙

# for _ in range(1, 6):
#    print('Python rocks!') #5

# Ex 6 Number sequence 1💙
# There is a sequence m and n (m <=n)

# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#     print(i)

# Ex 7 Number sequence 2 💙🌶️
# There are m and n (m < n)

# m = int(input())
# n = int(input())

# if m < n:
#     for i in range(m, n + 1):
#         print(i)

# elif m > n:
#     for i in range(m, n - 1, -1):
#         print(i)
# else:
#     print(m)

# Ex 8 Number sequence 3 💙🌶️🌶️
# There are 2 numbers m and n (m > n)
# prints all odd numbers

# 1)

# m = int(input())
# n = int(input())

# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)

# 2) = ?

# Ex 9 Number sequence 4 💙
# There are 2 numbers m and  n ( m <= n)

# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# Ex 10 Multiplication table 💙
# There is n. Make a multiplication table till 10

n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
