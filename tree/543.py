from tree.util import TreeNode, build_tree
from typing import Optional

class Solution:
    def __init__(self):
        self.max_length = 0
    def dfs(self, node) -> int:
        if node is None:
            return 0
        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        self.max_length = max(self.max_length, left_length + right_length + 1) # 每个节点计算完后，统计当前最大值
        return max([left_length, right_length]) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root)
        return self.max_length - 1

if __name__ == '__main__':
    root = [1,2]
    root = build_tree(root)
    solution = Solution()

    print(solution.diameterOfBinaryTree(root))