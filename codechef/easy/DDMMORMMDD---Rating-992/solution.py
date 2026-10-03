t=int(input())
for _ in range(t):
    s=input()
    c=""
    d=""
    for i in range(len(s)):
        if i in [0,1]:
            c+=(s[i])
        if i in [3,4]:
            d+=(s[i])
    c=int(c)
    d=int(d)
    if c<=12 and d<=12:
        print("both")
    elif c>12:
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")
        