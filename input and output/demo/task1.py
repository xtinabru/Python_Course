
a = [0]*100
print(len(a))

b = [2]
print(sum(b))

#max or min => print(max(a))

'''a = []
for i in range(100):
  a.append(i)
  print(a)'''
  
f = open("108.txt")
a = []
for s in f:
  a.append(int(s))
  print(sum(a))