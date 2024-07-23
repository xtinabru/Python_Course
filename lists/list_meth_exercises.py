# Ex 1 🔅
# colors = ["Orange"]
# colors.append("Red")
# colors.append("Blue")
# colors.append("Green")
# colors.insert(0, "Violet")
# colors.insert(2, "Purple")

# print(colors) # ['Violet', 'Orange', 'Purple', 'Red', 'Blue', 'Green']

# Ex 2 🔅

# colors = ["Red", "Blue", "Green", "Black", "White"]
# del colors[-1]
# colors.remove("Green")

# print(colors) # ['Red', 'Blue', 'Black']

# Ex 3 All at once 2 🌶️🔅

# numbers = [8, 9, 10, 11]

# numbers.pop(1)
# numbers.insert(1, 17)  # change the 2nd element - 9

# numbers.extend([4, 5, 6])  # add 4,5,6, to the end

# numbers.pop(0)  # delete 1st element

# new_numbers = numbers * 2  # double the list

# new_numbers.insert(3, 25)

# print(new_numbers)

# # or

# numbers = [8, 9, 10, 11]

# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

# Ex 4 Rearrange min and max 🔅

# seq = []
# for el in input().split():
#     seq.append(int(el))

# mx_ind = seq.index(max(seq))
# mn_ind = seq.index(min(seq))
# seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

# print(*seq)

# Ex 5 Articles🔅

# text = input().lower()

# words = text.split()

# articles = ["a", "an", "the"]

# count = sum(words.count(article) for article in articles)

# print("Общее количество артиклей:", count)

#### total_count = 0

# # Проходим по каждому артиклю в списке
# for article in articles:
#     # Считаем количество вхождений текущего артикля в списке слов
#     count = words.count(article)

#     # Добавляем количество найденных артиклей к общему счетчику
#     total_count += count

# or

# seq = input().lower().split()
# res = seq.count("a") + seq.count("an") + seq.count("the")

# print(f"Общее количество артиклей: {res}")

# Ex 6 Hack Brotherhood of Steel 🌶️🔅 ...

# first_line = input().strip()

# n = int(first_line[1:])

# for _ in range(n):
#     line = input()
#     # Удаляем комментарий (все после #) и пробелы в конце строки
#     cleaned_line = line.split("#")[0].rstrip()
#     print(cleaned_line)
