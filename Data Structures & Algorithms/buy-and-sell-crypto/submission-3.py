class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        lowest_buy=prices[0]
        for n in prices:
            lowest_buy=min(lowest_buy,n)
            profit=max(profit,n-lowest_buy)
        return profit 
