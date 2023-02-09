"""Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""


a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def delete(n):
    n.sort(reverse=True)
    for i in n:
        a.pop(i)
    print(a)
delete([0,4,5])

#or
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

    
    
