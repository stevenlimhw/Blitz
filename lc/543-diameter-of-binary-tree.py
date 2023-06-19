from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # keep track of the diameter of a given node
        # which is the sum of the max depths of a given node to the left and to the right
        self.res = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max depth can be to the left or right (subtrees)
        if not root:
            return 0
        left_subtree = self.maxDepth(root.left)
        right_subtree = self.maxDepth(root.right)
        self.res = max(self.res, left_subtree + right_subtree)
        return max(left_subtree, right_subtree) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.res
        