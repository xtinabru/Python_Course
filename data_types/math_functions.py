from math import *


#########################ROUND########################


# 🍎 round to 0
# n1 = int(2.7)
# print(n1)

# 🍎 round to the closest int
# n1 = round(2.6)
# print(n1)

# 🍎 round (x, n) rounds the number x to n decimal places
# n1 = round(2.5678, 2)
# print(n1)

# 🍎 floor (x) ⤵️

# x = floor(2.3)
# print(x)

# 🍎 ceil ⤴️

# x = ceil(2.3)
# print(x)

# 🍎 abs - asolute value
# x = abs(-43)
# print(x)

########################Roots, logarithms, powers and factorial################

# 🍊 square root

# x = sqrt(16)
# print(x)

# 🍊 raising number x to the power n
# x = pow(3, 2)
# print(x)

# 🍊 Logarithms:

# log(x)
# log10(x)
# log(x, b)
# factorial(n)

######################TRIGONOMETRY########################

# 🍋 :
# degrees(x)  -  transform angle x from radians to degrees
# radians(x) -  transform angle x from degrees to radians
# cos(x) - cos x in radians
# sin(x) - sin x in radians
# tan(x) - tan x in radians
# acos(x) - returns angle in radians from o to π, where cos  = x
# asin(x) - returns angle in radians from -π/2 to π/2, where sin = x
# atan(x) - return angle in radians from π/2 to π/2, whese tan  = x
# atan2(y, x) - polar angle (in radians) of a point with coordinates (x, y)

# The angular coordinate is also called the polar angle, or azimuth, and is denoted 𝜑, is equal to the angle by which the polar axis must be rotated counterclockwise in order to get to this point🍤

#    Для извлечения квадратного корня можно воспользоваться кодом n ** 0.5, вместо math.sqrt(n).🍤

# Для использования функций int(), float(), abs(), min(), max(), round() подключать модуль math нет необходимости. Это так называемые встроенные функции.

# Вызов функций pow(x, n) можно заменить использованием оператора возведения в степень: x**n.

# Импортировать функции (или любые другие объекты) из модуля можно несколькими способами:

# from math import *

# num = sqrt(10)

# from math import sqrt

# num = sqrt(10)

# import math

# num = math.sqrt(10)


# Однако рекомендуется избегать импортирования через from math import *,
# так как нет ясности, какие функции были импортированы и это загрязняет пространство имён лишними, неиспользуемыми функциями.
# Вместо этого рекомендуется использовать
# from math import sqrt или import math,
# чтобы явно указать, что именно вы импортируете. Это делает ваш код более читаемым и управляемым.
