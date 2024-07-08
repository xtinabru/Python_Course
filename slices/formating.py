# Example prints error 💠💠💠
# birth_year = 1992
# text = 'My name is Timur, I was born in ' + birth_year

# print(text) #-------->  TypeError: can only concatenate str (not "int") to str

# Second example 💠💠💠
# birth_year = 1992
# text = 'My name is Timur, I was born in ' + str(birth_year)

# print(text) # -------> My name is Timur, I was born in 1992

# This code works, but converting a number to a string every time is not very convenient. For more visual formatting, we can use the string format() method

# We pass the necessary parameters to the format() method, and Python puts them in place of the {} curly braces as placeholders. We can create as many placeholders as we want.

# birth_year = 1992 💠💠💠
# text = 'My name is Timur, I was born in {}'.format(birth_year)

# print(text)

# birth_year = 1991 💠💠💠
# name = "Lucio"
# profession = "Math teacher"

# text = "My name is {}, I was born in {}, I work as a {}.".format(
#     name, birth_year, profession
# )

# print(text)

# 🌀
# The format() method does a good job of formatting strings, but if there are a lot of parameters, the code may seem a little redundant.

# first_name = 'Taylor'
# second_name = 'Swift'
# country = 'USA'
# birth_date = '1989/12/13'
# birth_place = 'West Reading, Pennsylvania'
# text = '{0} {1} is a very famous singer from the {2}. She was born on {3} in {4}.'.format(first_name, second_name, country, birth_date, birth_place)

# print(text) # Taylor Swift is a very famous singer from the USA. She was born on 1989/12/13 in West Reading, Pennsylvania.

# 🌀
# first_name = 'Taylor'
# last_name = 'Swift'
# country = 'USA'
# birth_date = '1989/12/13'
# birth_place = 'West Reading, Pennsylvania'
# text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'

# print(text)
