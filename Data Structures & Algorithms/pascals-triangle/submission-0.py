class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        for row_l in range(2,numRows):
            prev=res[-1]
            row=[]
            for i in range(row_l+1):
                if i==0 or i==row_l:
                    row.append(1)
                else:
                    row.append(prev[i]+prev[i-1])
            res.append(row)

        return res[:numRows]