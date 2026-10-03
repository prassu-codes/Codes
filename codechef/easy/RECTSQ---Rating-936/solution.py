import math
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    b=math.gcd(n,m)
    print((n*m)//b**2)
    