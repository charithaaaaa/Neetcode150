# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None :
            return
        root.right, root.left=self.invertTree(root.left),self.invertTree(root.right)
        return root
        
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9     
#         4
#        / \
#       7   2
#      / \ / \
#     9  6 3  1
#         4 is the root node, 2 is the left child of 4 and 7 is the right child of 4. After inverting, 7 becomes the left child and 2 becomes the right child. The same process is applied to all nodes in the tree.
# Time complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(h) where h is the height of the tree, due to the recursive call stack. In the worst case of a completely unbalanced tree, this could be O(n