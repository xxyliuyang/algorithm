from typing import List, Optional
from linked.util import ListNode, to_string, create_link


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        index_2_node = {}
        count = 0
        cur = head
        while cur:
            index_2_node[count] = cur
            cur = cur.next
            count += 1

        if count-n-1 < 0:
            cur_remove_node = index_2_node[count - n]
            head = cur_remove_node.next
            cur_remove_node = None
            return head
        else:
            cur_remove_node = index_2_node[count-n]
            pre_node = index_2_node[count-n-1]
            pre_node.next = cur_remove_node.next
            cur_remove_node.next = None
            return head

if __name__ == '__main__':
    head = [1, 2]
    n = 2
    head = create_link(head)
    print(to_string(head))
    solution = Solution()

    head = solution.removeNthFromEnd(head, n)
    print(to_string(head))


