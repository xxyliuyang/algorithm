"""
遍历：递归三要素
1. 确定递归函数的参数和返回值:
2. 确定终止条件:
3. 确定单层递归的逻辑:
"""
from tree.util import build_tree

def pre_traversal(root):
    def _traverse(root, result):
        if root is None:
            return
        result.append(root.val)
        _traverse(root.left, result)
        _traverse(root.right, result)

    result = []
    _traverse(root, result=result)
    print(result)

def in_traversal(root):
    def _traverse(root, result):
        if root is None:
            return
        _traverse(root.left, result)
        result.append(root.val)
        _traverse(root.right, result)

    result = []
    _traverse(root, result=result)
    print(result)

def post_traversal(root):
    def _traverse(root, result):
        if root is None:
            return
        _traverse(root.left, result)
        _traverse(root.right, result)
        result.append(root.val)

    result = []
    _traverse(root, result=result)
    print(result)


def pre_iter_traversal(root):
    result = []
    stack = []
    if root:
        stack.append(root)

    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return result

def in_iter_traversal(root):
    result = []
    stack = []
    cur = root
    while cur is not None or stack:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result

def post_iter_traversal(root):
    result = []
    stack = []
    if root:
        stack.append(root)

    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return list(reversed(result))

def leval_traversal(root):
    queue1 = []
    queue2 = []
    result = []

    if root:
        queue1.append(root)

    while queue1:
        for cur in queue1:
            result.append(cur.val)
            if cur.left:
                queue2.append(cur.left)
            if cur.right:
                queue2.append(cur.right)

        queue1 = queue2
        queue2 = []
    return result



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    root = build_tree(nums)
    pre_traversal(root)
    print(pre_iter_traversal(root))
    in_traversal(root)
    print(in_iter_traversal(root))
    post_traversal(root)
    print(post_iter_traversal(root))
    print(leval_traversal(root))