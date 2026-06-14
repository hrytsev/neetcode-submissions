class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            current=numbers[i]
            residual=target-current
            if current in seen:
                index=seen[current]
                return [index+1,i+1]
            seen[residual]=i
        return -1