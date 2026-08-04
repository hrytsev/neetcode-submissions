class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for word in strs:
            while prefix not in word:
                prefix=prefix[:-1]
        return prefix