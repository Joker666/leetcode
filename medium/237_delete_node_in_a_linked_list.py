# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        second = node.next
        third = node.next.next
        node.next = third
        node.val = second.val

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val, end='')
            if head.next:
                print(" -> ", end='')
            head = head.next
        print("\n")



solution = Solution()

# Example 1:
l1 = ListNode(1)
second_node = ListNode(2)
l1.next = second_node

third_node = ListNode(3)
second_node.next = third_node

third_node.next = ListNode(4)

solution.list_print(l1)
solution.delete_node(third_node)
solution.list_print(l1)

# This was a quite interesting problem as we will not be given the head of the node, instead a node in the middle.
# I had no clue, so I watched a youtube video. Found out the solution is quite small, albeit without seeing it.
# Since I knew the solution was small, I was able to solve it myself.
#
# Essentially updating the value of the current node is what solves this problem.
