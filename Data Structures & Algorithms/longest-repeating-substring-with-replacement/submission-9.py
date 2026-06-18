class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_set=defaultdict(int)
        l=0
        ml=0
        freq=0
        for r in range(len(s)):
            win_set[s[r]]+=1
            freq=max(freq,win_set[s[r]])
            while r-l+1-freq>k:
                win_set[s[l]]-=1
                l+=1

            ml=max(ml,r-l+1)
        return ml