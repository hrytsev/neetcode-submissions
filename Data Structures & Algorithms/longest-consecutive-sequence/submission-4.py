class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique=set(nums)
        ml=0
        for n in unique:
            current=n
            l=1
            if n-1 not in unique:
                while current+1 in unique:
                    current+=1
                    l+=1
                ml=max(ml,l)
        return ml