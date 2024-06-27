# Ex 1 💚

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)


# 123
# 345

# 1 3
# 1 4
# 1 5
# 2 3
# 2 4
# 2 5
# 3 3
# 3 4
# 3 5

# Ex 2 💚

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end="")


# # 1 2 3
# # 3 4


# # 1 3 + 4

# # 1 4 + 5

# # 2 3 5
# # 2 4 6
# # 3 3 6
# # 3 4 7


# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)


# 99 100 101

# c0 i99 t99  => c1 t9
# while 9>0 => c2 t0
# while 0>0 ----------------
# for i100 t100 100>0 => c3 t10
# while t10>0 c4 => t10//10 = t1
# while t1>0 => c5 t1//10 =t0
# while 0>0 _ _ _ _ _ _ _ _
# for i=101, t101 101>0 => c6 t101//10 = t10
# while t10>0 => c7 t10//10 =t1
# while t1>0 => c8 t1//10 = t0
# while t0>0 --------------
# for...----------
# print 8
