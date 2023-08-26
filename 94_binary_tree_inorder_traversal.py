from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])

    def traverse(self, node: Optional[TreeNode], f_list: List[int]) -> List[int]:
        if not node:
            return f_list

        if node.left:
            self.traverse(node.left, f_list)
        f_list.append(node.val)
        if node.right:
            self.traverse(node.right, f_list)

        return f_list


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


s = solution.inorder_traversal(root)
print(s)
