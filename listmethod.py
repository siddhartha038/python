l = [1,2,4,6]
print(l)
l.append(9)
#append keep last element in the list
print(l)
l.sort(reverse=True)
print(l)

m=l.copy
m = [5,3,8]
l.extend(m)
print(m)
