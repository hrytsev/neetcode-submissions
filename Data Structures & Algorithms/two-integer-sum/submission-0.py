class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(nums):
            residual=target-n
            if n in seen:
                return [seen[n],i]
            else:
                seen[residual]=i
        return -1                 