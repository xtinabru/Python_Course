# ex1

"""
word = input()

if word == "Python":
    print("YEP")
else:
    print("NOPE")
"""
# ex2

"""
num = int(input())

last = num % 10
first = num // 10

if last == first:
    print("The digits are equal")
else:
    print("There are different digits")
"""
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)
