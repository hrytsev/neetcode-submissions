class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        while l+k<=len(nums):
            window=nums[l:l+k]
            res.append(max(window))
            l+=1
        return res