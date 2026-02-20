# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#1 take two pointers p1 @ head and p2 @ dummy pointing to head to handle 1 node condition also count as 0 to count the nodes.
#2 move the p1 unit it reaches None , also p2 starts moving when p1 count >n
# when p1 reaches None , while loops stops and we print p2 next next node.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1=head
        dumy=ListNode(0,head) #before head node
        p2=dumy
        count=0
        while p1 !=None:
            p1=p1.next
            count+=1
            if count>n:
                p2=p2.next
        p2.next=p2.next.next
        return dumy.next #handle 1 node linked list

# for example if we have 1->2->3->4->5 and n=2
# after 1st iteration p1=2 , count=1 , p2=0
# after 2nd iteration p1=3 , count=2 , p2=0
# after 3rd iteration p1=4 , count=3 , p2=1
# after 4th iteration p1=5 , count=4 , p2=2
# after 5th iteration p1=None , count=5 , p2=3
# after while loop p2 is at 3 and we set p2 next as p2 next next which is 5 and we return dummy next which is 1 
    