# Representation of strings in computer memory, ASCII and Unicode 🔅

# When a character is stored in memory, it is first converted into a digital code. And then this digital code is stored in memory as a binary number

# Various encoding schemes have been developed to represent characters in computer memory. Historically, the most important of these encoding schemes is the ASCII encoding scheme (American Standard Code for Information Interchange)

# ASCII character table 🔅

# ASCII is a set of 128 numeric codes that represent English letters, various punctuation marks, and other characters.
#
# For example, the ASCII code for the uppercase English letter "A" (Latin) is 65. When you type the uppercase letter "A" on a computer keyboard, the number 65 is stored in memory (as a binary number 01000001).

# There are exactly 7 bits per character in ASCII.

# The ASCII character set was developed in the early 1960s and was eventually adopted by almost all computer manufacturers. However, the ASCII encoding scheme has limitations because it only defines codes for 128 characters. To remedy this, the Unicode character set was developed in the early 1990s. It is a broad ASCII-compatible encoding scheme that can also represent characters from many of the world's languages. Today, Unicode is quickly becoming the standard character set used in the computer industry.

# Unicode Character Table 🔅

# The Unicode character table is a set of digital characters that includes characters from almost all written languages ​​of the world.
# The standard consists of two main parts: a universal character set and a family of encodings (Unicode transformation format, UTF). The Universal Character Set lists the characters allowed by the Unicode standard and assigns a code to each character as a non-negative integer. An encoding family defines how character codes are converted for storage on a computer and transmission.

# When storing one Unicode character in memory, 1 to 8 bytes may be required

# In Python, strings are stored as a sequence of Unicode characters.

# Unicode is not an encoding. This is exactly a symbol table. How characters with their corresponding codes are stored in computer memory depends on the specific Unicode-based encoding, such as UTF-8.

# The first 128 codes of the Unicode character table are the same as ASCII.

# function ord  🔆 🔆 🔆 order
# The ord function allows you to determine the code of a certain character in the Unicode character table. The argument to this function is a single character.

# num1 = ord("A")
# num2 = ord("B")
# num3 = ord("a")
# print(num1, num2, num3) 65 66 97

# num = ord("Abc") ⛔️
# print(num)   # TypeError: ord() expected a character, but string of length 3 found

# function chr 🔆 🔆 🔆 char

# The chr function allows you to determine the character itself by its code. The argument of this function is a numeric code

# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110)
# print(chr1, chr2, chr3) A K n

# ⛔️
# he ord and chr functions often work in tandem. We can use the following code to output all capital letters of the English alphabet:

# for i in range(26):
#     print(chr(ord("A") + i))

# Calling the function ord('A') returns the code of the character "A", which is equal to 65. Then, at each iteration of the loop, the value of the variable i = 0, 1, 2, ..., 25 is added to this code, and then the resulting code is converted to a character using a call to the chr function


# TASK 1 💠💠💠

# a = int(input())
# b = int(input())

# for i in range(a, b + 1):
#     print(chr(i), end=" ")

# TASK 2 💠💠💠

# text = str(input())

# for i in text:
#     print(ord(i), end=" ")

# TASK 3 notae Caesarianae🌶️ (1≤ n≤ 25)

# n = int(input())
# message = str(input())

# decode_message = ""

# for char in message:
#     original_position = ord(char) - ord("a")
#     new_position = (original_position - n) % 26
#     new_char = chr(new_position + ord("a"))
#     decode_message += new_char

# print(decode_message)
