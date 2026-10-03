# Valid Word

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A word is considered  **valid**  if:

- It contains a minimum of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes at least one vowel.
- It includes at least one consonant.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

 **Notes:** 

- 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
- A consonant is an English letter that is not a vowel.

 

 **Example 1:** 

 **Input:**  word = "234Adas"

 **Output:**  true

 **Explanation:** 

This word satisfies the conditions.

 **Example 2:** 

 **Input:**  word = "b3"

 **Output:**  false

 **Explanation:** 

The length of this word is fewer than 3, and does not have a vowel.

 **Example 3:** 

 **Input:**  word = "a3$e"

 **Output:**  false

 **Explanation:** 

This word contains a `'$'` character and does not have a consonant.

 

 **Constraints:** 

- 1 <= word.length <= 20
- word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 71.43%)  
**Submitted:** 2026-10-03T12:08:17.315Z  

```py
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        elif not word.isalnum():
            return False
        else:
            c,f=0,0
            d=['0','1','2','3','4','5','6','7','8','9']
            vowels='aeiouAEIOU'
            for i in word:
                if i in vowels:
                    c+=1
                if ((i>'a' and i<='z') or (i>'A' and i<='Z')) and (i not in vowels) and (i not in d):
                    f+=1
            return True if (c>0 and f>0)  else False
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-word/)