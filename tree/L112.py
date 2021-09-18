# https://mp.weixin.qq.com/s/EJr_nZ31TnvZmptBjkDGqA
# 递归是否有返回值

from typing import Optional
from tree.util import TreeNode, build_tree

class Solution:
    def traversal(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
            else:
                return False

        if root.left and self.traversal(root.left, targetSum-root.val):
            return True
        if root.right and self.traversal(root.right, targetSum-root.val):
            return True
        return False

    def traversal2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]
        while stack:
            cur, cur_sum= stack.pop()
            cur_sum += cur.val
            if cur.left is None and cur.right is None and targetSum == cur_sum:
                return True
            if cur.right:
                stack.append((cur.right, cur_sum))
            if cur.left:
                stack.append((cur.left, cur_sum))
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.traversal2(root, targetSum)





if __name__ == '__main__':
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22
    root = build_tree(nums)

    solution = Solution()
    print(solution.hasPathSum(root, 22))