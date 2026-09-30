
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=[]
    for i in range(1,n+1):
        p.append(i)
    for j in a:
        p.remove(j)
    mini=[]
    while k>0:
        mini.append(min(p))
        p.remove(min(p))
        k-=1
    print(*mini)