# https://mp.weixin.qq.com/s/a5cCGw1lY3yTNQoPLr-pGQ

from tree.util import TreeNode, build_tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            None

if __name__ == '__main__':
    solution = Solution()
    nums = [3,5,1,6,2,0,8,None,None,7,4]
    p = 5
    q = 4
    root = build_tree(nums)

    result = solution.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
    print(result.val)