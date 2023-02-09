
def compare(a,b):
    for i in a:
        if i in b:
            return True
            break
    return False

p=compare([1,2,3,4,5],[4,6,7,8])
print(p)
