class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique=set(nums)
        ml=0
        for n in unique:
            current_left=n
            current_right=n
            l=1
            while current_right+1 in unique:
                current_right+=1
                l+=1
        
            while current_left-1 in unique:
                current_left-=1
                l+=1
            ml=max(ml,l)
        return ml