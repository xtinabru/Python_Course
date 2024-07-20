# 1 Line by line output 🎀

# text = input()

# print(*text.split(), sep="\n")

# 2 Initials 🎀

# fullname = input()

# parts = fullname.split()

# initials = ""

# for part in parts:
#     initials += part[0] + "."

# print(initials)

# 2 Windows OS 🎀

# file_name = input()

# parts = file_name.split("\\")

# print("\n".join(parts))

# # or

# for part in parts:
#     print(part)

# 3 Diagram 🎀

# text = input()

# lines = text.split()

# for line in lines:
#     num = int(line)
#     print("+" * num)

# 4 Correct IP address 🎀

# ip_address = input()

# ip_numbers = ip_address.split(".")

# if len(ip_numbers) != 4:
#     print("НЕТ")
# else:
#     is_valid = True
#     for num in ip_numbers:
#         num = int(num)
#         if not (0 <= num <= 255):
#             is_valid = False
#             break

#     if is_valid:
#         print("ДА")
#     else:
#         print("НЕТ")
# or

# seq = input().split(".")

# for el in seq:
#     if not (0 <= int(el) <= 255):
#         print("НЕТ")
#         break
# else:
#     print("ДА")

# 5 Add separator 🎀

# text = input()
# separator = input()
# output = separator.join(text)
# print(output)

# 6 Number of matching pairs 🎀

# text = input()

# my_list = text.split()
# pairs = 0

# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             pairs += 1
# print(pairs)
