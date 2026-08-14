class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parsed=s.split()
        return len(parsed[-1])