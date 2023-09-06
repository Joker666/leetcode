from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Swap first two nodes
        temp = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = self.swap_pairs(temp)
        return head

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val, end=" ")
            head = head.next
        print("\n")


solution = Solution()

# # Example 1:
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

# Before swap: 1 -> 2 -> 3 -> 4
# After swap: 2 -> 1 -> 4 -> 3

res1 = solution.swap_pairs(l1)
solution.list_print(res1)

# Example 2:
l2 = ListNode(1)
l2.next = ListNode(2)

# Before swap: 1 -> 2
# After swap: 2 -> 1

res2 = solution.swap_pairs(l2)
solution.list_print(res2)

# # Example 3:
l3 = None

# Before swap: None
# After swap: None

res3 = solution.swap_pairs(l3)
solution.list_print(res3)


# This I could not solve without help. My first intuition was swapping the head and head->next.
# I stored the head in temp and tried to put it in head->next, but it created an infinite linked list.

#
