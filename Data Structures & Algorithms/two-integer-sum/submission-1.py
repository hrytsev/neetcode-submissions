class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i,v in enumerate(nums):
            if v in res:
                return [res[v],i]
            residual=target-v
            res[residual]=i
        return [-1,-1]