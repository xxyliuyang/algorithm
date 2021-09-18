# https://mp.weixin.qq.com/s/EJr_nZ31TnvZmptBjkDGqA
# 递归是否有返回值

import copy
from typing import Optional, List
from tree.util import TreeNode, build_tree

class Solution:
    def traversal(self, root: Optional[TreeNode], targetSum: int, result, path) -> bool:
        if root.left is None and root.right is None and targetSum == root.val:
            path.append(root.val)
            result.append(copy.deepcopy(path))
            return
        if root.left:
            path.append(root.val)
            self.traversal(root.left, targetSum-root.val, result, path)
            path.pop()
        if root.right:
            path.append(root.val)
            self.traversal(root.right, targetSum-root.val, result, path)
            path.pop()

    def traversal2(self, root: Optional[TreeNode], targetSum: int, result) -> bool:

        stack = [(root, 0, [])]
        while stack:
            cur, cur_sum, path = stack.pop()
            cur_sum += cur.val
            path.append(cur.val)

            if cur.left is None and cur.right is None and targetSum == cur_sum:
                result.append(copy.deepcopy(path))
            if cur.right:
                stack.append((cur.right, cur_sum, copy.deepcopy(path)))
            if cur.left:
                stack.append((cur.left, cur_sum, copy.deepcopy(path)))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if root is None:
            return result

        self.traversal(root, targetSum, result, [])
        return result


if __name__ == '__main__':
    nums = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    root = build_tree(nums)

    solution = Solution()
    print(solution.pathSum(root, 22))