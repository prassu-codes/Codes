# HDIVISR - Rating 860

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Highest Divisor

You are given an integer $N$. Find the largest integer between $1$ and $10$ (inclusive) which divides $N$.

### Input

The first and only line of the input contains a single integer $N$.

### Output

Print a single line containing one integer ― the largest divisor of $N$ between $1$ and $10$.

### Constraints
- $2 \leq N \leq 1,000$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
91
```

```
7
```

### Explanation:

The divisors of $91$ are $1, 7, 13, 91$, out of which only $1$ and $7$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 7) = 7$.

### Sample 2:
Input
Output

```
24
```

```
8
```

### Explanation:

The divisors of $24$ are $1, 2, 3, 4, 6, 8, 12, 24$, out of which $1, 2, 3, 4, 6, 8$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 2, 3, 4, 6, 8) = 8$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T11:46:03.255Z  

```py
# cook your dish here
n=int(input())
max=0
for i in range(1,11):
    if n%i==0:
        if i>max:
            max=i
print(max)
```

---

[View on CodeChef](https://www.codechef.com/problems/HDIVISR)