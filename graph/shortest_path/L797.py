# dfs求所有路径
from typing import List
import copy
from collections import defaultdict

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def dfs(self, link_graph, index, target):
        if index == target:
            self.result.append(copy.deepcopy(self.path))
            return

        for next in link_graph[index]:
            self.path.append(next)
            self.dfs(link_graph, next, target)
            self.path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if len(graph) == 0:
            return self.result
        # 构建图
        link_graph = defaultdict(list)
        for i, target in enumerate(graph):
            link_graph[i] = target

        self.path.append(0)
        self.dfs(link_graph, 0, len(graph)-1)
        return self.result

if __name__ == '__main__':
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    solution = Solution()
    print(solution.allPathsSourceTarget(graph))