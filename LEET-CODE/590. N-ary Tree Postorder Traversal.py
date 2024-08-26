class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.res=[]
        def dfs(root):
            for node in root.children:
                dfs(node)
            self.res.append(root.val)
        dfs(root)
        return self.res