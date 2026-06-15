class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid_i=(r+l)//2 
            mid=nums[mid_i]
            if mid>target:
                r=mid_i-1
            elif mid<target:
                l=mid_i+1
            else:
                return mid_i
        return -1