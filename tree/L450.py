
from typing import Optional
from tree.util import TreeNode, build_tree, tree_2_array

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return node
        if node is None:
            return root

        cur = root
        pre = None
        while cur:
            pre = cur
            if node.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if node.val < pre.val:
            pre.left = node
        else:
            pre.right = node
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        cur = root
        pre = None
        while cur:
            if key == cur.val:
                break
            elif key < cur.val:
                pre = cur
                cur = cur.left
            else:
                pre = cur
                cur = cur.right

        if cur is None:
            return root

        if pre is None:
            root = None
        elif pre.left and pre.left.val == cur.val:
            pre.left = None
        else:
            pre.right = None

        root = self.insertIntoBST(root, cur.right)
        root = self.insertIntoBST(root, cur.left)
        return root



if __name__ == '__main__':
    nums = [5,3,6,2,4,None,7]
    key = 7
    solution = Solution()

    root = build_tree(nums)
    root = solution.deleteNode(root, key)

    print(tree_2_array(root))