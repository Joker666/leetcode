from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    dummy = curr = ListNode()
    curr.next = head

    while curr.next and curr.next.next:
        prev = curr.next
        curr.next = curr.next.next

        prev.next = curr.next.next
        curr.next.next = prev

        curr = curr.next.next

    return dummy.next


def list_print(linked_list: Optional[ListNode]):
    head = linked_list
    while head:
        print(head.val, end='')
        if head.next:
            print(" -> ", end='')
        head = head.next
    print("\n")


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

list_print(swap_pairs(l1))
