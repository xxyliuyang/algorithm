class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_link(nums):
    if len(nums) == 0:
        return None
    res = ListNode()
    cur = res
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return res.next

def to_string(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

