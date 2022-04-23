from typing import List
from tree.util import Node, buld_multi_tree

class Solution:
    def preorder(self, root: Node) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) != 0:
            cur = stack.pop()
            res.append(cur.val)
            for n in cur.children[::-1]:
                stack.append(n)
        return res


if __name__ == '__main__':
    root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
    root = buld_multi_tree(root)

    solution = Solution()
    print(solution.preorder(root))