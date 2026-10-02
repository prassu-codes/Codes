class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b=""
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                b+=s[i]
                if s[i-1] ==' ':
                    break 
        return len(b)
