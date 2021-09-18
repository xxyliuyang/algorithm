from typing import Optional
from tree.util import TreeNode, build_tree, tree_2_array

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        cur = root
        pre = None
        while cur:
            pre = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val < pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root



if __name__ == '__main__':
    nums = [4,2,7,1,3]
    val = 5
    solution = Solution()

    root = build_tree(nums)
    solution.insertIntoBST(root, val)

    print(tree_2_array(root))