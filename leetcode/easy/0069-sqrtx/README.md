# Sqrt(x)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a non-negative integer `x`, return  *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be  **non-negative**  as well.

You  **must not use**  any built-in exponent function or operator.

- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

 **Example 1:** 

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

```

 **Example 2:** 

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

```

 

 **Constraints:** 

- 0 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 1783 ms (beats 5.00%)  
**Memory:** 19.1 MB (beats 97.88%)  
**Submitted:** 2026-09-30T11:39:17.713Z  

```py
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x==1 or x==2 or x==3:
            return 1
        else:
            for i in range(1,(x//2)+2): 
                if i*i==x:
                    return i
                    break
                if i*i>x:
                    return (i-1)
                    break

        
```

---

[View on LeetCode](https://leetcode.com/problems/sqrtx/)