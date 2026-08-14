class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right=-1
        res=[]
        for n in arr[::-1]:
            res.append(max_right)
            max_right=max(max_right,n)
        return list(reversed(res))