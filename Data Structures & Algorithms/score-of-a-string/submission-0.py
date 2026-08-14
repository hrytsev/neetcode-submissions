class Solution:
    def scoreOfString(self, s: str) -> int:
        ords=[ord(c) for c in s]
        sum=0
        for i,v in enumerate(ords[:-1]):
            sum+=abs(ords[i]-ords[i+1])
        print(sum)
        return sum
