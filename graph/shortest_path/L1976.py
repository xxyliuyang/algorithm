# Dijkstra
from typing import List
import queue
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # 初始化距离、条数
        distance = [[float('inf'), 0] for i in range(n)]
        distance[0][0] = 0
        distance[0][1] = 1

        # 字典图
        graph = defaultdict(list)
        for i,j,w in roads:
            graph[i].append([j, w])
            graph[j].append([i, w])

        # 优先级队列
        q = queue.PriorityQueue()
        q.put((0, 0))

        while not q.empty():
            t, x = q.get()
            if distance[x][0] < t:
                continue

            for edge in graph[x]:
                y = edge[0]
                d = distance[x][0] + edge[1]

                if d == distance[y][0]:
                    distance[y][1] += distance[x][1]
                if d < distance[y][0]:
                    distance[y][0] = d
                    q.put((d, y))
                    distance[y][1] = distance[x][1]

        return distance[n - 1][1]

if __name__ == '__main__':
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]

    solution = Solution()
    print(solution.countPaths(n, roads))