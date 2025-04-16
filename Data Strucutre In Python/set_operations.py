# Set Operations 

a = {3,23,1}
b = {23,4,2,55,1}
c = a.union(b) # {3,23,1,4,2,55}
print(c)
d = a.intersection(b) # {23,1}
print(d) 
e = a.difference((b)) # 3
print(e)