class Solution:
    def mergeNodes(self, head):
        temp=head.next
        head1=head
        while temp:
            sumValues=0
            while temp.val!=0:
                sumValues+=temp.val
                temp=temp.next
            head1.val=sumValues
            if temp.next is None:
                head1.next=None
                return head
            head1.next=temp
            head1=head1.next
            temp=temp.next
