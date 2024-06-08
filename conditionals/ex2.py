# ex1 PASSWORD

"""
password = input()
confirmation = input()

if password == confirmation:
    print("Пароль принят")
else:
    print("Пароль не принят")
"""

# ex2 EVEN AND ODD
"""
num = int(input())
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
"""

# ex3
"""
num = int(input())

first = num // 1000
second = (num // 100) % 10
third = (num // 10) % 10
fourth = num % 10

if first + fourth == second - third:
    print("YEP")
else:
    print("NOPE")
"""

# ex4
"""
age = int(input())

if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
"""

# ex5 Progression
"""
a = int(input())
b = int(input())
c = int(input())

if b - a  == c - b:
    print("YES")
else:
    print("NO")
"""

# ex6 the least of two
"""
num1, num2 = int(input()), int(input())
if num1 > num2:
    print(num2)
else:
    print(num1)
"""

# ex7 the least of 4 6782
"""
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a < b:
    min_ab = a
else:
    min_ab = b

if c < d:
    min_cd = c
else:
    min_cd = d

if min_ab < min_cd:
    min_abcd = min_ab
else:
    min_abcd = min_cd
print(min_abcd)
"""

# ex8 AGE GROUP
"""
age = int(input())

if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")
"""

# ex9 🌶️
a = int(input())
b = int(input())
c = int(input())

sum = 0

if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c
print(sum)
