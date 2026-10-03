# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a  **palindrome**  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a  **palindrome**, or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

 **Example 2:** 

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

 **Example 3:** 

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

 **Constraints:** 

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 5.95%)  
**Memory:** 19.7 MB (beats 54.67%)  
**Submitted:** 2026-10-03T06:06:15.506Z  

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=""
        for i in s:
            if (i>='0' and i<='9') or (i>='a' and i<='z'):
                b+=i
            if (i>='A' and i<='Z'):
                b+=i.lower()
        l=0 
        r=len(b)-1
        while l<=r:
            if b[l] != b[r]:
                return False
            l+=1
            r-=1
        return True
        
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)