class Solution:
    def removeLeafNodes(self, root, target) :
        if root == None :
            return None
        if root.left == None and root.right == None :
            if root.val== target :
                return None
            else:
                return root
        root.left=self.removeLeafNodes(root.left,target)
        root.right=self.removeLeafNodes(root.right,target)
        if root.left == None and root.right == None :
            if root.val== target :
                return None
            else:
                return root
        return root