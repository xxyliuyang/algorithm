import collections
def findRedundantConnection(edges):
    def dfs(source, target):# 是否连通
        if source not in see:
            see.add(source)
            if source == target:
                return True
            else:
                return any(dfs(nei,target) for nei in graph[source])
    graph = collections.defaultdict(set)

    for a,b in edges:
        see = set([])
        if a in graph and b in graph and dfs(a,b):
            return [a,b]
        graph[a].add(b)
        graph[b].add(a)

def findRedundantConnection3(edges):
    def dfs(a, b):
        """判断是否可达"""
        stack = [a]
        see = set([])

        while stack:
            cur = stack.pop()
            if cur == b:
                return True
            if cur not in see:
                see.add(cur)
                for t in graph[cur]:
                    stack.append(t)
        return False

    graph = collections.defaultdict(set)

    for a, b in edges:
        if a in graph and b in graph and dfs(a, b):
            return [a, b]
        graph[a].add(b)
        graph[b].add(a)


class DSU():
    def __init__(self):
        self.parent = [i for i in range(1001)]
        self.rank = [0] * 1001

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1

        return True
def findRedundantConnection4(nums):
    """并查集的解法"""
    dsu = DSU()
    for x, y in nums:
        if not dsu.union(x, y):
            return [x, y]
    return [-1, -1]

if __name__ == '__main__':
    nums = [[4,5],[1,2],[2,4],[3,4],[2,3]]
    print(findRedundantConnection4(nums))

