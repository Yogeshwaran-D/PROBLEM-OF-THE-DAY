class Solution:
    def distributeCoins(self, root) :
        self.moves = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            tot = left+right+root.val-1
            self.moves += abs(tot)
            return tot
        
        dfs(root)
        return self.moves