from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head


solution = Solution()

# Example 1:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Before swap: 1 -> 2 -> 3 -> 4
# After swap: 2 -> 1 -> 4 -> 3

solution.swap_pairs(head)

# Example 2:
head = ListNode(1)
head.next = ListNode(2)

# Before swap: 1 -> 2
# After swap: 2 -> 1

solution.swap_pairs(head)

# Example 3:
head = None

# Before swap: None
# After swap: None

solution.swap_pairs(head)
