# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked.util import ListNode, create_link, to_string

class Solution:

    def reverse(self, cur):
        if not cur:
            return cur

        c1 = None
        c2 = cur
        c3 = cur.next

        while c3:
            c2.next = c1
            c1 = c2
            c2 = c3
            c3 = c3.next
        c2.next = c1
        return c2


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast, slow = head, head
        pre = None

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None

        cur1 = head
        cur2 = slow
        cur2 = self.reverse(cur2)

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True


if __name__ == '__main__':
    solution = Solution()
    head = [1, 2, 2, 1]

    head = create_link(head)
    print(solution.isPalindrome(head))