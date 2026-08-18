class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_dups = set()
            col_dups = set()
            square_dups = set()
            for j in range(len(board[i])):
                # check rows
                value = board[i][j]
                if value != "." and value in row_dups: return False
                else: row_dups.add(value)
                # check cols
                value = board[j][i]
                if value != "." and value in col_dups: return False
                else: col_dups.add(value) 
                # check square
                mapped_i = i - (i % 3) + math.floor(j / 3)
                mapped_j = (j % 3) + ((i % 3) * 3)
                value = board[mapped_i][mapped_j]
                if value != "." and value in square_dups: return False
                else: square_dups.add(value)
        return True

        