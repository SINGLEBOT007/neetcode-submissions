class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # easy method check row, col, and box individually

        for i in range(9):
            s = set()
            for j in range(9):
                temp = board[i][j]
                if temp in s:
                    return False
                elif temp != '.':
                    s.add(temp)
        
        for i in range(9):
            s = set()
            for j in range(9):
                temp = board[j][i]
                if temp in s:
                    return False
                elif temp != '.':
                    s.add(temp)

        boxes = [(0,0),(0,3),(0,6)
                ,(3,0),(3,3),(3,6)
                ,(6,0),(6,3),(6,6)]

        for i,j in boxes:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    temp = board[row][col]
                    if temp in s:
                        return False
                    elif temp!= '.':
                        s.add(temp)

        return True