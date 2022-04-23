class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, x):
        self.val = x
        self.children = []


def buld_multi_tree(nums):
    if len(nums) == 0:
        return None
    root = Node(nums[0])
    queue1 = [root]
    queue2 = []
    i = 2
    while i < len(nums):
        if len(queue1) != 0:
            if nums[i] is not None:
                cur = Node(nums[i])
                queue1[0].children.append(cur)
                queue2.append(cur)
            else:
                queue1 = queue1[1:]
            i += 1
        else:
            queue1 = queue2
            queue2 = []
    return root



def build_tree(nums):
    # 利用树的结构性质构建树，利用两个队列和二叉树的数组索引关系
    if len(nums) == 0:
        return None
    root = TreeNode(nums[0])
    queue1 = [root]
    queue2 = []
    i = 0
    while i < len(nums)//2:
        while len(queue1) != 0:
            cur = queue1.pop(0)
            if i*2+1 < len(nums) and nums[i*2+1] is not None:
                cur.left = TreeNode(nums[i*2+1])
                queue2.append(cur.left)
            if i*2+2 < len(nums) and nums[i*2+2] is not None:
                cur.right = TreeNode(nums[i*2+2])
                queue2.append(cur.right)
            i += 1
        queue1 = queue2
        queue2 = []
    return root


def tree_2_array(root):
    result = []
    queue = [root]

    while queue:
        queue_tmp = []
        for node in queue:
            if node:
                result.append(node.val)
                queue_tmp.append(node.left)
                queue_tmp.append(node.right)
            else:
                result.append(None)
        queue = queue_tmp
    return result

