from typing import Optional, List
from tree.util import TreeNode, build_tree

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root

        max_value = None
        max_count = 0
        pre_value = None
        pre_count = 0

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre_value is None:
                    pre_count = 1
                    pre_value = cur.val
                elif cur.val == pre_value:
                    pre_count += 1
                else:
                    if pre_count > max_count:
                        max_count = pre_count
                        max_value = pre_value
                    pre_count = 1
                    pre_value = cur.val
                cur = cur.right

        if pre_count > max_count:
            max_value = pre_value
        return max_value

    def findMode2(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        nums = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                nums.append(cur.val)
                cur = cur.right

        if len(nums) == 1:
            return nums[0]

        max_value = 0
        max_count = 0
        cur_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_value = nums[i-1]
                cur_count = 1
        if cur_count > max_count:
            max_value = nums[i-1]
        return max_value

if __name__ == '__main__':
    solution = Solution()
    nums = [1,None,2,2]
    root = build_tree(nums)

    print(solution.findMode(root))