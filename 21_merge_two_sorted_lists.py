from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def push(head_ref: Optional[ListNode], new_data: int) -> ListNode:
    new_node = ListNode(new_data)
    new_node.next = head_ref
    return new_node


def append(head_ref: Optional[ListNode], new_data: int) -> ListNode:
    new_node = ListNode(new_data)

    if head_ref is None:
        head_ref = new_node
        return head_ref

    head = head_ref
    while head:
        if head.next is None:
            head.next = new_node
            break
        head = head.next

    return head_ref


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        arr = []

        head = list1
        while head:
            arr.append(head.val)
            head = head.next

        head = list2
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        head = None
        for x in arr:
            head = append(head, x)

        return head

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val)
            head = head.next


solution = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
res = solution.merge_two_lists(list1=l1, list2=l2)
solution.list_print(res)
