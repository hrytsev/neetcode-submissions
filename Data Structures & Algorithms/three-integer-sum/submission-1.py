class Solution:
    def threeSum(self,nums):
        res=[]
        arr=sorted(nums)
        seen=set()
        for i,v in enumerate(arr):
            if v in seen:
                continue
            seen.add(v)
            l=i+1
            r=len(arr)-1
            while l<r:
                threeSum=-arr[l]-arr[r]
                if threeSum<v:
                    r-=1
                elif threeSum>v:
                    l+=1
                elif threeSum==v:
                    res.append([arr[i],arr[l],arr[r]])
                    l += 1
                    r -= 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
        return res
        