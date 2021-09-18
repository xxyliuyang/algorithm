"""
判断二叉树的最小深度
"""
from typing import Optional
from tree.util import TreeNode, build_tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 1
        queue = [root]
        while queue:
            queue_tmp = []
            for node in queue:
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue_tmp.append(node.left)
                if node.right:
                    queue_tmp.append(node.right)
            queue = queue_tmp
            depth += 1
        return depth

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        if root.left is None:
            return self.minDepth2(root.right) + 1
        elif root.right is None:
            return self.minDepth2(root.left) + 1
        else:
            return min(self.minDepth2(root.left), self.minDepth2(root.right)) + 1

if __name__ == '__main__':
    nums = [1,2]

    root = build_tree(nums)

    solution = Solution()
    print(solution.minDepth2(root))