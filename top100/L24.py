from typing import Optional
from linked.util import ListNode, create_link, to_string

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        duty0 = ListNode()
        duty1 = ListNode()
        duty2 = ListNode()
        duty0.next = duty1
        duty1.next = duty2
        duty2.next = head

        pre = duty0
        slow = duty1
        fast = duty2

        while fast.next and fast.next.next:
            pre = pre.next.next
            slow = slow.next.next
            fast = fast.next.next

            slow.next = fast.next
            pre.next = fast
            fast.next = slow
            fast, slow = slow, fast
        return duty2.next


if __name__ == '__main__':
    head = [1]
    head = create_link(head)
    print(to_string(head))

    solution = Solution()
    print(to_string(solution.swapPairs(head)))