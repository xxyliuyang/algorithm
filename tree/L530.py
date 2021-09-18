from typing import Optional
from tree.util import TreeNode, build_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        nums = []
        cur = root

        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                nums.append(cur.val)
                cur = cur.right

        result = float("inf")
        for i in range(1, len(nums)):
            result = min(result, nums[i]-nums[i-1])
        return result

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        def _traverse(root, result):
            if root.left:
                _traverse(root.left, result)
            result.append(root.val)
            if root.right:
                _traverse(root.right, result)

        nums = []
        _traverse(root, result=nums)

        result = float("inf")
        for i in range(1, len(nums)):
            result = min(result, nums[i] - nums[i - 1])
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,48,None,None,12,49]
    root = build_tree(nums)

    print(solution.getMinimumDifference2(root))