class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        candidate=nums[0]
        for v in nums:
            if cnt==0:
                candidate=v
            if candidate==v:
                cnt+=1
            else:
                cnt-=1
           
        return candidate