# 🔅

# When printing the contents of a list using the print() function, the elements are printed in square brackets, with all elements separated by a comma.

# 1 ⭐️ FOR
# To display each list item on a separate line, you can use the following code:
# If you need element indexes:

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(numbers)):
#     print(numbers[i])

# If indexes are not needed:

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     print(num)

# This loop will go through the list of numbers, giving the loop variable num the value of each element of the list (!), unlike the previous loop, in which the loop variable “ran” through the indices of the list.

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     print(num, end=" ")

# If we need to print list elements on one line, separated by spaces, we can use the optional end parameter of the print() function

# 2  List unpacking wuthout FOR

# 1) Printing list elements separated by one space character:
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(*numbers) # 0 1 2 3 4 5 6 7 8 9 10

# 2) Printing list items, each on a separate line

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(*numbers, sep="\n")

# 📌 Since strings contain characters just as lists contain elements, we can use string unpacking in the same way we use list unpacking.

# s = "Python"

# print(*s) # P y t h o n
# print() # nothing
# print(*s, sep="\n")  # each on a separate line
