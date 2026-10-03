# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    summ=0
    for i in range(1,n+1):
        summ+=a[i-1]
        d=(summ/i)*100
        if d==100:
            c+=1 
    print(c)