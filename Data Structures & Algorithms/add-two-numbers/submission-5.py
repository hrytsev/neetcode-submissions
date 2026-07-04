# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        sum=0
        res=0
        while l1 or l2 or res:
            sum=res
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            res=sum//10
            add=sum%10
            current.next=ListNode(add,None)
            current=current.next
        return dummy.next
