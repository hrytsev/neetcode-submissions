import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            s=(l+r)//2
            total=0
            for p in piles:
                total+=math.ceil(p/s)
            if total>h:
                l=s+1
            else:
                r=s-1
        return math.ceil((l+r)/2)