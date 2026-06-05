class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dots = row.count('.')
            t = len(set(row))
            if t + dots - (1 if dots else 0) != 9:
                    return False
        for i in range(9):
            curr = []
            for j in range(9):
                curr.append(board[j][i])
            dots = curr.count('.')
            t = len(set(curr))
            if t + dots - (1 if dots else 0) != 9:
                    return False
        
        for boxrow in range(0, 9, 3):
            for boxcol in range(0, 9,3):
                curr = []
                for i in range(3):
                    for j in range(3):
                        curr.append(board[boxrow + i][boxcol + j])
                
                dots = curr.count('.')
                t = len(set(curr))
                if t + dots - (1 if dots else 0) != 9:
                    return False
        return True

