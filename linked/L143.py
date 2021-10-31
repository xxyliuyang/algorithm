# 讲解：分割链表， https://mp.weixin.qq.com/s/wZ0JforWRPdiEkWsU9NsPw

from linked.util import ListNode, to_string, create_link
from typing import Optional

class Solution:
    def reverse(self, cur):

        c1 = None
        c2 = cur
        tmp = None
        while c2:
            tmp = c2.next
            c2.next = c1
            c1 = c2
            c2 = tmp
        return c1

    def combine(self, cur1, cur2):
        head = cur1
        cur = head
        cur1 = cur1.next

        while cur1 or cur2:
            if cur2:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next

            if cur1:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
        return head


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and head.next:
            return head
        fast, slow = head, head
        pre = None

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if fast:
            c1 = head
            c2 = slow.next
            slow.next = None
        else:
            c1 = head
            c2 = slow
            pre.next = None

        c2 = self.reverse(c2)
        res = self.combine(c1, c2)
        return res


if __name__ == '__main__':
    solution = Solution()
    head = [1,3,2,4]
    head = create_link(head)

    head = solution.reorderList(head)
    print(to_string(head))
