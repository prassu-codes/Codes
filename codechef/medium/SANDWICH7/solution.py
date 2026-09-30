# cook your dish here
b,h,c=map(int,input().split())
p=c+h 
c=0
while b>=2 and p>0:
    b-=2
    p-=1
    c+=1 
print(c)