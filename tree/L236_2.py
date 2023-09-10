# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L236_2.py
# Time   : 2023/9/10 17:10
# Author : liuyang09
"""
from tree.util import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if root is None:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    root = build_tree(nums)

    result = solution.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
    print(result.val)
