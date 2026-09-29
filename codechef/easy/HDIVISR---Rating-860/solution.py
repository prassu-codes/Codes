# cook your dish here
n=int(input())
max=0
for i in range(1,11):
    if n%i==0:
        if i>max:
            max=i
print(max)