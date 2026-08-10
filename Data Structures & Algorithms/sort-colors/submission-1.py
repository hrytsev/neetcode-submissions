import heapq
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        swap=True
        while swap:
            swap=False
            for i,v in enumerate(nums[:-1]):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    swap=True
        