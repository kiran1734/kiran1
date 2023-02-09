"""Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""
b=0
a=['abc', 'xyz', 'aba', '1221']
for i in a:
    if len(i)>=2:
        if i[0]==i[-1]:
            b=b+1
print(b)
        

    
