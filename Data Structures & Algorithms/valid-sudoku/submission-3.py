class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        dim=int(n**0.5)
        row_set=[set() for _ in range(n)]
        col_set=[set() for _ in range(n)]
        block_set={(j,i): set() for j in range(dim) for i in range(dim)}
        for i in range(n):
            for j in range(n):
                current=board[i][j]
                current_col=board[j][i]
                block_index=(i//dim,j//dim)
                if current in block_set[block_index]:
                    print(f"block {block_index}: {current}, <{i},{j}>",block_set)
                    return False
                elif current !=".":
                    block_set[block_index].add(current)

                if current !=".":
                    if current not in row_set[i]:
                        row_set[i].add(current)
                    else:
                        return False
                if current_col!=".":
                    if current_col not in col_set[i]:
                        col_set[i].add(current_col)
                    else:
                        print(f"{j},{i}:{current_col}")
                        return False
           
            
            

            
        return True            