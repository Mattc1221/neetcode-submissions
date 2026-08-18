class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_dups = set()
            col_dups = set()
            square_dups = set()
            for j in range(len(board[i])):
                # check rows
                if board[i][j] in row_dups: return False
                if board[i][j] != ".": row_dups.add(board[i][j])
                # check cols
                if board[j][i] in col_dups: return False
                if board[j][i] != ".": col_dups.add(board[j][i]) 
                # check square
                mapped_i = i - (i % 3) + (j // 3)
                mapped_j = (j % 3) + ((i % 3) * 3)
                if board[mapped_i][mapped_j] in square_dups: return False
                if board[mapped_i][mapped_j] != ".": square_dups.add(board[mapped_i][mapped_j])
        return True

        