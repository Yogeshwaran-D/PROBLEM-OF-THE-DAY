class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,lis,total):   
            if total == target:
                res.append(lis.copy())
                return
            if i==len(candidates) or total>target:
                return
            lis.append(candidates[i])
            dfs(i+1,lis,total+candidates[i])
            lis.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,lis,total)
        dfs(0,[],0)
        return res