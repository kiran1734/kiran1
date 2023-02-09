a=[4,5,6,345,3,232,54,54,342,231,425245,2343,3,2,1]
#to print the largest number in list a
b=0
for i in a:
    if i>b:
        b=i
print(b)
#to print the smallest number in list a
c=a[0]
for j in a:
    if i<c:
        c=i
print(c)
#or u can simply use min(list) nad max(list)
print(max(a))
print(min(a))
