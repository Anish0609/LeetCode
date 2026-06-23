# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head,times):
            curr=head
            prev=None

            for i in range(times):
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
    
        if head==None :
            return head
            
        left=head 
        prevleft=None
        res=None
        size=k

        while True :
            right=left
            for i in range (1,size):
                if right==None :
                    break
                right=right.next
            
            if right :
                nextleft=right.next
                reverse(left,size)
                if prevleft :
                    prevleft.next=right
                prevleft=left
                if res==None :
                    res=right
                left=nextleft
            else :
                if prevleft :
                    prevleft.next=left
                if res==None :
                    res=left    
                break
        
        return res
                




        
        
