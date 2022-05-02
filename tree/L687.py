# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from tree.util import build_tree, TreeNode

class Solution:
    def __init__(self):
        self.max_lenght = 0
    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        left_length = 0
        right_lenght = 0
        if node.left and node.left.val == node.val:
            left_length = left + 1
        if node.right and node.right.val == node.val:
            right_lenght = right + 1

        self.max_lenght = max([self.max_lenght, left_length + right_lenght])
        return max(left_length, right_lenght);

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_lenght

if __name__ == '__main__':
    root = [5,4,5,1,1,5]
    root = build_tree(root)

    solution = Solution()
    print(solution.longestUnivaluePath(root))