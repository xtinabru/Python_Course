# Method insert() 💜

# The insert() method allows you to INSERT a value into a LIST at a given position. Two arguments are passed to it:

#         INDEX: index specifying where the value is inserted;
#         VALUE: the value to be inserted.

# ➰ When a value is inserted into a list, the list expands in size to accommodate the new value. The value that was previously at the given index position and all elements after it are shifted one position to the end of the list.

# names = ["Gvido", "Roman", "Timur"]
# print(names) # ['Gvido', 'Roman', 'Timur']
# names.insert(0, "Anders")
# print(names) # ['Anders', 'Gvido', 'Roman', 'Timur']
# names.insert(3, "Josef")
# print(names) # ['Anders', 'Gvido', 'Roman', 'Josef', 'Timur']

# ➰ If an invalid index is specified, no error occurs during program execution. If an index is given beyond the end of the list, the value will be added to the end of the list. If a negative index is applied, which indicates an invalid position, then the value will be inserted at the beginning of the list.


# Method index() 💜

# The index() method returns the INDEX of the FIRST element whose value is equal to the value passed to the method. Thus, one parameter is passed to the method:
# value: the value whose index you want to find.

# ➰ If an element in the list is not found, an error occurs at runtime.

# names = ["Gvido", "Roman", "Timur"]
# position = names.index("Timur")
# print(position) # 2

# names = ["Gvido", "Roman", "Timur"]
# position = names.index("Anders")
# print(position) # ValueError: 'Anders' is not in list

# ➰ To avoid such errors, you can use the index() method along with the in membership operator:

# names = ["Gvido", "Roman", "Timur"]
# if "Anders" in names:
#     position = names.index("Anders")
#     print(position)
# else:
#     print("Такого значения нет в списке")

# Method remove() 💜

# The remove() method removes the first element whose value is equal to the value passed to the method. One parameter is passed to the method:
#       value: The value to be removed

# ➰ The method reduces the size of the list by one element. All elements after the deleted element are shifted one position to the beginning of the list. If an element in the list is not found, an error occurs at runtime.

# food = ["Рис", "Курица", "Рыба", "Брокколи", "Рис"] #
# print(food) # ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# food.remove("Рис")
# print(food) # ['Курица', 'Рыба', 'Брокколи', 'Рис']

# ❕ Important: the remove() method only removes the first element with the specified value. All subsequent occurrences of it remain in the list. To remove all occurrences, you need to use a while loop in conjunction with the in membership operator and the remove method.

# Method pop() 💜

# The pop() method removes the element at the specified index and returns it. The pop() method is passed one optional argument:

#            index: The index of the element to be removed.

# ➰ If the index is not specified, then the method removes and returns the last element of the list. If the list is empty or the index specified is out of range, an error occurs at runtime.

# names = ["Gvido", "Roman", "Timur"]
# item = names.pop(1)
# print(item) # Roman
# print(names) # ['Gvido', 'Timur']

# Method count() 💜

# The count() method returns the number of elements in the list whose values ​​are equal to the value passed to the method.

# One parameter is passed to the method:
#          value: value, the number of elements equal to which should be counted.
# ➰ If the value is not found in the list, the method returns 0.

# names = ["Timur", "Gvido", "Roman", "Timur", "Anders", "Timur"]
# cnt1 = names.count("Timur")
# cnt2 = names.count("Gvido")
# cnt3 = names.count("Josef")

# print(cnt1) # 3
# print(cnt2) # 1
# print(cnt3) # 0

# Method reverse() 💜

# The reverse() method reverses the order of values ​​in the list, that is, it changes it to the opposite.

# names = ["Gvido", "Roman", "Timur"]
# names.reverse()
# print(names) # ['Timur', 'Roman', 'Gvido']

# ❕ There is a big difference between calling the names.reverse() method and using the names[::-1] slice. The reverse() method reverses the order of the elements in the current list, and the slice creates a copy of the list with the elements in reverse order.

# Method clear() 💜

# The clear() method removes all elements from the list.

# names = ["Gvido", "Roman", "Timur"]
# names.clear()
# print(names) # []

# Method copy() 💜

# The copy() method creates a shallow copy of the list.

# names = ["Gvido", "Roman", "Timur"]
# names_copy = names.copy()  # создаем поверхностную копию списка names

# print(names) # ['Gvido', 'Roman', 'Timur']
# print(names_copy) # ['Gvido', 'Roman', 'Timur']

# ➰ A similar result can be achieved using slices or the list() function:

# names = ['Gvido', 'Roman' , 'Timur']
# names_copy1 = list(names)
# # создаем поверхностную копию с помощью функции list()

# names_copy2 = names[:]
# # создаем поверхностную копию с помощью среза от начала до конца
