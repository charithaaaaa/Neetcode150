# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps
            
            if slow == fast:          # if they meet → cycle exists
                return True
        
        return False                  # reached end → no cycle
