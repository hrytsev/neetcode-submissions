
class Solution:
                
    def productExceptSelf(self,nums):
        n=len(nums)
        left_cum=[ 1 for _ in range(n)]
        right_cum=[ 1 for _ in range(n)]
        left_cum[0]=nums[0]
        for i in range(1,n):
            left_cum[i]=left_cum[i-1]*nums[i]

        nums_reverse=list(reversed(nums))
    
        right_cum[0]=nums[-1]
        for i in range(1, n):
            right_cum[i]=right_cum[i-1]*nums_reverse[i]
        print(left_cum,right_cum)


        res=[]
        for i in range(n):
            l=left_cum[i-1]
            if i==0:
                l=1
            r=right_cum[n-i-2]
            if i == n-1:
                r=1
            print(f"item={nums[i]}, l={l}, r={r}")
            res.append(l*r)
        return res
