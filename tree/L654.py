# https://mp.weixin.qq.com/s/TiyD9eRDBfisXozKu6KObQ?forceh5=1
# 递归是否处理空值，是根据是否传入空的case

from typing import List, Optional
from tree.util import TreeNode, build_tree, tree_2_array


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_index = nums.index(max(nums))
        root = TreeNode(nums[max_index])
        if max_index > 0:
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
        if max_index < len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root


    def constructMaximumBinaryTree2(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        max_index = nums.index(max(nums))
        root = TreeNode(nums[max_index])
        root.left = self.constructMaximumBinaryTree2(nums[:max_index])
        root.right = self.constructMaximumBinaryTree2(nums[max_index + 1:])

        return root

if __name__ == '__main__':
    nums = [3,2,1]
    solution = Solution()
    root = solution.constructMaximumBinaryTree2(nums)
    print(tree_2_array(root))


