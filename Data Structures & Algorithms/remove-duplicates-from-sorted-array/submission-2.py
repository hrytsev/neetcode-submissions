class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        l=0
        while l<len(nums):
            tmp=nums[l]
            if nums[l]==prev:
                del nums[l]
            else:
                l+=1

            prev=tmp
        return len(nums)