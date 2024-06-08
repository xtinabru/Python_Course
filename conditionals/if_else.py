# Part 1 "Conditionals"

# branching: True or False

"""
answer = input("Which programming language do we learn?")
if answer == "Python":
    print("Right!")
    print("Python is awesome!")
else:
    print("No!")
"""

#  (=) - define
#  (==) - conditional operator

# examples
num = 1992
s = "I love Python"

# comparison
"""
if x > 7
if x < 7
if x >= 7
if x <= 7
if x == 7
if x != 7
"""

# examples
"""
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, "less than", num2)
if num1 > num2:
    print(num1, "bigger than", num2)
if num1 == num2:
    print(num1, "equals", num2)
if num1 != num2:
    print(num1, "doesn't equal", num2)
    
"""

# CHAINS
"""
age = int(input())
if 3 <= age <= 6:
    print("You are a kid")
"""
# Transitive relations
# if a == b and b == c => A==C
# if a > b and b > c => A > C
# if a || b and b || c => A || C
# if a / b and b / c  => a / c

# Intransitivity
# !=
# if a != b and b != c IT DOESN'T MEAN THAT a != c
