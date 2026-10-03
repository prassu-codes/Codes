# RECTSQ - Rating 936

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Farmer And His Plot

Santosh has a farm at Byteland. He has a very big family to look after. His life takes a sudden turn and he runs into a financial crisis. After giving all the money he has in his hand, he decides to sell his plots. The speciality of his land is that it is rectangular in nature. Santosh comes to know that he will get more money if he sells square shaped plots. So keeping this in mind, he decides to  **divide his land into minimum possible number of square plots**, such that each plot has the  **same area**, and the  **plots divide the land perfectly**. He does this in order to get the maximum profit out of this.

So your task is to  **find the minimum number of square plots with the same area, that can be formed out of the rectangular land, such that they divide it perfectly.** 

### Input Format
- The first line of the input contains $T$, the number of test cases. Then $T$ lines follow.
- The first and only line of each test case contains two space-separated integers, $N$ and $M$, the length and the breadth of the land, respectively.
### Output Format

For each test case, print the minimum number of square plots with equal area, such that they divide the farm land perfectly, in a new line.

### Constraints

$1 \le T \le 20$
$1 \le M \le 10000$
$1 \le N \le 10000$

### Sample 1:
Input
Output

```
2
10 15
4 6

```

```
6
6

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T14:54:02.263Z  

```py
import math
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    b=math.gcd(n,m)
    print((n*m)//b**2)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/RECTSQ)