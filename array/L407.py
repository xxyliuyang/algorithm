from typing import List
from queue import PriorityQueue

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row = len(heightMap)
        col = len(heightMap[0])
        if row <= 2 or col <= 2:
            return 0

        q = PriorityQueue()
        visible = [[False for _ in range(col)] for _ in range(row)]

        for i in range(row):
            q.put((heightMap[i][0], i, 0))
            q.put((heightMap[i][col-1], i, col-1))
            visible[i][0] = True
            visible[i][col-1] = True
        for i in range(1, col-1): # 注意重复
            q.put((heightMap[0][i], 0, i))
            q.put((heightMap[row-1][i], row-1, i))
            visible[0][i] = True
            visible[row-1][i] = True

        total = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while not q.empty():
            h, x, y = q.get()
            for direction in directions:
                nx, ny = x+direction[0], y+direction[1]
                if nx < 0 or nx >= row or ny < 0 or ny >= col or visible[nx][ny]:
                    continue
                if heightMap[nx][ny] < h:
                    total += h - heightMap[nx][ny]
                q.put((max(heightMap[nx][ny], h), nx, ny))
                visible[nx][ny] = True
        return total

if __name__ == '__main__':
    heightMap = [[1, 4, 3, 1, 3, 2],
                 [3, 2, 1, 3, 2, 4],
                 [2, 3, 3, 2, 3, 1]]
    solution = Solution()
    print(solution.trapRainWater(heightMap))