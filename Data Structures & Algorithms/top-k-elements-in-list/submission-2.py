from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for key in freq:
            curr_freq=freq[key]
            buckets[curr_freq].append(key)
        res=[]
        for bucket in buckets[::-1]:
            if bucket:
                for item in bucket:
                    res.append(item)
                    if len(res)==k:
                        return res
        return res