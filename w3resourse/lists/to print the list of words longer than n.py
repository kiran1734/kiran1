
def listofwords(n,a):
    b=a.split()
    c=[]
    for i in b:
        if len(i)>n:
            c=c+[i]
    print(c)
listofwords(3,"The quick brown fox jumps over the lazy dog")
        
