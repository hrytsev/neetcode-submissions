class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        current_max=0
        for n in nums:
            if n==1:
               current+=1
            else:
                current=0
            current_max=max(current_max,current)
        return current_max 