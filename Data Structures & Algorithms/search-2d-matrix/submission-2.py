class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        mrows, mcols = len(matrix), len(matrix[0])

        top, bot = 0, mrows-1
        #to find row
        while top <= bot:
            mid = (top+bot)//2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not top<=bot: return False
        #to find val in row
        valrow = (top+bot)//2

        l,r = 0, mcols-1
        while l<=r:
            m = (l+r)//2
            if target < matrix[valrow][m]:
                r = m - 1
            elif target > matrix[valrow][m]:
                l = m + 1
            else:
                return True


        return False




        