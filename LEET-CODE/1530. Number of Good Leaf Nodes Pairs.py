class Solution:
    def countPairs(self, root, distance):
        self.pairs=0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left=dfs(node.left)
            right=dfs(node.right)
            for d1 in left:
                for d2 in right:
                    if d1+d2 <= distance:
                        self.pairs+=1
            all_dist=left+right
            return [d+1 for d in all_dist]
        dfs(root)
        return self.pairs