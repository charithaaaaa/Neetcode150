# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val!=q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
# Time complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(h) where h is the height of the tree, which is the maximum number of nodes on the path from the root to a leaf. In the worst case of a skewed tree, the height can be equal to the number of nodes, resulting in O(n)
