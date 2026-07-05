class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        l_max=0
        r_max=0
        res=0
        while l<r:
            if height[l]>height[r]:
                r_max=max(r_max,height[r])
                res+=r_max-height[r]
                r-=1
            else:
                l_max=max(l_max,height[l])
                res+=l_max-height[l]
                l+=1
        return res
