class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inOrder=[]
        def inOrderTraversal(node):
            if not node :
                return
            inOrderTraversal(node.left)
            inOrder.append(node.val)
            inOrderTraversal(node.right)
        inOrderTraversal(root)
        N=len(inOrder)
        def constructTree(left,right):
            if left>right:
                return
            if left==right:
                return TreeNode(inOrder[left])
            mid=(left+right)//2
            currentRoot=TreeNode(inOrder[mid])
            currentRoot.left=constructTree(left,mid-1)
            currentRoot.right=constructTree(mid+1,right)
            return currentRoot
        return constructTree(0,N-1)
