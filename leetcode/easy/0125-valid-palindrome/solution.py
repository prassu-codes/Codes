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
        
        
        