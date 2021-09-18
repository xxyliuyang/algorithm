"""判断一棵树是不是镜像对称"""

from tree.util import build_tree

def is_symmetric(tree):
    """递归"""
    def compare(left, right):
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left is None and right is None:
            return True
        if left.val != right.val:
            return False

        return compare(left.right, right.left) and compare(left.left, right.right)



    if tree is None:
        return True
    return compare(tree.left, tree.right)

def is_symmetric2(tree):
    """遍历"""
    if tree is None:
        return True

    left = [tree.left]
    right = [tree.right]

    while len(left) > 0 or len(right) >0:
        if len(left) != len(right):
            return False

        left2 = []
        right2 = []
        for i in range(len(left)):
            if left[i] is None and right[i] is None:
                continue
            if left[i] is None or right[i] is None or left[i].val != right[i].val:
                return False

            left2.append(left[i].left)
            left2.append(left[i].right)
            right2.append(right[i].right)
            right2.append(right[i].left)

        left = left2
        right = right2
    return True



if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 3]
    tree = build_tree(nums)

    print(is_symmetric2(tree))

