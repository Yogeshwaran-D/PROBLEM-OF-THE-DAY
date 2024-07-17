class Solution:
    def delNodes(self, root, to_delete) :
        set_delete=set(to_delete)
        set_res=set([root])

        def dfs(node):
            if not node : return None
            res=node
            if node.val in set_delete:
                res=None
                set_res.discard(node)
                if node.left : set_res.add(node.left)
                if node.right : set_res.add(node.right)
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            return res
        dfs(root)
        return list(set_res)