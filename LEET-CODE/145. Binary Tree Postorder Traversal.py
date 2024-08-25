class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        def Traversal(root):
            if root:
                Traversal(root.left)
                Traversal(root.right)
                self.res.append(root.val)
        Traversal(root)
        return self.res