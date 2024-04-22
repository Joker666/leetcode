from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = []

        if root is None:
            return visited

        queue = [root]

        while len(queue) != 0:
            len_q = len(queue)

            level = []
            for i in range(len_q):
                current = queue.pop(0)
                level.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            visited.append(level)
        return visited


solution = Solution()

root = TreeNode(1)

left = TreeNode(2)
right = TreeNode(3)

root.left = left
root.right = right

left.left = TreeNode(4)
left.right = TreeNode(6)

right_right = TreeNode(5)
right.right = right_right

s = solution.level_order_traversal(root)
print(s)

# In the queue-based approach, the left node is inserted first and then the right node.
# The intuition behind this is that the left node will be popped first in the next iteration
# since we are pushing into a queue which is FIFO(First in First out).
# We don't necessarily need to do this for BFS, since we are doing level order traversal, but
# it's nice to move from left to right.

# However, for pushing one level at a time, a simple queue will not work; we need to keep track of levels.
# I couldn't solve this until I got some clue from ChatGPT.
# The idea is the length of the queue is the number of nodes for that level.
