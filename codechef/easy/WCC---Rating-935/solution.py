t=int(input())
for _ in range(t):
    x=int(input())
    a=input() 
    c,n=0,0
    for i in a:
        if i=='C':
            c+=2
        elif i=='N':
            n+=2 
        else:
            c+=1
            n+=1
    if c==n:
        print(55*x)
    elif c>n:
        print(60*x)
    else:
        print(40*x)
    
