# 讲解：https://mp.weixin.qq.com/s/C_Cra0IYJne6-dlu54aEVg
# 每次在一行中选择一个位置
from typing import List
from copy import deepcopy


class Solution:
    def __init__(self, n):
        self.bound = n
        self.result = []
        self.path = [["" for _ in range(n)] for _ in range(n)]

    def check(self, row, col):
        for i in range(self.bound):
            if self.path[i][col] == "Q" or self.path[row][i] == "Q":
                return True

        directions = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
        for x, y in directions:
            i, j = row, col
            while i >= 0 and j >= 0 and i < self.bound and j < self.bound:
                if self.path[i][j] == "Q":
                    return True
                i += x
                j += y
        return False

    def backtrack(self, n, row):
        if n == 0:
            self.result.append(deepcopy(self.path))
            return

        for i in range(row, self.bound):
            for j in range(0, self.bound):
                if self.check(i, j):
                    continue
                self.path[i][j] = "Q"
                self.backtrack(n - 1, i+1)
                self.path[i][j] = ""

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return self.result
        self.backtrack(n, 0)
        return self.result


if __name__ == '__main__':
    n = 4
    solution = Solution(n)

    print(solution.solveNQueens(n))
