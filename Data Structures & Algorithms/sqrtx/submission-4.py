class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        
        l=0
        r=x//2
        res=0
        while l<=r:
            mid = (r+l)//2
            p= mid * mid
            if p==x:
                return mid
            elif p>x:
                r=mid-1
            else:
                res=mid
                l=mid+1

            
        return res