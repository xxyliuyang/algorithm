# Dijkstra
from typing import List
import queue
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 创建图
        graph = defaultdict(list)
        for x, y, t in times:
            graph[x-1].append((y-1, t))

        # 初始化
        distance = [float('inf') for i in range(n)] # 到每个点的距离
        distance[k-1] = 0
        q = queue.PriorityQueue()
        q.put((0, k-1)) # 【距离, 目标】
        visited = set([])

        # 基于优先级队列进行广度遍历
        while not q.empty():
            time, x = q.get()
            if x in visited:
                continue
            visited.add(x)

            for y, t in graph[x]:
                d = distance[x] + t
                if d < distance[y]:
                    distance[y] = d
                    q.put((d, y))

        m = max(distance)
        if m == float('inf'):
            return -1
        return m

if __name__ == '__main__':
    times = [[1,2,1]]
    n = 2
    k = 2

    solution = Solution()
    print(solution.networkDelayTime(times, n, k))