# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth

        queue = [root]

        while len(queue) > 0:
            depth += 1
            for i in range(len(queue)):
                current = queue.pop(0)

                if current.left is None and current.right is None:
                    return depth

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return depth



    def print_tree(self, node: Optional[TreeNode], level=0):
        if node is not None:
            self.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            self.print_tree(node.right, level + 1)



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

solution.print_tree(root)
print(solution.min_depth(root))

# I tried to solve it recursively first, but it didn't come to me. So I tried level order traversal using queue
# to reach levels and keep track of the depth.
