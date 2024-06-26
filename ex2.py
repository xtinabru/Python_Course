# Exercise 1
# Smallest prime factor // Наименьший делитель 🤏🏻

# n = int(input())

# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# Exercise "Follow the rules"🫰🏻

n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    elif 17 < i < 37:
        continue
    elif 78 < i < 87:
        continue
    print(i)
