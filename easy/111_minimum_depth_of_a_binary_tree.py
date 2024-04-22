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

    def min_depth_2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_subtree_depth = self.min_depth_2(root.left)
        right_subtree_depth = self.min_depth_2(root.right)

        if root.left is None:
            return right_subtree_depth + 1
        if root.right is None:
            return left_subtree_depth + 1

        return min(left_subtree_depth, right_subtree_depth) + 1

    def print_tree(self, node: Optional[TreeNode], level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            self.print_tree(node.left, level + 1)


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
print(solution.min_depth_2(root))

# I tried to solve it recursively first, but it didn't come to me. So I tried level order traversal using queue
# to reach levels and keep track of the depth.

# After seeing the recursive solution, I tried to solve it myself. It is similar to the max depth problem.
# Except, if the binary tree is not a complete tree, it doesn't work. Because if a left node is none, but
# the right node has value, it will count the depth of the level as 0 since min(0, 1) = 0.
# To account for that, we return early when we are sure that at least the level exists.
