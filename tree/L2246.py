# 多叉树后根递归遍历：对递归的的控制
# 题目：对多叉树，相邻节点不同字符的最大长度
# 路径：并不是必须是根节点，关键的难点是如何向上聚出更长的路径
"""
步骤：

构建图的邻接矩阵；
枚举树中的节点 u，计算以该节点为 根 的最长路径的长度，记录下最大值即可得到最终的答案；
"""

from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.max_length = 0

    def dfs(self, tree, s, cur_node) -> int:
        """
        求出当前节点的最大长度
        """
        max1, max2 = 0, 0  # max1、max2： u 的子树中，与 x 字符不同且合法路径最长及次长的长度

        # 求最长子树的长度
        for v in tree[cur_node]:
            num = self.dfs(tree, s, v)
            if s[cur_node] != s[v]:
                if num > max1:
                    max2 = max1
                    max1 = num
                elif num > max2:
                    max2 = num
        self.max_length = max(self.max_length, max1 + max2 + 1) # 每个节点计算完后，统计当前最大值
        return max1 + 1

    def longestPath(self, parent: List[int], s: str) -> int:
        # 多叉树表示
        tree = defaultdict(list)
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        self.dfs(tree, s, 0)

        return self.max_length

if __name__ == '__main__':
    parent = [-1]
    s = "a"

    solution = Solution()
    print(solution.longestPath(parent, s))