t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n):
        if (a[i]-1 not in a) and a[i]>0 and (a[i]-1)>=0:
            a[i]=a[i]-1 
            c+=1 
    if c%2==0:
        print("Bob")
    else:
        print("Alice")