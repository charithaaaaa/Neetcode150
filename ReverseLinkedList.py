# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next #storing next element in nxt
            curr.next = prev #reverse arrow
            prev = curr #ah prev node ni curr cheyali
            curr = nxt 

        return prev
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 ->
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)       
head.next.next.next.next = ListNode(5)
# Reversing the linked list
sol = Solution()
reversed_head = sol.reverseList(head)
# Printing the reversed linked list
curr = reversed_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
# Output: 5 -> 4 -> 3 -> 2 -> 1 ->