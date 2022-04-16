from typing import List
from collections import defaultdict
import queue

class Solution:

    def min_weight_path(self, n, graph, src):
        # 初始化Dijkstra
        distance = [float("inf") for _ in range(n)]
        visited = set([])
        q = queue.PriorityQueue()
        q.put((0, src)) # 距离，目的地
        distance[src] = 0

        # 优先队列遍历
        while not q.empty():
            w1, x = q.get()
            if x in visited:
                continue
            visited.add(x)

            for y, w2 in graph[x]:
                w = w1 + w2
                if w < distance[y]:
                    distance[y] = w
                    q.put((w, y))
        return distance

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        # 构建图
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for x, y, weight in edges:
            graph[x].append((y, weight))
            reverse_graph[y].append((x, weight))

        # 最短路径算法，出发点到每个点的最短距离
        d1 = self.min_weight_path(n, graph, src1)
        d2 = self.min_weight_path(n, graph, src2)
        if d1[dest] == float("inf") or d2[dest] == float("inf"):
            return -1
        d3 = self.min_weight_path(n, reverse_graph, dest)

        # 求出最小值
        min_weight_value = float("inf")
        for i in range(n):
            w = d1[i] + d2[i] + d3[i]
            if w < min_weight_value:
                min_weight_value = w
        return min_weight_value

if __name__ == '__main__':
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2],
                           [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5

    solution = Solution()
    print(solution.minimumWeight(n, edges, src1, src2, dest))