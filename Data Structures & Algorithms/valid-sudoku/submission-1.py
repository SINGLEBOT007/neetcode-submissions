class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # easy method check row, col, and box individually

        # for i in range(9):
        #     s = set()
        #     for j in range(9):
        #         temp = board[i][j]
        #         if temp in s:
        #             return False
        #         elif temp != '.':
        #             s.add(temp)
        
        # for i in range(9):
        #     s = set()
        #     for j in range(9):
        #         temp = board[j][i]
        #         if temp in s:
        #             return False
        #         elif temp != '.':
        #             s.add(temp)

        # boxes = [(0,0),(0,3),(0,6)
        #         ,(3,0),(3,3),(3,6)
        #         ,(6,0),(6,3),(6,6)]

        # for i,j in boxes:
        #     s = set()
        #     for row in range(i,i+3):
        #         for col in range(j,j+3):
        #             temp = board[row][col]
        #             if temp in s:
        #                 return False
        #             elif temp!= '.':
        #                 s.add(temp)

        # return True

        # approch 2 !

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqrs[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[(r//3,c//3)].add(board[r][c])
        return True


                


