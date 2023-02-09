a= [1, 3, 5, 7, 9]
b=[1, 2, 4, 6, 7, 8]
c=list(set(a)-set(b))
d=list(set(b)-set(a))
print(c+d)


#or

print(list(set(a)^set(b)))
