class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            parsed="".join(sorted(s))
            group[parsed].append(s)
        return list(group.values())