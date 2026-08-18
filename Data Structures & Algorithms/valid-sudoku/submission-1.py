class Solution:
    """
    i: 3, j: 7

    (i * 9) + j = num

    mapped_i = i + floor(j / 3)
    mapped_j = j % 3
    i = 0: 0,0 - 0,1 - 0,2
           1,0 - 1,1 - 1,2
           2,0 - 2,1 - 2,2

    mapped_i = i + floor(j / 3)
    mapped_j = (j % 3) + i % 3
    i = 1: 0,3 - 0,4 - 0,5
           1,3 - 1,4 - 1,5
           2,3 - 2,4 - 2,5

    i = 4: 

        0  1  2    3  4  5    6  7  8
    0: 00 01 02 | 09 10 11 | 18 19 20 
    1: 03 04 05 | 12 13 14 | 21 22 23 
    2: 06 07 08 | 15 16 17 | 24 25 26
       ------------------------------ 
    3: 27 28 29 | 36 37 38 | 45 46 47 
    4: 30 31 32 | 39 40 41 | 48 49 50 
    5: 33 34 35 | 42 43 44 | 51 52 53
       ------------------------------ 
    6: 54 55 56 | 63 64 65 | 72 73 74 
    7: 57 58 59 | 66 67 68 | 75 76 77 
    8: 60 61 62 | 69 70 71 | 78 79 80 
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_dups = set()
            col_dups = set()
            square_dups = set()
            for j in range(len(board[i])):
                # check rows
                value = board[i][j]
                if value != "." and value in row_dups: 
                    print("ROW: ", value, " AT: ", i, j)
                    return False
                else: row_dups.add(value)
                # check cols
                value = board[j][i]
                if value != "." and value in col_dups: 
                    print("COL: ", value, " AT: ", i, j)
                    return False
                else: col_dups.add(value) 
                # check square
                mapped_i = i - (i % 3) + math.floor(j / 3)
                mapped_j = (j % 3) + ((i % 3) * 3)
                value = board[mapped_i][mapped_j]
                if value != "." and value in square_dups: 
                    print("SQUARE: ", value, " AT: ", i, j, " MAPPED: ", mapped_i, mapped_j, square_dups)
                    return False
                else: square_dups.add(value)
        return True



board=[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

        