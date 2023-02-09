"""Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
kk=[]
for i in a:
    b=(i[1],i[0])
    kk.append(b)
kk.sort()
out=[]
for j in kk:
    b=(j[1],j[0])
    out.append(b)
print(out)

#or
def last(n):
    return n[-1]
def final(a):
    return sorted(a,key=last)
p=final([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(p)
    
    
