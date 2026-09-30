t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ma={}
    maxfreq=0
    for i in range(n):
        v=a[i]-i
        if v not in ma:
            ma[v]=1
        else:
            ma[v]+=1
        maxfreq=max(ma[v],maxfreq)
    print(n-maxfreq)