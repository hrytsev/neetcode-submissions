class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        seen=set()
        sum=0
        while sum!=1:
            sum=0
            for c in s:
                sum+=int(c)**2
            if sum in seen:
                return False
            seen.add(sum)
            s=str(sum)
        return sum==1