# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    f=0
    for i in a:
        if i==0:
            f+=1
        elif i<0:
            c+=1 
    if c%2!=0 and f==0:
        print(1)
    else:
        print(0)