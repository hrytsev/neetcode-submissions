from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        filtered=list(map(lambda pair:pair[0],sorted(freq.items(),key=lambda pair:pair[1],reverse=True)))[:k]
        
        return filtered