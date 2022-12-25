# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L200.py
# Time   : 2022/12/25 12:37 PM
"""
from typing import List


class Solution:

    def bfs(self, grid, used, i, j):
        n, m = len(grid), len(grid[0])
        q = [(i, j)]
        while q:
            x, y = q.pop()
            for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                nx = x + direction[0]
                ny = y + direction[1]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1" and not used[nx][ny]:
                    q.append((nx, ny))
                    used[nx][ny] = True

    def dfs(self, grid, used, x, y):
        n, m = len(grid), len(grid[0])
        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or ny<0 or nx >= n or ny >= m:
                continue
            if grid[nx][ny] == "1" and not used[nx][ny]:
                used[nx][ny] = True
                self.bfs(grid, used, nx, ny)

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        used = [[False for _ in range(m)] for _ in range(n)]

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not used[i][j]:
                    res += 1
                    used[i][j] = True
                    self.dfs(grid, used, i, j)
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution = Solution()
    print(solution.numIslands(grid))
