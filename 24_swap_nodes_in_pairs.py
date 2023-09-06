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
        temp = head.next.next  # save the third node or the next pair
        head.next.next = head  # make the head tail to the second node
        head = head.next  # put the second node in the head
        head.next.next = self.swap_pairs(temp)
        return head

    def swap_pairs_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr:
            # save ptrs
            temp = curr.next.next  # save the third node or the next pair
            second = curr.next  # save the second node

            # reverse
            second.next = curr  # second's next would be current
            curr.next = temp  # curr is second now, so curr's next would be third
            prev.next = second  # prev is dummy, prev's next is the head, which will be second

            prev, curr = curr, temp

        return dummy.next

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val, end=" ")
            head = head.next
        print("\n")


solution = Solution()

# Example 1:
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

# Before swap: 1 -> 2 -> 3 -> 4
# After swap: 2 -> 1 -> 4 -> 3

res1 = solution.swap_pairs_2(l1)
solution.list_print(res1)

# Example 2:
l2 = ListNode(1)
l2.next = ListNode(2)

# Before swap: 1 -> 2
# After swap: 2 -> 1

res2 = solution.swap_pairs(l2)
solution.list_print(res2)

# Example 3:
l3 = None

# Before swap: None
# After swap: None

res3 = solution.swap_pairs(l3)
solution.list_print(res3)


# This I could not solve without help. My first intuition was swapping the head and head->next.
# I stored the head in temp and tried to put it in head->next, but it created an infinite linked list.

# The intuition here is, to swap first and second node, we need to make the second node head.
# Where does the first node go? We need to make the first node tail to the second node *before*
# second node becomes head. So when second node becomes head, the linked list kind of advanced and
# first node is now second node. Swapped! And before we do all of this, we hold the third node in a temp
# variable and recursively call the swap functions and add the result back as the third node.
