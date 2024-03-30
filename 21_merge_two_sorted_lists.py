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
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

    def merge_two_lists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        result = None
        while list1:
            while list2:
                if list1 is None:
                    result = append(result, list2.val)
                    list2 = list2.next
                    continue

                if list1.val <= list2.val:
                    result = append(result, list1.val)
                    list1 = list1.next

                if list1 is None:
                    result = append(result, list2.val)
                    list2 = list2.next
                    continue

                if list1.val >= list2.val:
                    result = append(result, list2.val)
                    list2 = list2.next

            if list2 is None and list1:
                result = append(result, list1.val)
                list1 = list1.next

        return result

    def merge_two_lists_3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

    def list_print(self, linked_list: Optional[ListNode]):
        head = linked_list
        while head:
            print(head.val)
            head = head.next


solution = Solution()

l1 = ListNode(-9)
l1.next = ListNode(3)
l1.next.next = ListNode(7)

l2 = ListNode(5)
l2.next = ListNode(7)
l2.next.next = ListNode(8)
res = solution.merge_two_lists_3(list1=l1, list2=l2)
solution.list_print(res)

# The first intuition was to convert the linked lists into an array and then sort the array.
# The creating a linked list from the array. This solution works, except it is not optimal.

# It cracked on me that the input lists are sorted which I didn't get first.
# So, second intuition was going through two linked lists in nested loop and inserting items based
# on whatever list had the smaller one and advancing that list

# Then third intuition came from looking at YouTube that we can run one loop as long as both lists
# have value! Damn! Should have thought about it.

# Also I was using append and push because simple linking was not working. Turns out linking does work.

# At the end of the loop, curr will point to the last node in the merged list.
# However, since dummy was never updated after it was initialized, it still points to the first node in the merged list.
# This is why we return dummy.next instead of curr.next -
# because dummy.next points to the first node in the merged list, while curr.next points to the last node.
