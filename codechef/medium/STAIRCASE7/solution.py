t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1,0,-1):
        if (a[i]-a[i-1])!=1:
            a[i-1]=(a[i]-1)
            c+=1 
    print(c)