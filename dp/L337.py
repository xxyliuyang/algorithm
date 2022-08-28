# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from tree.util import TreeNode, build_tree
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        pass

if __name__ == '__main__':
    root = [3, 4, 5, 1, 3, None, 1]
    root = build_tree(root)
    solution = Solution()
    print(solution.rob(root))