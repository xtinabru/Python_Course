# String methods
# 📌 isalnum(), isalpha(), isdigit(), islower(), isupper(), isspace()📌

# Character classification
# Methods in this group classify a string based on the characters it contains.

#   isalnum() 🌷
# determines whether the source string consists of alphanumeric characters

# s1 = 'abc123'
# s2 = 'abc$*123'
# s3 = ''

# print(s1.isalnum())   true
# print(s2.isalnum())   false
# print(s3.isalnum())   false

# isalnum() returns True even if the string contains only alphabetic or only numeric characters: 🪷

# s1 = 'BEEGEEK'
# s2 = '2202'

# print(s1.isalnum()) true
# print(s2.isalnum()) true

# isalpha() 🌷
# The method returns True if the source string is non-empty and consists only of alphabetic characters, or False otherwise

# s1 = 'ABCabc'
# s2 = 'abc123'
# s3 = ''

# print(s1.isalpha()) true
# print(s2.isalpha()) false
# print(s3.isalpha()) false

# isdigit() 🌷

# s1 = '1234567'
# s2 = 'abc123'
# s3 = ''

# print(s1.isdigit()) true
# print(s2.isdigit()) false
# print(s3.isdigit()) false

# islower() 🌷
# whether all alphabetic characters in the source string are lowercase (lowercase)

# s1 = 'abc'
# s2 = 'abc1$d'
# s3 = 'Abc1$D'

# print(s1.islower()) true
# print(s2.islower()) true
# print(s3.islower()) false

# 🍈  islower() ignores all non-letter characters

# print("1234".islower()) false
# print("+-*/".islower()) false
# print("ab#%".islower()) true

# isupper() 🌷

# s1 = 'ABC'
# s2 = 'ABC1$D'
# s3 = 'Abc1$D'

# print(s1.isupper()) true
# print(s2.isupper()) true
# print(s3.isupper()) false

# 🍈 ignores all non-letter characters

# print('5678'.isupper()) false
# print('!?_&'.isupper()) false
# print('AB%$'.isupper()) true

# isspace() 🌷

# only spaces

# s1 = '       '
# s2 = 'abc1$d'

# print(s1.isspace()) true
# print(s2.isspace()) False

# s1 = '' # empty is false
# print(s1.isspace())
