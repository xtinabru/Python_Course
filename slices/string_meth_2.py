# Basic search and replace methods  ✨

# Methods for finding and replacing strings within other strings.
# 📌 Each method in this group accepts optional <start> and <end> arguments.
# 📌 If no parameters are specified, it is assumed that <start> = 0 , <end> = len(s)
# 📌As with string slices, the method's effect is limited to the portion of the source string starting at the <start> character position and continuing up to, but not including, the <end> character position. If <start> is specified but <end> is not, then the method is applied to the portion of the source string from <start> to the end of the string.

#  Method count() 🎈

# The count(<sub>, <start>, <end>) method counts the number of non-overlapping occurrences of the substring <sub> in the source string s

# s = 'foo goo moo'
# print(s.count('oo'))           # 3
# print(s.count('oo', 0, 8))  # sub, start, end # 2

#  Method startswith() 🎈

# always returns either True or False, depending on whether the specified part of the string begins with the substring suffix
# (<suffix>, <start>, <end>)

# s = 'foobar'
# print(s.startswith('foo')) True
# print(s.startswith('baz')) False

#  Method endswith() 🎈
# (<suffix>, <start>, <end>)

# s = 'foobar'
# print(s.endswith('bar')) True
# print(s.endswith('baz')) False

#  Methods find(), rfind() 🎈
# find(<sub>, <start>, <end>)

# finds the index of the first occurrence of the substring <sub> in the source string s. If the string s does not contain the substring <sub>, then the method returns the value -1. We can use this method along with the in operator to check whether a given string contains a certain substring or not

# s = 'foo bar foo baz foo qux'
# print(s.find('foo')) 0
# print(s.find('bar')) 4
# print(s.find('qu')) 20
# print(s.find('python')) -1


# FIND
# s = "hello world, hello universe"
# sub = "hello"
# index = s.find(sub)
# print(index)  # Output: 0

# RFIND
# s = "hello world, hello universe"
# sub = "hello"
# index = s.rfind(sub)
# print(index)  # Output: 13

# methods index(), rindex() 🎈

# index(<sub>, <start>, <end>)
# identical to the find(<sub>, <start>, <end>) method, except that it raises a ValueError: substring not found error at runtime if the substring <sub> is not found

# The rindex(<sub>, <start>, <end>) method is identical to the index(<sub>, <start>, <end>) method, except that it looks for the first occurrence of the substring <sub> starting from the end of string s

# The find() and rfind() methods are safer than index() and rindex() because they do not generate an error during program execution. 🎀

# method strip() 🎈

# The strip() method returns a copy of the string s with all spaces at the beginning and end of the string removed.

# s = "     foo bar foo baz foo qux      "
# print(s.strip())             # foo bar foo baz foo qux

# method lstrip() 🎈

# returns a copy of the string s with all leading spaces removed.

# s = '     foo bar foo baz foo qux      '
# print(s.lstrip())               # foo bar foo baz foo qux⎵ ⎵ ⎵ ⎵ ⎵ ⎵

# method rstrip()🎈

# The strip(), lstrip(), rstrip() methods can take an optional <chars> argument as input. The optional <chars> argument is a string that specifies the character set to be removed. 🎀

# method replace() 🎈

# replace(<old>, <new>)

# returns a copy of s with all occurrences of the substring <old> replaced by <new>

# s = "foo bar foo baz foo qux"
# print(s.replace("foo", "grault"))       # grault bar grault baz grault qux

# The replace() method can take an optional third argument <count>, which specifies the number of replacements.

# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault', 2))        # grault bar grault baz foo qux
