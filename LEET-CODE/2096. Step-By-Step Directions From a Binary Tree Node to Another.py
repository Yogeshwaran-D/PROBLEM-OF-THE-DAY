class Solution:
    def getDirections(self, root, startValue, destValue) :
        def dfs(root,path,target):
            if not root :
                return ""
            if root.val == target:
                return path
            path.append("L")
            res=dfs(root.left,path,target)
            if res : return res
            path.pop()
            path.append("R")
            res = dfs(root.right,path,target)
            if res : return res
            path.pop()
            return ""
        start=dfs(root,[],startValue)
        dest=dfs(root,[],destValue)
        i=0
        while i<min(len(start),len(dest)):
            if start[i] != dest[i]:
                break
            i+=1
        return ("U" * len(start[i:])) + "".join(dest[i:])