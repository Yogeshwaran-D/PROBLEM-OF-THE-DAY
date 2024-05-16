class Solution:
    def evaluateTree(self, root):
        if root.left == None and root.right == None:
            return root.val == 1 
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)