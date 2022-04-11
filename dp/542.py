from typing import List

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])

        dp = [[max((rows, cols)) for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if (mat[i][j] == 0):
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j>0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i < rows -1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                if j < cols -1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        return dp

if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[0,0,0]]

    solution = Solution()
    predcit = solution.updateMatrix(mat)

    [print(a) for a in mat]
    print()
    [print(b) for b in predcit]
