import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)
    def quicksort(self,arr):
        if len(arr)<1:
            return arr
        pivot=int(random.random()*len(arr))
        left=[n for n in arr if n<arr[pivot]]
        right=[n for n in arr if n>arr[pivot]]
        mid=[n for n in arr if n==arr[pivot]]
        return self.quicksort(left) + mid + self.quicksort(right)