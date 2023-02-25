from typing import List

class Solution:
    def __init__(self):
        self.count = 0

    def bfs(self, x, y, grid):
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(x, y)]

        area = 0
        used = {(x, y)}
        while queue:
            x, y = queue.pop()
            for dir in directions:
                nx, ny = x + dir[0], y + dir[1]
                if 0<= nx < n and 0<=ny<m and (nx, ny) not in used and grid[nx][ny]==1:
                    used.add((nx, ny))
                    queue.append((nx, ny))
                    area += 1
        return area


    def largestIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])

        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, self.bfs(i, j, grid)+1)
        return res


    # ======
    def get_island_area_by_dfs(self, grid, used, x, y, island_number):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        m = len(grid[0])
        if not(0<= x < n and 0<=y<m):
            return
        if grid[x][y] == 0 or used[x][y]==1:
            return

        grid[x][y] = island_number
        self.count += 1
        for dir in directions:
            self.get_island_area_by_dfs(grid, used, x+dir[0], y+dir[1], island_number)

    def set_island_numbert_and_get_area_map(self, grid):
        n = len(grid)
        m = len(grid[0])
        used = [[0 for _ in range(m)] for _ in range(n)]

        island_number = 2
        island_number_2_area = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.count = 0
                    self.get_island_area_by_dfs(grid, used, i, j, island_number)
                    island_number_2_area[island_number] = self.count
                    island_number += 1
        return island_number_2_area


    def largestIsland2(self, grid: List[List[int]]) -> int:
        island_number_2_area = self.set_island_numbert_and_get_area_map(grid)

        n = len(grid)
        m = len(grid[0])
        if sum(island_number_2_area.values()) == n*m:
            return n*m

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        res = 0
        for i in range(n):
            for j in range(m):
                island_area = 1
                if grid[i][j] == 0:
                    island_number_used = set([])
                    for dir in directions:
                        nx = i + dir[0]
                        ny = j + dir[1]

                        if not (0 <= nx < n and 0 <= ny < m):
                            continue
                        island_number = grid[i][j]
                        if island_number in island_number_used or island_number not in island_number_2_area:
                            continue
                        island_area += island_number_2_area[grid[nx][ny]]
                        island_number_used.add(island_number)
                    res = max(island_area, res)
        return res


if __name__ == '__main__':
    grid = [[1,0],[0,1]]
    solution = Solution()
    print(solution.largestIsland(grid))