a=[p*p for p in range(31)]
print(a[5:])

#or
b=[]
for i in range(len(a)):
    if i>4:
        b.append(a[i])
print(b)
