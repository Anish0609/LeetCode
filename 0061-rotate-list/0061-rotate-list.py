# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None :
            return head
        
        n=1
        last=head

        while last.next!=None :
            n+=1
            last=last.next
        
        k=k%n
        if k==0 :
            return head
        
        c=n-k
        count=1
        t=head
        res=0

        while count!=c :
            count+=1
            t=t.next
        
        last.next=head
        res=t.next
        t.next=None
    
        return res
        

        
        