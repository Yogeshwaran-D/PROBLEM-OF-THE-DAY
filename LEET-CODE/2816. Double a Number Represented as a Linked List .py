class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head):
        prev=None
        current=head
        next=head.next
        while(next != None ):
            current.next=prev
            prev=current
            current=next
            next=next.next
        current.next=prev
        return current
    def doubleIt(self, head) :
        head = self.reverseList(head)
        temp=None
        carry=0
        while(head != None):
            val=2*head.val
            compute=val+carry
            carry=compute//10
            compute=compute % 10
            t=ListNode(compute)
            t.next=temp
            temp=t
            head=head.next
        if carry!=0:
            t=ListNode(carry)
            t.next=temp
            temp=t
        return temp
