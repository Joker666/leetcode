# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

    def traverse(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth

        left_subtree_depth = self.traverse(root.left, depth)
        right_subtree_depth = self.traverse(root.right, depth)

        return max(left_subtree_depth, right_subtree_depth) + 1

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
print(solution.max_depth(root))