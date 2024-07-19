# Ex 1🩵
# The split() method splits a string into parts using the default whitespace (or a specified delimiter) as the delimiter, and returns a list of those parts. The join() method joins the elements of a list (or string) into a string, using as a delimiter the string on which it is called. If we apply the join() method to a list, then its elements can only be of string data type.

# Ex 2🩵 What will the code below show?

# s = "a     b c"
# print(s.split()) # ['a', 'b', 'c']

# Ex 3🩵 What will the code below show?

# s = "a     b c"
# print(s.split(" ")) # ['a', '', '', '', '', 'b', 'c']

# Ex 4🩵 What will the code below show?

# print("-".join(["pen", "pineapple", "apple", "pen"]))
# pen-pineapple-apple-pen

# Ex 5🩵 What will the code below show?

# letters = ['B', ' ', 'T', ' ', 'S']
# print(letters.split()) # errror, as it's a list

# Ex 6🩵 What will the code below show?

# print("-".join("DNA")) # D-N-A

# Ex 7🩵 What will the code below show?

# symbols = ["I", "D", "O", "L"]
# print(symbols.join("-"))  # error

# Ex 8🩵 What will the code below show?

# s = "BEEGEEK"
# chars = list(s)
# s = "**".join(chars)
# print(s) # B**E**E**G**E**E**K
