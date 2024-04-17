from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        prev = None

        while curr:
            then = curr.next

            # reverse the pointer
            curr.next = prev

            # advance both prev and curr
            prev = curr
            curr = then

        return prev

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val, end='')
            if head.next:
                print(" -> ", end='')
            head = head.next
        print("\n")


solution = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

reversed_l1 = solution.reverse_list(l1)
solution.list_print(reversed_l1)

# Strange that such a simple solution did not occur to me first.
# The idea is to reverse the pointers, not swap list nodes. And advancing the two pointers after reversing.
# I couldn't do it on my own, and it took a very long time.
