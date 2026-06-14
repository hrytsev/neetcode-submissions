class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l,r=0,0
        profit=0
        while r<n:
            left=prices[l]
            right=prices[r]
            if left<right:
                profit=max(profit,right-left)
            else:
                l=r
            r+=1
        return profit