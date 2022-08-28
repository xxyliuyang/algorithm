# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree.util import build_tree, TreeNode

class Solution:
    def compare_left_and_right(self, left: TreeNode, right:TreeNode):
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left is None and right is None:
            return True
        if left.val != right.val:
            return False

        return self.compare_left_and_right(left.left, right.right) and self.compare_left_and_right(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.compare_left_and_right(root.left, root.right)

if __name__ == '__main__':
    root = [1, 2, 2, 3, 4, 4, 3]
    root = build_tree(root)

    solution = Solution()
    print(solution.isSymmetric(root))
