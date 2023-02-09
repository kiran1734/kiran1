a=[2,34,1,2,4,3,23,354,23,354,3,4,3,2,1,34,54]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
for j in b:
    print(j,"--",a.count(j))
