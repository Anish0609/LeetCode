# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right :
            return head

        
        before=0
        pos=1
        t=head
        
        while pos<left :
            before=t
            t=t.next
            pos+=1
        
        curr=t
        prev=None
        times=right-left+1

        for i in range(times):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        
        if left==1:
            head=prev
        else :
            before.next=prev
        t.next=curr

        return head
        
        