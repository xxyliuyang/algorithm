# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L226.py
# Time   : 2023/9/10 18:33
# Author : liuyang09
"""
from typing import Optional

from tree.util import build_tree, TreeNode, tree_2_array


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left

if __name__ == "__main__":
    solution = Solution()
    nums = [4,2,7,1,3,6,9]
    root = build_tree(nums)

    solution.invertTree(root)
    print(tree_2_array(root))