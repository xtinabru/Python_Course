s = "cris666hello"
#print(s[8])

print("hel" in s)

s = s.replace("6", "7")
print(s)
s = s.replace("7", "5", 1)
print(s)

newSt = "crist 666 hello"
a = newSt.split()
print(a)

print("".join(a))

print(len(s))