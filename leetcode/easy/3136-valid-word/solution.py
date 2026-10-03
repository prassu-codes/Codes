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
        
        