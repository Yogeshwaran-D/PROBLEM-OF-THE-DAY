class Solution:
    def stack(self,node):
        if node.next == None :
            return node
        node.next=self.stack(node.next)
        if node.val >= node.next.val:
            return node
        else:
            return node.next
    def removeNodes(self, head):
        return self.stack(head)