from linked.util import ListNode,create_link,to_string
def addTwoNumbers(l1, l2):# 两个链表数字相加
    res = ListNode()
    cur = res
    hold = 0
    while l1 and l2:
        v1 = l1.val
        v2 = l2.val
        new_val = v1 + v2 + hold
        hold = new_val // 10
        cur.next = ListNode(new_val%10)
        cur = cur.next
        l1,l2 = l1.next,l2.next
    if l1:
        while l1:
            v1 = l1.val
            new_val = v1 + hold
            hold = new_val // 10
            cur.next = ListNode(new_val % 10)
            cur = cur.next
            l1 = l1.next
    if l2:
        while l2:
            v2 = l2.val
            new_val = v2 + hold
            hold = new_val // 10
            cur.next = ListNode(new_val % 10)
            cur = cur.next
            l2 = l2.next
    if hold != 0:
        cur.next = ListNode(hold)
    return res.next



if __name__ == '__main__':
    l1 = create_link([5])
    l2 = create_link([5])
    res = addTwoNumbers(l1,l2)
    print(to_string(res))
