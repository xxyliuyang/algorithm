# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : 695.py
# Time   : 2023/1/8 10:40 AM
# Author : liuyang09
"""
"""
深度优先 vs 广度优先
"""
from typing import List


class Solution:

    def bfs(self, grid, used, i, j):
        row_num = len(grid)
        col_num = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        area = 0
        q = [(i, j)]
        used[i][j] = True
        while q:
            x, y = q.pop()
            area += 1
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx < row_num \
                        and 0 <= ny < col_num \
                        and grid[nx][ny] == 1 \
                        and not used[nx][ny]:
                    used[nx][ny] = True
                    q.append((nx, ny))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        used = [[False for _ in range(col_num)] for _ in range(row_num)]

        max_area = 0
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == 1 and not used[i][j]:
                    area = self.bfs(grid, used, i, j)
                    max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

    solution = Solution()
    print(solution.maxAreaOfIsland(grid))
