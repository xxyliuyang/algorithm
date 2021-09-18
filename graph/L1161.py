from tree.util import build_tree

def maxLevelSum(root):
    if root is None:
        return 0
    queue1 = [root]
    queue2 = []
    max_level = 0
    cur_level = 1
    max_sum = float('-inf')
    while len(queue1) != 0 or len(queue2) != 0:
        cur_sum = 0
        while len(queue1) != 0:
            cur = queue1.pop(0)
            cur_sum += cur.val
            if cur.left:
                queue2.append(cur.left)
            if cur.right:
                queue2.append(cur.right)
        queue1 = queue2
        queue2 = []
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_level = cur_level
        cur_level += 1
    return max_level

if __name__ == '__main__':
    nums = [1, 7, 0, 7, -8, None, None]
    root = build_tree(nums)
    print(maxLevelSum(root))