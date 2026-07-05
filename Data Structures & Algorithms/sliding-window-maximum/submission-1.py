import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        while l+k<=len(nums):
            window=nums[l:l+k]
            heapq.heapify_max(window)
            res.append(heapq.heappop(window))
            l+=1
        return res