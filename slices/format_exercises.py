# Exercise 1 What will print? 🔻🔻🔻

# planet = 'Arrakis'
# bad_guys = 'Harkonnens'
# text = 'The desert planet {}, rich in valuable spice, is exploited by cruel {}.'.format(planet, bad_guys)

# print(text)    # The desert planet Arrakis, rich in valuable spice, is exploited by cruel Harkonnens.

# Exercise 2 What will print? 🔻🔻🔻

# name = "Leto Atreides"
# planet = "Caladan"
# text = "Duke {1} is the ruler of the planet {0}.".format(planet, name)

# In this line, {0} and {1} are placeholders for the format() arguments.

# print(text)  # Duke Leto Atreides is the ruler of the planet Caladan.

# Exercise 3 What will print? 🔻🔻🔻

# name = 'Dune'
# text = f'The novel "{name}" was published in 1965 by Frank Herbert.'

# print(text)  # The novel "Dune" was published in 1965 by Frank Herbert.

# Exercise 4 What will print? 🔻🔻🔻

# name = "Imperium"
# text = "For the {name} spice is used by the navigators to find safe paths between the stars."

# print(text)

# Exercise 5 What will print if version 3.12? 🔻🔻🔻

# text = f'By Imperial decree, Leto Atreides is now the fief of the planet {'Arrakis'}.'
# print(text)


# TASK 1 🔷🔷🔷

# Using the format() method, complete the following code to output the text:
# In 2010, someone paid 10k Bitcoin for two pizzas.


# s = "In {0}, someone paid {1} {2} for two pizzas."

# print(s.format(2010, "10k", "Bitcoin"))


# TASK 2 🔷🔷🔷
# Using f-string

# s = f'In {2010}, someone paid {"10K"} {"Bitcoin"} for two pizzas.'

# print(s)


# TASK 3 Exchange rates 💹

# current_date = input()
# dollar = input()
# yuan = input()

# text = f"На {current_date}: 1$ = {dollar}₽, 1¥ = {yuan}₽"

# print(text)


# TASK 4 Sum of Cubes 🆚 Cube of Sum

# a = int(input())
# b = int(input())

# sum_of_cubes = a**3 + b**3
# cube_of_sum = (a + b) ** 3

# text = f"""Для чисел {a} и {b}:
#   Сумма кубов: {a}**3 + {b}**3 = {sum_of_cubes}
#   Куб суммы: ({a} + {b})**3 = {cube_of_sum}"""
# print(text)


# TASK 5 WEIGHT 🏃🌶️


# day = int(input())
# current_weight = float(input())

# initial_weight = 100
# final_weight = 88
# days = 60
# weight_loss_per_day = (initial_weight - final_weight) / days

# target_weight = initial_weight - weight_loss_per_day * day

# if current_weight <= target_weight:
#     print("Все идет по плану")
# else:
#     print("Что-то пошло не так")

# print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight:.1f} кг")
