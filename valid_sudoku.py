# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # dicts used to check if number already in row or col or 3 by 3 square
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                # empty space so we skip
                if board[r][c] == ".":
                    continue
                # if current row or column or 3 by 3 square already contains current number in board[r][c], then not valid
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3 , c // 3)]:
                    return False
                # otherwise, add number to respective row, column, and square to be marked as seen
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3 , c // 3)].add(board[r][c])

        # valid board if program terminates naturally
        return True
                