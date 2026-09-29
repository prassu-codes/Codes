# NONNEGPROD - Rating 948

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Non-Negative Product

Alice has an array of $N$ integers — $A_1, A_2, \ldots, A_N$. She wants the product of all the elements of the array to be a non-negative integer. That is, it can be either $0$ or positive. But she doesn't want it to be negative.

To do this, she is willing to remove some elements of the array. Determine the minimum number of elements that she will have to remove to make the product of the array's elements non-negative.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases. The first line of each test case contains a single integer $N$ — the number of elements in the array originally. The next line contains $N$ space-separated integers — $A_1, A_2, \ldots, A_N$, which are the original array elements.
### Output Format

For each test case, output on a new line the minimum number of elements that she has to remove from the array.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 10000$
- $-1000 \leq A_i \leq 1000$
### Sample 1:
Input
Output

```
4
3
1 9 8
4
2 -1 9 100
4
2 -1 0 100
4
2 -1 -1 100

```

```
0
1
0
0

```

### Explanation:

 **Test case $1$:**  The product of the elements of the array is $1 \times 9 \times 8 = 72$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

 **Test case $2$:**  The product of the elements of the array is $2 \times -1 \times 9 \times 100 = -1800$, which is negative. Alice can remove the element $-1$, and the product then becomes non-negative. Hence the answer is $1$.

 **Test case $3$:**  The product of the elements of the array is $2 \times -1 \times 0 \times 100 = 0$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

 **Test case $4$:**  The product of the elements of the array is $2 \times -1 \times -1 \times 100 = 200$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T12:02:56.065Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/NONNEGPROD)