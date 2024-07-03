# Some methods are: min(), max(), len(), int(), floar() 🌹

# A method is a specialized function that is closely associated with an object. Like a function, a method is called to perform a separate task, but it is called on a specific object and “knows” about its target object at runtime.

# Method is a function applied to an object. 🌹
# In this case, to the line.
# The method is called in the form object_name.method_name(parameters).

# Methods of the string data type can be divided into three groups:

# Register conversion;
# Search and replace;
# Classification of symbols

# Register conversion🌹

# method capitalize() ❗️

# The capitalize() method returns a copy of the string s in which the first character is uppercase and all other characters are lowercase.

# s = "foO BaR BAZ quX"
# print(s.capitalize())      #Foo bar baz qux

# 📌 Characters that are not letters of the alphabet remain unchanged. The result of executing the following code:

# s = "foo123#BAR#."
# print(s.capitalize())    # Foo123#bar#.

# method swapcase() ❗️

# The swapcase() method returns a copy of the string s in which all uppercase characters are converted to lowercase characters and vice versa

# s = "FOO Bar 123 baz qUX"   # foo bAR 123 BAZ Qux
# print(s.swapcase())

# method title() ❗️

# The title() method returns a copy of the string s with the first character of each word converted to uppercase.

# s = "the sun also rises"
# print(s.title())       # The Sun Also Rises

# s = "what's happened to ted's IBM stock?"
# print(s.title())   #What'S Happened To Ted'S Ibm Stock?

# method lower()❗️

# The lower() method returns a copy of the string s with all characters in lowercase.

# s = "FOO Bar 123 baz qUX"
# print(s.lower())    # foo bar 123 baz qux

# method upper()❗️

# The upper() method returns a copy of the string s with all characters in uppercase.

# s = "FOO Bar 123 baz qUX"
# print(s.upper())           # FOO BAR 123 BAZ QUX

# ❕❕❕ One very important note about methods in this category is that they do not modify the original string. If you want to change the string s, you need to write the code: s = s.lower(). In fact, here you are creating a completely different object in the computer’s memory, it’s just with the old name s.

# ➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿

# TASKS

# 1 What will show 🔹

# s = "i Learn Python language"
# print(s.capitalize())        # I learn python language

# 2  What will show 🔹

# s = 'i LEARN Python LAnguaGE'
# print(s.lower())                # i learn python language

# 3  What will show 🔹

# s = "$12344%^$#@!"
# print(s.lower())  # $12344%^$#@!

# 4  What will show 🔹

# s1 = "a"
# s2 = s1.upper()
# print(s1, s2)  # a A


# 5  What will show 🔹

# s = "i LEARN Python LAnguaGE"
# print(s.upper())        # I LEARN PYTHON LANGUAGE


# 6  What will show 🔹

# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())  # I learn pYTHON laNGUAge

# ➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿➿

# Capital letters 🌹

# s = input()

# s2 = s.title()

# if s2 == s:
#     print("YES")
# else:
#     print("NO")

# sWAP cASE 🌹

# s = input()
# print(s.swapcase())

# Write a program that determines whether the shade of a text is good or not. The text has a good connotation if it contains the substring “good” in all possible cases.

# s = input()

# s = s.lower()

# if "хорош" in s:
#   print("YES")
# else:
#   print("NO")

# Lawer case 🌹

# s = input()

# total_lower = 0

# for i in s:
#     if i.islower():
#         total_lower += 1

# print(total_lower)
