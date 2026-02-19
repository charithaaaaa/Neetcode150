# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        #splitting linklist into 2 half using slow and fast pointer , when fast pointer reach end slow be at mid
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        p2=slow.next #we name 2nd half linked list as p2
        slow.next=None #slow,next becomes none so p2 and other half are not connected
        #Reversing p2
        prev=None
        while p2 and p2.next: #min of 2 nodes req
            p2next=p2.next
            p2.next=prev #set the next node of 1st node of p2 as None to reverse 
            prev=p2
            p2=p2next
        p2.next=prev
        p1=head
        while p1 and p2:
            p1next=p1.next
            p2next=p2.next
            p1.next=p2
            p2.next=p1next
            p1=p1next
            p2=p2next
#for example if we have 1->2->3->4->5
#after splitting we have 1->2->3 and 4->5
#after reversing 2nd half we have 1->2->3 and 5->4
#after merging we have 1->5->2->4->3

