 #Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from collections import deque
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        nodes_queue = deque([root])  # queue to process nodes level by level

        while nodes_queue:
            current_node = nodes_queue.popleft()

            # swap children of current node
            current_node.left, current_node.right = (
                current_node.right,
                current_node.left,
            )

            # add children to queue for later processing
            if current_node.left:
                nodes_queue.append(current_node.left)

            if current_node.right:
                nodes_queue.append(current_node.right)

        return root

# Time complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(w) where w is the maximum width of the tree, which is the maximum number of nodes at any level in the tree. In the worst case of a complete binary

#BY BFS