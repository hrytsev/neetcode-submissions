from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[item for rows in matrix for item in rows]
        l=0
        r=len(arr)-1
        while l<=r:
          mid_i=(r+l)//2
          mid=arr[mid_i]
          if mid == target:
            return True
          elif mid<target:
            l=mid_i+1
          else:
            r=mid_i-1
        return False