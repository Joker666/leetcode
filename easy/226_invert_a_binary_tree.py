from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        l = self.invert_tree(root.left)
        r = self.invert_tree(root.right)

        root.left = r
        root.right = l

        return root

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
solution.invert_tree(root)
solution.print_tree(root)
