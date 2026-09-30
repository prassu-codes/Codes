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

        