class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_V=0
        l,r=0, len(heights)-1
        while l<=r:
            left=heights[l]
            right=heights[r]
            side=min(left,right)
            V=(r-l)*side
            max_V=max(max_V,V)
            if side==left:
                l+=1
            else:
                r-=1
        return max_V